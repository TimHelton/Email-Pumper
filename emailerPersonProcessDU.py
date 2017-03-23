import cx_Oracle
from emailerPersonInsUpdScreen import *
from tkinter import messagebox

global index, rows, currentScreen
index = 0
currentScreen = None

def readDb(top, queryScreen, b2, b4):

    global rows, rowcount, currentScreen

    whereClause = ""
    if (queryScreen.e0.get()):
        whereClause = whereClause + "email like '%" + queryScreen.e0.get() + "%' and "
    if (queryScreen.e1.get()):
        whereClause = whereClause + "last_name like '%" + queryScreen.e1.get() + "%' and "
    if (queryScreen.e2.get()):
        whereClause = whereClause + "first_name like '%" + queryScreen.e2.get() + "%' and "
    if (queryScreen.e3.get()):
        whereClause = whereClause + "address1 like '%" + queryScreen.e3.get() + "%' and "
    if (queryScreen.e4.get()):
        whereClause = whereClause + "address2 like '%" + queryScreen.e4.get() + "%' and "
    if (queryScreen.e5.get()):
        whereClause = whereClause + "city like '%" + queryScreen.e5.get() + "%' and "
    if (queryScreen.e6.get()):
        whereClause = whereClause + "state like '%" + queryScreen.e6.get() + "%' and "
    if (queryScreen.e7.get()):
        whereClause = whereClause + "zipcode like '%" + queryScreen.e7.get() + "%' and "
    if (queryScreen.e8.get()):
        whereClause = whereClause + "phone1 like '%" + queryScreen.e8.get() + "%' and "
    if (queryScreen.e9.get()):
        whereClause = whereClause + "phone1_type like '%" + queryScreen.e9.get() + "%' and "
    if (queryScreen.e10.get()):
        whereClause = whereClause + "phone2 like '%" + queryScreen.e10.get() + "%' and "
    if (queryScreen.e11.get()):
        whereClause = whereClause + "phone2_type like '%" + queryScreen.e11.get() + "%' and "
    if (queryScreen.e12.get()):
        whereClause = whereClause + "core like '%" + queryScreen.e12.get() + "%' and "

    whereClause = whereClause + "1 = 1"

    queryCommand = "select * from person where " + whereClause

    print(queryCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()
    cursor.execute(queryCommand)
    rows = cursor.fetchall()
    rowcount = len(rows)
    cursor.close()
    conn.close()

    if(rowcount > 0):
        global currentScreen, index
        b2.config(state = NORMAL)
        if(rowcount > 1):
            b4.config(state = NORMAL)
        updateScreen = PersonInsUpdScreen(top)
        currentScreen = updateScreen
        queryScreen.eraseScreen()
        index = 0
        showOneRow(updateScreen)
    else:
        messagebox.showinfo("Query Status", "No rows found.")

def showNextRow(b3, b4):
    global index
    index = index + 1
    showOneRow(currentScreen)
    b3.config(state = NORMAL)
    if index == rowcount - 1:
        b4.config(state = DISABLED)

def showPreviousRow(b3, b4):
    global index
    index = index - 1
    showOneRow(currentScreen)
    b4.config(state = NORMAL)
    if index == 0:
        b3.config(state = DISABLED)

def showOneRow(screen):
    global index
    screen.clearAll()
    screen.e12.delete(0, END)
    screen.e0.insert(0, rows[index][0])
    if rows[index][1] != None:
        screen.e1.insert(0, rows[index][1])
    if rows[index][2] != None:
        screen.e2.insert(0, rows[index][2])
    if rows[index][3] != None:
        screen.e3.insert(0, rows[index][3])
    if rows[index][4] != None:
        screen.e4.insert(0, rows[index][4])
    if rows[index][5] != None:
        screen.e5.insert(0, rows[index][5])
    if rows[index][6] != None:
        screen.e6.insert(0, rows[index][6])
    if rows[index][7] != None:
        screen.e7.insert(0, rows[index][7])
    if rows[index][8] != None:
        screen.e8.insert(0, rows[index][8])
    if rows[index][9] != None:
        screen.e9.insert(0, rows[index][9])
    if rows[index][10] != None:
        screen.e10.insert(0, rows[index][10])
    if rows[index][11] != None:
        screen.e11.insert(0, rows[index][11])
    screen.e12.insert(0, rows[index][12])

def getKeyForCurrentRow():
    return rows[index][0]

def getCurrentScreen(screen):
    if currentScreen == None:
        return screen
    else:
        return currentScreen
