from tkinter import *

class MessageQueryScreen:

    def __init__(self, top):
        self.l1 = Label(top, text="Core Only? (Y/N):", width=15, anchor=E, justify=RIGHT)
        self.l1.grid(row=0, column=0, padx=5, pady=5)

        self.l2 = Label(top, text="Subject:", width=15, anchor=E, justify=RIGHT)
        self.l2.grid(row=1, column=0, padx=5, pady=5)

        self.l3 = Label(top, text="Message:", width=15, anchor=E, justify=RIGHT)
        self.l3.grid(row=2, column=0, padx=5, pady=5)

        self.l4 = Label(top, text="Attachment:", width=15, anchor=E, justify=RIGHT)
        self.l4.grid(row=28, column=0, padx=5, pady=5)

        self.e1 = Entry(top, width=2, bd=3, validate="focusout")  # Core only
        self.e1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        self.e2 = Entry(top, width=100, bd=3, validate="focusout")  # Subject
        self.e2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        self.e3 = Text(top, width=75, height=25, bd=3, wrap=WORD)  # Message
        self.e3.grid(row=2, column=1, sticky=W, padx=5, pady=5, rowspan=25)

        self.e4 = Entry(top, width=100, bd=3)  # Attachment
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
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0.0, END)
        self.e4.delete(0, END)
