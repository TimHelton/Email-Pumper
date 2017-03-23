import emailerPersonInserter
import emailerPersonDeleter
import emailerPersonUpdater
import emailerMessageInserter
import emailerMessageDeleter
import emailerMessageUpdater
from emailerPersonInsUpdScreen import *

top = Tk()
top.title("Email Pumper")

PersonInsertCalledFlag = FALSE
PersonDeleteCalledFlag = FALSE
PersonUpdateCalledFlag = FALSE
MessageInsertCalledFlag = FALSE
MessageDeleteCalledFlag = FALSE
MessageUpdateCalledFlag = FALSE

def doMenu():
    menu_bar = Menu(top)

    fileMenu = Menu(menu_bar, tearoff=0)
    fileMenu.add_command(label="Quit", command=top.quit)
    menu_bar.add_cascade(label="File", menu=fileMenu)

    dbMenu = Menu(menu_bar, tearoff=0)
    dbMenu.add_command(label="Insert", command=lambda: prepPersonInsertScreen())
    dbMenu.add_command(label="Update", command=lambda: prepPersonUpdateScreen())
    dbMenu.add_command(label="Delete", command=lambda: prepPersonDeleteScreen())
    menu_bar.add_cascade(label="Contacts", menu=dbMenu)

    emailMenu = Menu(menu_bar, tearoff=0)
    emailMenu.add_command(label="Compose", command=lambda: prepMessageInsertScreen())
    emailMenu.add_command(label="Update", command=lambda: prepMessageUpdateScreen())
    emailMenu.add_command(label="Delete", command=lambda: prepMessageDeleteScreen())
    menu_bar.add_cascade(label="Email", menu=emailMenu)

    top.config(menu=menu_bar)

def eraseScreen():
    global PersonInsertCalledFlag, PersonDeleteCalledFlag, PersonUpdateCalledFlag
    global MessageInsertCalledFlag, MessageDeleteCalledFlag, MessageUpdateCalledFlag

    if PersonInsertCalledFlag:
        emailerPersonInserter.eraseScreen()
        PersonInsertCalledFlag = FALSE
    if PersonDeleteCalledFlag:
        emailerPersonDeleter.eraseScreen()
        PersonDeleteCalledFlag = FALSE
    if PersonUpdateCalledFlag:
        emailerPersonUpdater.eraseScreen()
        PersonUpdateCalledFlag = FALSE
    if MessageInsertCalledFlag:
        emailerMessageInserter.eraseScreen()
        MessageInsertCalledFlag = FALSE
    if MessageDeleteCalledFlag:
        emailerMessageDeleter.eraseScreen()
        MessageDeleteCalledFlag = FALSE
    if MessageUpdateCalledFlag:
        emailerMessageUpdater.eraseScreen()
        MessageUpdateCalledFlag = FALSE

def prepPersonInsertScreen():
    global PersonInsertCalledFlag
    eraseScreen()
    emailerPersonInserter.insert(top)
    PersonInsertCalledFlag = TRUE

def prepPersonUpdateScreen():
    global PersonUpdateCalledFlag
    eraseScreen()
    emailerPersonUpdater.queryForUpdate(top)
    PersonUpdateCalledFlag = TRUE

def prepPersonDeleteScreen():
    global PersonDeleteCalledFlag
    eraseScreen()
    emailerPersonDeleter.delete(top)
    PersonDeleteCalledFlag = TRUE

def prepMessageInsertScreen():
    global MessageInsertCalledFlag
    eraseScreen()
    emailerMessageInserter.insert(top)
    MessageInsertCalledFlag = TRUE

def prepMessageUpdateScreen():
    global MessageUpdateCalledFlag
    eraseScreen()
    emailerMessageUpdater.queryForUpdate(top)
    MessageUpdateCalledFlag = TRUE

def prepMessageDeleteScreen():
    global MessageDeleteCalledFlag
    eraseScreen()
    emailerMessageDeleter.delete(top)
    MessageDeleteCalledFlag = TRUE

doMenu()

mainloop()
