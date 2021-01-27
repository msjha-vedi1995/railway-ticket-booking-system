from tkinter import *

t=Tk()
t.geometry("300x100")

def display():
    print("Username is:"+ue.get()+"Password is:"+pe.get())

t.title("Railway reservation system")
w=Label(t,text="Welcome")
u=Label(t,text="Username")
p=Label(t,text="password")

ue=Entry(t)
pe=Entry(t,show='*')

q=Button(t,text="Quit",command=t.quit)
d = Button(t, text="Display", command=display)


w.grid(row=0,column=3)
u.grid(row=1,column=2)
p.grid(row=2, column=2)

ue.grid(columnspan=5,row=1,column=5)
pe.grid(columnspan=5,row=2,column=5)

q.grid(row=3,column=2)
d.grid(columnspan=2,row=3,column=4)

t.mainloop()