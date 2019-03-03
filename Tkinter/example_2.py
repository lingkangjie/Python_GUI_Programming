# the basic idea of layout managers in Tkinter
from tkinter import *

w1 = Tk()
w1.title('pack')
# width x height + x_offset + y_offset
w1.geometry('200x100+10+10') # set the windows size and location
Label(w1,text='a',bg='red').pack()
Label(w1,text='aaaa',bg='red').pack()
Label(w1,text='b',bg='red').pack()

w2 = Tk()
w2.title('pack')
w2.geometry('200x100+210+10') # set the windows size and location
Label(w2,text='a',bg='red').pack(fill=X)
Label(w2,text='aaaa',bg='red').pack(fill=X)
Label(w2,text='b',bg='red').pack(fill=X)

w3 = Tk()
w3.title('pack')
w3.geometry('200x100+410+10') # set the windows size and location
# add external padding,padding in x and y direction
Label(w3,text='a',bg='red').pack(fill=X,padx=5)
Label(w3,text='aaaa',bg='red').pack(fill=X,padx=10)
Label(w3,text='b',bg='red').pack(fill=X,padx=10,pady=20)

w4 = Tk()
w4.title('pack')
w4.geometry('200x100+610+10') # set the windows size and location
# add internal padding,padding in x and y direction
Label(w4,text='a',bg='red').pack(ipadx=5)
Label(w4,text='aaaa',bg='red').pack(ipadx=10)
Label(w4,text='b',bg='red').pack(ipadx=10,ipady=20)

#use Place geometry manager to explicitly set the position and
#size of a window, either in absolute terms, or relative to 
#another window
w5 = Tk()
w5.title('place')
w5.geometry('200x100+810+10') # set the windows size and location
# add internal padding,padding in x and y direction
Label(w5,text='a',bg='red').place(x=0,y=0,width=100,height=25)
Label(w5,text='aaaa',bg='red').place(x=0,y=30,width=50,height=25)
Label(w5,text='b',bg='red').place(x=10,y=60,width=200,height=25)

# grid method
w6 = Tk()
w6.title('place')
w6.geometry('200x150+1010+10') # set the windows size and location
colours = ['red','green','orange','white','yellow','blue']
r = 0
for c in colours:
    Label(w6,text=c,relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(w6,bg=c,relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r+1

mainloop()

