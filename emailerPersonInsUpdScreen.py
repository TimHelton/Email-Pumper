from tkinter import *
from tkinter import messagebox

class PersonInsUpdScreen():

    def __init__(self, top):

        vcmd0 = (top.register(self.vEmail))
        vcmd1 = (top.register(self.vLname))
        vcmd2 = (top.register(self.vFname))
        vcmd3 = (top.register(self.vAddress1))
        vcmd4 = (top.register(self.vAddress2))
        vcmd5 = (top.register(self.vCity))
        vcmd6 = (top.register(self.vState))
        vcmd7 = (top.register(self.vZip))
        vcmd8 = (top.register(self.vPhone1))
        vcmd9 = (top.register(self.vPhoneType1))
        vcmd10 = (top.register(self.vPhone2))
        vcmd11 = (top.register(self.vPhoneType2))
        vcmd12 = (top.register(self.vCore))

        self.l0 = Label(top, text="Email Address:", width=15, anchor=E, justify=RIGHT)
        self.l0.grid(row=0, column=0, padx=5, pady=5)

        self.l1 = Label(top, text="Last Name:", width=15, anchor=E, justify=RIGHT)
        self.l1.grid(row=1, column=0, padx=5, pady=5)

        self.l2 = Label(top, text="First Name:", width=15, anchor=E, justify=RIGHT)
        self.l2.grid(row=2, column=0, padx=5, pady=5)

        self.l3 = Label(top, text="Address Line 1:", width=15, anchor=E, justify=RIGHT)
        self.l3.grid(row=3, column=0, padx=5, pady=5)

        self.l4 = Label(top, text="Address Line 2:", width=15, anchor=E, justify=RIGHT)
        self.l4.grid(row=4, column=0, padx=5, pady=5)

        self.l5 = Label(top, text="City:", width=15, anchor=E, justify=RIGHT)
        self.l5.grid(row=5, column=0, padx=5, pady=5)

        self.l6 = Label(top, text="State:", width=15, anchor=E, justify=RIGHT)
        self.l6.grid(row=6, column=0, padx=5, pady=5)

        self.l7 = Label(top, text="Postal Code:", width=15, anchor=E, justify=RIGHT)
        self.l7.grid(row=7, column=0, padx=5, pady=5)

        self.l8 = Label(top, text="Phone 1:", width=15, anchor=E, justify=RIGHT)
        self.l8.grid(row=8, column=0, padx=5, pady=5)

        self.l9 = Label(top, text="Phone Type:", width=15, anchor=E, justify=RIGHT)
        self.l9.grid(row=9, column=0, padx=5, pady=5)

        self.l10 = Label(top, text="Phone 2:", width=15, anchor=E, justify=RIGHT)
        self.l10.grid(row=10, column=0, padx=5, pady=5)

        self.l11 = Label(top, text="Phone Type:", width=15, anchor=E, justify=RIGHT)
        self.l11.grid(row=11, column=0, padx=5, pady=5)

        self.l12 = Label(top, text="Core Y/N:", width=15, anchor=E, justify=RIGHT)
        self.l12.grid(row=12, column=0, padx=5, pady=5)

        self.e0 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd0)                         # Email
        self.e0.grid(row=0, column=1, padx=5, pady=5)

        self.e1 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd1)                         # Last Name
        self.e1.grid(row=1, column=1, padx=5, pady=5)

        self.e2 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd2)                         # First Name
        self.e2.grid(row=2, column=1, padx=5, pady=5)

        self.e3 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd3)                         # Address1
        self.e3.grid(row=3, column=1, padx=5, pady=5)

        self.e4 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd4)                         # Address2
        self.e4.grid(row=4, column=1, padx=5, pady=5)

        self.e5 = Entry(top, width=55, bd=3, validate="focusout", vcmd=vcmd5)                         # City
        self.e5.grid(row=5, column=1, padx=5, pady=5)

        self.e6 = Entry(top, width=3, bd=3, validate="focusout", vcmd=vcmd6)                          # State
        self.e6.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        self.e7 = Entry(top, width=12, bd=3, validate="focusout", vcmd=vcmd7)                         # Postal code
        self.e7.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        self.e8 = Entry(top, width=15, bd=3, validate="focusout", vcmd=vcmd8)                         # Telephone 1
        self.e8.grid(row=8, column=1, sticky=W, padx=5, pady=5)

        self.e9 = Entry(top, width=10, bd=3, validate="focusout", vcmd=vcmd9)                         # Telephone type
        self.e9.grid(row=9, column=1, sticky=W, padx=5, pady=5)

        self.e10 = Entry(top, width=15, bd=3, validate="focusout", vcmd=vcmd10)                       # Telephone 2
        self.e10.grid(row=10, column=1, sticky=W, padx=5, pady=5)

        self.e11 = Entry(top, width=10, bd=3, validate="focusout", vcmd=vcmd11)                       # Telephone type
        self.e11.grid(row=11, column=1, sticky=W, padx=5, pady=5)

        self.e12 = Entry(top, width=2, bd=3, validate="focusout", vcmd=vcmd12)                        # Core (Y/N)
        self.e12.grid(row=12, column=1, sticky=W, padx=5, pady=5)
        self.e12.insert(0, "N")

    def eraseScreen(self):
        self.l0.grid_remove()
        self.l1.grid_remove()
        self.l2.grid_remove()
        self.l3.grid_remove()
        self.l4.grid_remove()
        self.l5.grid_remove()
        self.l6.grid_remove()
        self.l7.grid_remove()
        self.l8.grid_remove()
        self.l9.grid_remove()
        self.l10.grid_remove()
        self.l11.grid_remove()
        self.l12.grid_remove()
        self.e0.grid_remove()
        self.e1.grid_remove()
        self.e2.grid_remove()
        self.e3.grid_remove()
        self.e4.grid_remove()
        self.e5.grid_remove()
        self.e6.grid_remove()
        self.e7.grid_remove()
        self.e8.grid_remove()
        self.e9.grid_remove()
        self.e10.grid_remove()
        self.e11.grid_remove()
        self.e12.grid_remove()

    def clearAll(self):
        self.e0.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)
        self.e10.delete(0, END)
        self.e11.delete(0, END)

    def vEmail(self):
        string = self.e0.get()
        if (len(string) > 45):
            self.e0.delete(0, END)
            messagebox.showinfo("Email entry box", "Use only forty-five characters for email")
            return FALSE
        elif (len(string) > 0 and string.count("@") != 1):
            self.e0.delete(0, END)
            messagebox.showinfo("Email entry box", "Invalid email address")
            return FALSE
        else:
            return TRUE

    def vLname(self):
        string = self.e1.get()
        if (len(string) > 45):
            self.e1.delete(0, END)
            messagebox.showinfo("Last name entry box", "Please limit name to a maximum of forty-five characters")
            return FALSE
        else:
            return TRUE

    def vFname(self):
        string = self.e2.get()
        if (len(string) > 45):
            self.e2.delete(0, END)
            messagebox.showinfo("First name entry box", "Please limit name to a maximum of forty-five characters")
            return FALSE
        else:
            return TRUE

    def vAddress1(self):
        string = self.e3.get()
        if (len(string) > 45):
            self.e3.delete(0, END)
            messagebox.showinfo("Address entry box", "Please limit address to a maximum of forty-five characters")
            return FALSE
        else:
            return TRUE

    def vAddress2(self):
        string = self.e4.get()
        if (len(string) > 45):
            self.e4.delete(0, END)
            messagebox.showinfo("Address entry box", "Please limit address to a maximum of forty-five characters")
            return FALSE
        else:
            return TRUE

    def vCity(self):
        string = self.e5.get()
        if (len(string) > 45):
            self.e5.delete(0, END)
            messagebox.showinfo("City entry box", "Please limit city to a maximum of forty-five characters")
            return FALSE
        else:
            return TRUE

    def vState(self):
        string = self.e6.get()
        if (len(string) == 2 or len(string) == 0):
            return TRUE
        else:
            self.e6.delete(0, END)
            messagebox.showinfo("State entry box", "Use only two character abbreviations for the state")
            return FALSE

    def vZip(self):
        string = self.e7.get()
        if (len(string) > 10):
            self.e7.delete(0, END)
            messagebox.showinfo("Postal code entry box", "Please limit postal code to a maximum of ten characters")
            return FALSE
        else:
            return TRUE

    def vPhone1(self):
        string = self.e8.get()
        if (len(string) > 15):
            self.e8.delete(0, END)
            messagebox.showinfo("Phone entry box", "Please limit phone to a maximum of fifteen characters")
            return FALSE
        else:
            return TRUE

    def vPhoneType1(self):
        string = self.e9.get()
        if (len(string) > 10):
            self.e9.delete(0, END)
            messagebox.showinfo("Phone type entry box", "Please limit phone type to a maximum of ten characters")
            return FALSE
        else:
            return TRUE

    def vPhone2(self):
        string = self.e10.get()
        if (len(string) > 15):
            self.e10.delete(0, END)
            messagebox.showinfo("Phone entry box", "Please limit phone to a maximum of fifteen characters")
            return FALSE
        else:
            return TRUE

    def vPhoneType2(self):
        string = self.e11.get()
        if (len(string) > 10):
            self.e11.delete(0, END)
            messagebox.showinfo("Phone type entry box", "Please limit phone type to a maximum of ten characters")
            return FALSE
        else:
            return TRUE

    def vCore(self):
        string = self.e12.get()
        string = string.upper()
        if string == "Y" or string == "N":
            self.e12.delete(0, END)
            self.e12.insert(0, string)  # Force to uppercase
            return TRUE
        else:
            self.e12.delete(0, END)
            messagebox.showinfo("Core entry box", "Please enter 'Y' or 'N'")
            return FALSE
