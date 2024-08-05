import tkinter  ## import tkinter
from tkinter import *

root = Tk() ## create root window 
## root window and dimension 
root.title("Enter User and Password")
root.geometry('550x500')

##adding entry field 
lbl1= Label(root, text = "Username", fg = 'black', bg = 'grey')
lbl2= Label(root, text = "Password", fg = 'black', bg = 'grey')

lbl1.grid()
lbl2.grid()

# adding Entry Field
e1 = Entry(root)
e2 = Entry(root,show="*")

e1.grid(column =1, row =0)
e2.grid(column =1, row =1)

# function to display user text when
# button is clicked
def clicked():
 
    res = "You wrote" + " "+ e2.get()
    lbl2.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Show" ,
             fg = "red", command=clicked)

btn.grid(column=2, row=1)
 

root.mainloop()  ## Execute 