from tkinter import *

root= Tk()
root.title("dropdownmenu")
root.geometry("400x400")

gender=StringVar()
gender.set("Gender")

drop = OptionMenu(root, gender, "M","F")
drop.grid(row=0,column=0)

destinationEntry = OptionMenu(s,)
destinationEntry.grid(row=1, column=4)

root.mainloop( )