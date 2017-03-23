from emailerPersonProcessDU import *
from emailerPersonInsUpdScreen import *
from emailerPersonQueryScreen import *
import cx_Oracle

def queryForUpdate(top):

    global queryScreen, b0, b1, b2, b3, b4

    queryScreen = PersonQueryScreen(top)

    b0 = Button(top, text="Clear", width=10, command=lambda:clearAll(top))
    b0.grid(row=1, column=2, padx=15, pady=5)
    b1 = Button(top, text="Query", width=10, command=lambda:readDb(top, queryScreen, b2, b4))
    b1.grid(row=2, column=2, padx=15, pady=5)
    b2 = Button(top, text="Update", width=10, command=lambda:updateDb(top, b2, b3, b4), state='disabled')
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

def updateDb(top, b2, b3, b4):
    currentScreen = getCurrentScreen(queryScreen)
    updateCommand = "Update person set "
    updateCommand = updateCommand + "email = '" + currentScreen.e0.get() + "', "
    updateCommand = updateCommand + "last_name = '" + currentScreen.e1.get() + "', "
    updateCommand = updateCommand + "first_name = '" + currentScreen.e2.get() + "', "
    updateCommand = updateCommand + "address1 = '" + currentScreen.e3.get() + "', "
    updateCommand = updateCommand + "address2 = '" + currentScreen.e4.get() + "', "
    updateCommand = updateCommand + "city = '" + currentScreen.e5.get() + "', "
    updateCommand = updateCommand + "state = '" + currentScreen.e6.get() + "', "
    updateCommand = updateCommand + "zipcode = '" + currentScreen.e7.get() + "', "
    updateCommand = updateCommand + "phone1 = '" + currentScreen.e8.get() + "', "
    updateCommand = updateCommand + "phone1_type = '" + currentScreen.e9.get() + "', "
    updateCommand = updateCommand + "phone2 = '" + currentScreen.e10.get() + "', "
    updateCommand = updateCommand + "phone2_type = '" + currentScreen.e11.get() + "', "
    updateCommand = updateCommand + "core = '" + currentScreen.e12.get() + "' "
    updateCommand = updateCommand + "where email = '" + getKeyForCurrentRow() + "'"

    print(updateCommand)

    conn = cx_Oracle.connect('emailer/ilik2fly@TIMHELTON')
    cursor = conn.cursor()
    try:
        cursor.execute(updateCommand)
        messagebox.showinfo("Update Status", "One Row Updated")
        currentScreen.clearAll()
    except cx_Oracle.DatabaseError as exception:
        error, = exception.args
        messagebox.showinfo("Update Status", "Can't update record. " + error.message)

    cursor.close()
    conn.commit()
    conn.close()

    clearAll(top)
    currentScreen.eraseScreen()

def clearAll(top):
    global queryScreen
    currScreen = getCurrentScreen(queryScreen)
    currScreen.clearAll()
    if currScreen != queryScreen:
        queryScreen = PersonQueryScreen(top)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
