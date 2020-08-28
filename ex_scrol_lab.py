from tkinter import *

def data():
    for i in range(50):
       Label(frame,text=i).grid(row=i,column=0)
       Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame,text="..........").grid(row=i,column=2)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root=Tk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")

canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()
#f1=Frame(frame,bg="red",width=50,height=40)
#f1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
root.mainloop()
'''

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)
    print(event)

frame = Frame(root, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)

File = "1.png"
img = ImageTk.PhotoImage(Image.open(File))
canvas.create_image(0,0,image=img, anchor="nw")

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)
frame.bind("<Configure>",lambda event: canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200))
#frame.bind("<Configure>", lambda event, canvas=canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200))
frame.pack()
root.mainloop()
'''
