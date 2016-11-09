import time
from tkinter import *



_author_ = 'sdh'


root = Tk()
top=Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

mb= Menubutton ( top, text="Time Zone", relief=RAISED )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0)
mb["menu"] = mb.menu

gmtVar = IntVar()
cmtVar = IntVar()

mb.menu.add_checkbutton( label="GMT -5:00",
                         variable=gmtVar )
mb.menu.add_checkbutton( label="CMT -6:00",
                         variable=cmtVar )

mb.pack()
top.mainloop()



def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    #if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 miliseconds
    # to update the time display as needed
    # could use >200 ms, but display messes up
    clock.after(200, tick)

tick()



root.mainloop()
