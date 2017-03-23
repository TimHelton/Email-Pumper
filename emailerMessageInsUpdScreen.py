from tkinter import *
from tkinter import messagebox

class MessageInsUpdScreen:

    def __init__(self, top):

        vcmd1 = top.register(self.vCoreOnly)
        vcmd2 = top.register(self.vSubject)

        self.l1 = Label(top, text="Core Only? (Y/N):", width=15, anchor=E, justify=RIGHT)
        self.l1.grid(row=0, column=0, padx=5, pady=5)

        self.l2 = Label(top, text="Subject:", width=15, anchor=E, justify=RIGHT)
        self.l2.grid(row=1, column=0, padx=5, pady=5)

        self.l3 = Label(top, text="Message:", width=15, anchor=E, justify=RIGHT)
        self.l3.grid(row=2, column=0, padx=5, pady=5)

        self.l4 = Label(top, text="Attachment:", width=15, anchor=E, justify=RIGHT)
        self.l4.grid(row=28, column=0, padx=5, pady=5)

        self.e1 = Entry(top, width=2, bd=3, validate="focusout", vcmd=vcmd1)                        # Core only
        self.e1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        self.e1.insert(0, 'Y')

        self.e2 = Entry(top, width=100, bd=3, validate="focusout", vcmd=vcmd2)                      # Subject
        self.e2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        self.e3 = Text(top, width=75, height=25, bd=3, wrap=WORD)                                   # Message
        self.e3.grid(row=2, column=1, sticky=W, padx=5, pady=5, rowspan=25)

        self.e4 = Entry(top, width=100, bd=3, state=DISABLED)                                       # Attachment
        self.e4.grid(row=28, column=1, sticky=W, padx=5, pady=5)

    def eraseScreen(self):
        self.l1.grid_remove()
        self.l2.grid_remove()
        self.l3.grid_remove()
        self.l4.grid_remove()
        self.e1.grid_remove()
        self.e2.grid_remove()
        self.e3.grid_remove()
        self.e4.grid_remove()

    def clearAll(self):
        self.e2.delete(0, END)
        self.e3.delete(0.0, END)
        self.e4.config(state=NORMAL)
        self.e4.delete(0, END)
        self.e4.config(state=DISABLED)

    def vCoreOnly(self):
        string = self.e1.get()
        string = string.upper()
        if (string == "Y" or string == "N"):
            self.e1.delete(0, END)
            self.e1.insert(0, string)       # Force to uppercase
            return TRUE
        else:
            self.e1.delete(0, END)
            messagebox.showinfo("Core only entry box", "Please enter 'Y' or 'N'")
            return FALSE

    def vSubject(self):
        string = self.e2.get()
        if (len(string) > 255):
            self.e2.delete(0, END)
            messagebox.showinfo("Subject entry box", "Please limit subject to a maximum of 255 characters")
            return FALSE
        else:
            return TRUE