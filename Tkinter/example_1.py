# Create the first example
# Functionalities:
# 1.create windows, create label widget

from os import path
import os
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox,ttk
from tkinter.ttk import Combobox,Radiobutton
from tkinter.ttk import Checkbutton,Progressbar

window = Tk()
window.title("Example one")
window.geometry('900x800')

lbl = Label(window,text='Label 1',padx=50,pady=10,bg='red')
# without calling the grid function for label, it won't show up
lbl.grid(column=0,row=0)

# create textbox using Tkinter Entry class
txt = Entry(window,width=10)
txt.grid(column=1,row=0)

# add a area to show the botton clicked event
show1= Label(window,text='show area two')
# without calling the grid function for label, it won't show up
show1.grid(column=2,row=0)
# add a function to handle button click event
def clicked():
    show1.configure(text='The input is:' + txt.get())
# add a button,and change backgroud and foreground
btn = Button(window,text='Click Me',bg='orange',fg='red',command=clicked)
btn.grid(column=3,row=0)

# add a area to show the combobox selected event
show2= Label(window,text='Show Area',bg='green',fg='red')
show2.grid(column=0,row=1)
# add a combobox widget
combo = Combobox(window)
combo['values'] = (1,2,'name',4,5,'Text')
combo.current(2) # set the selected item
combo.grid(column=1,row=1)
# show the selected results
show2.configure(text='The select is:' +combo.get())

# add a checkbotton widget

# set check state,method one
# chk_state = IntVar()
# chk_state.set(0) # uncheck
# chk_state.set(1) # check

# set check state,method 2
chk_state = BooleanVar()
chk_state.set(True) # set check state
chk = Checkbutton(window,text='Choose',var=chk_state)
chk.grid(column=0,row=3)

# add a area to show the combobox selected event
show3= Label(window,text='Show Area',bg='white',fg='red')
show3.grid(column=3,row=4)
# handle event function
def rad1_event():
    show3.configure(text='first')
def rad2_event():
    show3.configure(text='second')
def rad3_event():
    show3.configure(text='third')
# add radio buttons widgets
rad1 = Radiobutton(window,text='first',value=1,command=rad1_event)
rad2 = Radiobutton(window,text='second',value=2,command=rad2_event)
rad3 = Radiobutton(window,text='third',value=3,command=rad3_event)
rad1.grid(column=0,row=4)
rad2.grid(column=1,row=4)
rad3.grid(column=2,row=4)

# add a ScrolledText widget
s_txt = scrolledtext.ScrolledText(window,width=40,height=10)
s_txt.grid(column=0,row=5)
s_txt.insert(INSERT,'you text goes here')

# add a messagebox
# there are also have messagebox.askquestion,messagebox.askyesno,
# messagebox.askyesnocancel,messagebox.okcancel,messagebox.askretrycancel
def show_info():
    messagebox.showinfo('Message title','Message info content')
btn = Button(window,text='showinfo',bg='orange',fg='red',command=show_info)
btn.grid(column=1,row=6)

def show_warning():
    messagebox.showwarning('Message title','Message warning content')
btn = Button(window,text='showwarning',bg='orange',fg='red',command=show_warning)
btn.grid(column=2,row=6)

def show_error():
    messagebox.showerror('Message title','Message error content')
btn = Button(window,text='showerror',bg='orange',fg='red',command=show_error)
btn.grid(column=3,row=6)

# add a SpinBox,and set default value
var = IntVar()
var.set(9)
spin = Spinbox(window,from_=0,to=20,width=5,textvariable=var)
spin.grid(column=0,row=7)

# add another SpinBox
spin = Spinbox(window,values=(2,5,16),width=10)
spin.grid(column=1,row=7)

# add a Progressbar widget
style = ttk.Style()
style.theme_use('default')
style.configure('black.Horizontal.TProgressbar',background='blue')
bar = Progressbar(window,length=200,style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0,row=8)

# add filedialog
def get_file():
    #print(os.getcwd()) # the current path
    file_ = filedialog.askopenfilename(initialdir=os.getcwd(),\
            filetypes=(('Text files','*.txt'),('Python file','*.py'),\
            ('all files','*.*')))
    print('the file is:' + file_)

btn = Button(window,text='get file',bg='orange',fg='red',command=get_file)
btn.grid(column=0,row=9)

# add menu
menu = Menu(window)
# diable the dashed line, which will show the menu items in a small separate windows
#new_item = Menu(menu,tearoff=0)
def menu_event():
    messagebox.showinfo('Message title','Message info content')

new_item = Menu(menu)
new_item.add_command(label='has an event',command=menu_event)
new_item.add_command(label='NEW_2')
new_item.add_separator()
new_item.add_command(label='NEW_3')
menu.add_cascade(label='File',menu=new_item)
window.configure(menu=menu)

window.mainloop()
