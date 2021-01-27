from tkinter import *
import tkinter.messagebox

def registerNew():
    pass1 = password1Entry.get()
    pass2 = password2Entry.get()
    if pass1 != pass2:
        print("Warning!", "Passwords Do Not Match")
    else:
        print("password matched")
    return

'''def login():
    l.tkraise()
    Label(l, text='this is the login page').pack()'''

root=Tk()


root.title('Railway Reservation System')

r=Frame(root)
l=Frame(root)
s=Frame(root)
b=Frame(root)

for frame in (r, l, s, b):
    frame.grid(row=0, column=0)



Label(r, text="New User Registration", font=("Times New Roman", 18)).grid(row=0, column=0, columnspan=4,sticky=E + W)
Label(r, text="Full Name").grid(row=1, column=0, sticky=W)
Label(r, text="Age").grid(row=2, column=0, sticky=W)
Label(r, text="Sex").grid(row=3, column=0, sticky=W)
Label(r, text="Contact No.").grid(row=4, column=0, sticky=W)
Label(r, text="Email Address").grid(row=5, column=0, sticky=W)
Label(r, text="Username").grid(row=6, column=0, sticky=W)
Label(r, text="Password").grid(row=7, column=0, sticky=W)
Label(r, text="Confirm Password").grid(row=8, column=0, sticky=W)

nameEntry = Entry(r, width=30).grid(row=1, column=1)
ageEntry = Entry(r, width=30).grid(row=2, column=1)
sexEntry = Entry(r, width=30).grid(row=3, column=1)
noEntry = Entry(r, width=30).grid(row=4, column=1)
emailEntry = Entry(r, width=30).grid(row=5, column=1)
userEntry = Entry(r, width=30).grid(row=6, column=1)
password1Entry = Entry(r, width=30).grid(row=7, column=1)
password2Entry = Entry(r, width=30).grid(row=8, column=1)


RegisterButton = Button(r, text="Create", width=15, command=registerNew).grid(row=9, column=1)

r.tkraise()


root.mainloop()
