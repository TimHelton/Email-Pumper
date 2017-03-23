from emailerPersonProcessDU import *
from emailerPersonQueryScreen import *
import cx_Oracle

def delete(top):
    global queryScreen, b0, b1, b2, b3, b4

    queryScreen = PersonQueryScreen(top)
    b0 = Button(top, text="Clear", width=10, command=lambda:clearAll(top))
    b0.grid(row=1, column=2, padx=15, pady=5)
    b1 = Button(top, text="Query", width=10, command=lambda:readDb(top, queryScreen, b2, b4))
    b1.grid(row=2, column=2, padx=15, pady=5)
    b2 = Button(top, text="Delete", width=10, command=lambda:deleteFromDb(top, b2, b3, b4), state='disabled')
    b2.grid(row=3, column=2, padx=15, pady=5)
    b3 = Button(top, text="Previous", width=10, command=lambda:showPreviousRow(b3, b4), state='disabled')
    b3.grid(row=5, column=2, padx=15, pady=5)
    b4 = Button(top, text="Next", width=10, command=lambda:showNextRow(b3, b4), state='disabled')
    b4.grid(row=6, column=2, padx=15, pady=5)

def eraseScreen():
    b0.grid_remove()
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    queryScreen.eraseScreen()
    currScreen = getCurrentScreen(queryScreen)
    currScreen.eraseScreen()

def deleteFromDb(top, b2, b3, b4):
    deleteCommand = "Delete from person where email = '" + getKeyForCurrentRow() + "'"
    print(deleteCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()

    try:
        cursor.execute(deleteCommand)
        messagebox.showinfo("Delete Status", "One record deleted.")
        queryScreen.clearAll()
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Delete Status", "Can't delete record. " + error.message)

    cursor.close()
    conn.commit()
    conn.close()

    clearAll(top)

def clearAll(top):
    global queryScreen
    currScreen = getCurrentScreen(queryScreen)
    currScreen.clearAll()
    if currScreen != queryScreen:
        queryScreen = PersonQueryScreen(top)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
