from emailerMessageProcessDU import *
from emailerMessageInsUpdScreen import *
from emailerMessageQueryScreen import *
import cx_Oracle
import os
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from io import BytesIO
import tkinter as tk

global attachment
attachment = ""

def queryForUpdate(top):

    global queryScreen, b0, b1, b2, b3, b4, b5, b6, b7, b8

    queryScreen = MessageQueryScreen(top)

    b0 = Button(top, text="Clear", width=15, command=lambda: clearAll(top))
    b0.grid(row=1, column=2, padx=15, pady=5)
    b1 = Button(top, text="Query", width=15, command=lambda: readDb(top, queryScreen, b2, b3, b4, b5, b6, b7, b8))
    b1.grid(row=2, column=2, padx=15, pady=5)
    b2 = Button(top, text="Update", width=15, command=lambda: updateDb(top, b2, b3, b4, b7, b8), state='disabled')
    b2.grid(row=3, column=2, padx=15, pady=5)
    b3 = Button(top, text="Add Attachment", width=15, command=lambda: addAttachment(queryScreen), state='disabled')
    b3.grid(row=5, column=2, padx=15, pady=5)
    b4 = Button(top, text="Delete Attachment", width=15, command=lambda: deleteAttachment(queryScreen), state='disabled')
    b4.grid(row=6, column=2, padx=15, pady=5)
    b5 = Button(top, text="Previous", width=15, command=lambda: showPreviousRow(b3, b4, b5, b6, b7, b8), state='disabled')
    b5.grid(row=8, column=2, padx=15, pady=5)
    b6 = Button(top, text="Next", width=15, command=lambda: showNextRow(b3, b4, b5, b6, b7, b8), state='disabled')
    b6.grid(row=9, column=2, padx=15, pady=5)
    b7 = Button(top, text="Send", width=15, command=lambda: sendMessage())
    b7.grid(row=12, column=2, padx=5, pady=5)
    b7.config(state=DISABLED)
    b8 = Button(top, text="Show Attachment", width=15, command=lambda: showAttachment(queryScreen), state=DISABLED)
    b8.grid(row=28, column=2, padx=5, pady=5)

def showAttachment(queryScreen):
    path = getCurrentScreen(queryScreen).e4.get()
    name, extension = os.path.splitext(path)

    if (extension == '.jpg' or extension == '.JPG' or
        extension == '.jpeg' or extension == '.JPEG' or
        extension == '.png' or extension == '.PNG'):

        childWindow = Toplevel()
        childWindow.title(path)
        bytesFile = BytesIO(bytes(getAttachment()))
        imageFh = Image.open(bytesFile)
        image = ImageTk.PhotoImage(imageFh)
        tk.Label(childWindow, image=image).grid()
        childWindow.mainloop()
    else:
        messagebox.showinfo("Unsupported Extension", "Files ending in " + extension + " can not be displayed")


def sendMessage():

    email_id = getKeyForCurrentRow()

    args = [email_id]

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

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
    b7.config(state=DISABLED)

def eraseScreen():
    b0.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b6.grid_remove()
    b7.grid_remove()
    b8.grid_remove()
    queryScreen.eraseScreen()
    currScreen = getCurrentScreen(queryScreen)
    currScreen.eraseScreen()

def updateDb(top, b2, b3, b4, b7, b8):

    global attachment

    currentScreen = getCurrentScreen(queryScreen)

    updateCommand = "Update email set "
    updateCommand += "core_only = '" + currentScreen.e1.get() + "', "
    updateCommand += "subject = :subject, "
    updateCommand += "message = :message, "
    updateCommand += "attachmentfile = '" + currentScreen.e4.get() + "', "
    updateCommand += "attachment = :blob "
    updateCommand += "where email_id = " + str(getKeyForCurrentRow())

    print(updateCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()
    try:
        cursor.execute(updateCommand, subject=currentScreen.e2.get(), message=currentScreen.e3.get(0.0, END),
                       blob=attachment )
        messagebox.showinfo("Update Status", "One Row Updated")
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Update Status", "Can't update record. " + error.message)

    cursor.close()
    conn.commit()
    conn.close()

    if attachment != NONE:
        b8.config(status=NORMAL)

def clearAll(top):
    global queryScreen
    currScreen = getCurrentScreen(queryScreen)
    currScreen.clearAll()
    if currScreen != queryScreen:
        queryScreen = MessageQueryScreen(top)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

def deleteAttachment(queryScreen):

    global attachment

    attachment = None
    currentScreen = getCurrentScreen(queryScreen)
    currentScreen.e4.config(state=NORMAL)
    currentScreen.e4.delete(0, END)
    currentScreen.e4.config(state=DISABLED)
    b3.config(state=NORMAL)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b8.config(state=DISABLED)

def addAttachment(queryScreen):

    global attachment

    username = os.environ['USERNAME']
    filename = askopenfilename(initialdir="C:/users/" + username + "/Documents")
    if filename:
        currentScreen = getCurrentScreen(queryScreen)
        currentScreen.e4.config(state=NORMAL)
        currentScreen.e4.insert(0, filename)
        currentScreen.e4.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=NORMAL)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b8.config(state=NORMAL)

        with open(filename, 'rb') as file:
            attachment = file.read()

