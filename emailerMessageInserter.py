from emailerMessageInsUpdScreen import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
import cx_Oracle
from PIL import ImageTk, Image
from io import BytesIO

global attachment
attachment = ""

def insert(top):

    global insertScreen, b0, b1, b2, b3, b4, b5

    insertScreen = MessageInsUpdScreen(top)

    b0 = Button(top, text="Clear", width=15, command=lambda: clearAll(insertScreen))
    b0.grid(row=1, column=2, padx=5, pady=5)

    b1 = Button(top, text="Insert", width=15, command=lambda: writeDb(insertScreen))
    b1.grid(row=2, column=2, padx=5, pady=5)

    b2 = Button(top, text="Add Attachment", width=15, command=lambda: addAttachment(insertScreen))
    b2.grid(row=5, column=2, padx=5, pady=5)

    b3 = Button(top, text="Delete Attachment", width=15, command=lambda: deleteAttachment(insertScreen))
    b3.grid(row=6, column=2, padx=5, pady=5)
    b3.config(state=DISABLED)

    b4 = Button(top, text="Send", width=15, command=lambda: sendMessage())
    b4.grid(row=9, column=2, padx=5, pady=5)
    b4.config(state=DISABLED)

    b5 = Button(top, text="Show Attachment", width=15, command=lambda: showAttachment(insertScreen), state=DISABLED)
    b5.grid(row=28, column=2, padx=5, pady=5)

def showAttachment(insertScreen):
    path = insertScreen.e4.get()
    name, extension = os.path.splitext(path)

    if (extension == '.jpg' or extension == '.JPG' or
        extension == '.jpeg' or extension == '.JPEG' or
        extension == '.png' or extension == '.PNG'):

        childWindow = Toplevel()
        childWindow.title(path)
        bytesFile = BytesIO(attachment)
        imageFh = Image.open(bytesFile)
        image = ImageTk.PhotoImage(imageFh)
        tk.Label(childWindow, image=image).grid()
        childWindow.mainloop()
    else:
        messagebox.showinfo("Unsupported Extension", "Files ending in " + extension + " can not be displayed")

def sendMessage():

    selectCommand = "select max(email_id) from email"

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

    try:
        cursor.execute(selectCommand)
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Query Status", "Can't execute query. " + error.message)

    row = cursor.fetchone()
    email_id = row[0]

    args = [email_id]

    try:
        cursor.callproc('send_many', args)
        messagebox.showinfo("Send Status", "Email sent.")
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Send Status", "Can't execute send command. " + error.message)

    cursor.close()
    conn.close()

    print("Sending Message " + str(email_id))

    b4.config(state=DISABLED)

def deleteAttachment(insertScreen):

    global attachment

    attachment = None
    insertScreen.e4.config(state=NORMAL)
    insertScreen.e4.delete(0, END)
    insertScreen.e4.config(state=DISABLED)
    b2.config(state=NORMAL)
    b3.config(state=DISABLED)
    b5.config(state=DISABLED)

def addAttachment(insertScreen):

    global attachment

    username = os.environ['USERNAME']
    filename = askopenfilename(initialdir="C:/users/" + username + "/Documents")
    if filename:
        insertScreen.e4.config(state=NORMAL)
        insertScreen.e4.insert(0, filename)
        insertScreen.e4.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=NORMAL)
        b5.config(state=NORMAL)

        with open(filename, 'rb') as file:
            attachment = file.read()

def writeDb(insertScreen):

    global attachment

    columns = "(core_only, subject, message"
    if attachment:
        columns += ", attachmentfile, attachment"
    columns += ")"

    values = "("
    values += "'" + insertScreen.e1.get() + "', "       # Core_only
    values += " :subject, "                             # Subject
    values += " :message "                              # Message
    if attachment:
        values += ", '" + insertScreen.e4.get() + "', "         # Attachment file
        values += ":blob "
    values += ")"

    insertCommand = "Insert into email " + columns + " values " + values
    print(insertCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

    try:
        if attachment:
            cursor.execute(insertCommand, subject=insertScreen.e2.get(),
                           blob=attachment, message=insertScreen.e3.get(0.0, END))
        else:
            cursor.execute(insertCommand, subject=insertScreen.e2.get(), message=insertScreen.e3.get(0.0, END))
        messagebox.showinfo("Insert Status", "One record inserted.")
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Insert Status", "Can't insert record. " + error.message)

    cursor.close()
    conn.commit()
    conn.close()

    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=NORMAL)

def clearAll(insertScreen):
    insertScreen.clearAll()
    deleteAttachment(insertScreen)
    b1.config(state=NORMAL)
    b4.config(state=DISABLED)

def eraseScreen():
    b0.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    insertScreen.eraseScreen()
