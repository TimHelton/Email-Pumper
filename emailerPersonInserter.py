from emailerPersonInsUpdScreen import *
import cx_Oracle

def insert(top):

    global insertScreen, b0, b1

    insertScreen = PersonInsUpdScreen(top)

    b0 = Button(top, text="Clear", width=10, command=lambda:insertScreen.clearAll())
    b0.grid(row=1, column=2, padx=15, pady=5)

    b1 = Button(top, text="Insert", width=10, command=lambda:writeDb(insertScreen))
    b1.grid(row=2, column=2, padx=15, pady=5)

def writeDb(insertScreen):
    values = "('" + insertScreen.e0.get() + "', "
    values = values + "'" + insertScreen.e1.get() + "', "
    values = values + "'" + insertScreen.e2.get() + "', "
    values = values + "'" + insertScreen.e3.get() + "', "
    values = values + "'" + insertScreen.e4.get() + "', "
    values = values + "'" + insertScreen.e5.get() + "', "
    values = values + "'" + insertScreen.e6.get() + "', "
    values = values + "'" + insertScreen.e7.get() + "', "
    values = values + "'" + insertScreen.e8.get() + "', "
    values = values + "'" + insertScreen.e9.get() + "', "
    values = values + "'" + insertScreen.e10.get() + "', "
    values = values + "'" + insertScreen.e11.get() + "', "
    values = values + "'" + insertScreen.e12.get() + "')"

    insertCommand = "Insert into person values " + values

    print(insertCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

    try:
        cursor.execute(insertCommand)
        messagebox.showinfo("Insert Status", "One record inserted.")
        insertScreen.clearAll()
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Insert Status", "Can't insert record. " + error.message)

    cursor.close()
    conn.commit()
    conn.close()

    insertScreen.clearAll

def eraseScreen():
    b0.grid_remove()
    b1.grid_remove()
    insertScreen.eraseScreen()
