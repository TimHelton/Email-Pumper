import cx_Oracle
from emailerMessageInsUpdScreen import *
from tkinter import messagebox

global index, rows, currentScreen
index = 0
currentScreen = None

def readDb(top, queryScreen, b2, b3, b4, b5, b6, b7, b8):

    global rows, rowcount, currentScreen

    whereClause = ""
    if queryScreen.e1.get():
        whereClause += "core_only like '%" + queryScreen.e1.get() + "%' and "
    if queryScreen.e2.get():
        whereClause += "subject like '%" + queryScreen.e2.get() + "%' and "
    message = queryScreen.e3.get(0.0, END).rstrip('\n')
    if message:
        whereClause += "message like '%" + message + "%' and "
    if queryScreen.e4.get():
        whereClause += "attachmentfile like '%" + queryScreen.e4.get() + "%' and "
    whereClause += "date_sent is null"

    queryCommand = "select email_id, core_only, subject, message, attachmentfile, attachment from email where " + whereClause

    print(queryCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

    try:
        cursor.execute(queryCommand)
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Query Status", "Can't process query. " + error.message)

    rows = cursor.fetchall()
    rowcount = len(rows)
    cursor.close()

    #conn.close()  # Can't close the connection or the clob read fails when displaying the rows

    if (rowcount > 0):
        global index
        b2.config(state=NORMAL)
        b7.config(state=NORMAL)
        if (rowcount > 1):
            b6.config(state=NORMAL)
        updateScreen = MessageInsUpdScreen(top)
        currentScreen = updateScreen
        queryScreen.eraseScreen()
        index = 0
        showOneRow(updateScreen, b3, b4, b8)
        if queryScreen.e4.get():
            b8.config(state=NORMAL)
        else:
            b8.config(state=DISABLED)
    else:
        messagebox.showinfo("Query Status", "No rows found.")

def showNextRow(b3, b4, b5, b6, b7, b8):
    global index
    index += 1
    showOneRow(currentScreen, b3, b4, b8)
    b5.config(state=NORMAL)
    b7.config(state=NORMAL)
    if index == rowcount - 1:
        b6.config(state=DISABLED)

def showPreviousRow(b3, b4, b5, b6, b7, b8):
    global index
    index -= 1
    showOneRow(currentScreen, b3, b4, b8)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    if index == 0:
        b5.config(state=DISABLED)

def showOneRow(screen, b3, b4, b8):
    global index, attachment
    screen.clearAll()
    screen.e1.delete(0, END)

    if rows[index][1] != None:                  # core_only
        screen.e1.insert(0, rows[index][1])
    if rows[index][2] != None:                  # subject
        screen.e2.insert(0, rows[index][2])
    if rows[index][3] != None:                  # message
        screen.e3.insert(0.0, str(rows[index][3].read()))
    if rows[index][4] != None:                  # attachmentFile
        screen.e4.config(state=NORMAL)
        screen.e4.insert(0, rows[index][4])
        screen.e4.config(state=DISABLED)
        attachment = rows[index][5].read()
        b3.config(state=DISABLED)
        b4.config(state=NORMAL)
        b8.config(state=NORMAL)
    else:
        b3.config(state=NORMAL)
        b4.config(state=DISABLED)
        b8.config(state=DISABLED)

def getKeyForCurrentRow():
    return rows[index][0]

def getCurrentScreen(screen):
    if currentScreen == None:
        return screen
    else:
        return currentScreen

def getAttachment():
    return attachment
