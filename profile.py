import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import login

def start_gui():
    
    root = tk.Tk()
    Toplevel1 (root)
    root.mainloop()

class Toplevel1:
    def __init__(self, top=None):
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("455x595+392+35")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Profile")
        top.configure(background="#b6b6b6")
        top.configure(highlightbackground="#e3fdf4")
        top.configure(highlightcolor="#46edfb")
        top.configure(highlightthickness="1")
        
        # top.configure(background="IndianRed2")#d9d9d9")
        # top.configure(highlightbackground="#d9d9d9")
        # top.configure(highlightcolor="black")
        
        self.Framet = tk.Frame(top)
        self.Framet.place(relx=0.011, rely=0.008, relheight=0.983, relwidth=0.978)
        #self.Framet.place(relx=0.022, rely=0.016, relheight=0.959, relwidth=0.957)
        self.Framet.configure(relief='groove')
        self.Framet.configure(borderwidth="2")
        self.Framet.configure(relief="groove")
        self.Framet.configure(background="#c3c3c3")
        #self.Framet.configure(highlightbackground="#ff4848")
        #self.Framet.configure(highlightcolor="#ff4848")
        #self.Framet.configure(highlightthickness="1")


        self.container = tk.Frame(self.Framet)
        self.container.place(relx=0.0, rely=0.0, relheight=0.908, relwidth=1.0)
        self.container.configure(borderwidth="2")
        self.container.configure(relief="groove")
        self.container.configure(background="#d9d9d9")
        self.container.configure(highlightbackground="#d9d9d9")
        self.container.configure(highlightcolor="black")
        
        
        self.Frame1 = tk.Frame(self.Framet)
        self.Frame1.place(relx=0.0, rely=0.906, relheight=0.108, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Button1 = tk.Button(self.Frame1,command="")
        self.Button1.place(relx=0.044, rely=0.154, height=34, width=44)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Home''')
        #photo_location = os.path.join(prog_location,"./home.png")
        global _img1         
        _img1 = ImageTk.PhotoImage(Image.open('home.png').resize((50,50),Image.ANTIALIAS))
        self.Button1.configure(image=_img1)
        #self.Button1.configure(image= ImageTk.PhotoImage(Image.open('home.png')))

        self.Button2 = tk.Button(self.Frame1,command="")
        self.Button2.place(relx=0.222, rely=0.154, height=37, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Search''')
        global _img2         
        _img2 = ImageTk.PhotoImage(Image.open('search.png').resize((40,35),Image.ANTIALIAS))
        self.Button2.configure(image=_img2)

        self.Button3 = tk.Button(self.Frame1,command="")
        self.Button3.place(relx=0.422, rely=0.154, height=34, width=47)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Upload''')
        global _img3         
        _img3 = ImageTk.PhotoImage(Image.open('upload.png').resize((50,50),Image.ANTIALIAS))
        self.Button3.configure(image=_img3)

        self.Button4 = tk.Button(self.Frame1,command="")
        self.Button4.place(relx=0.622, rely=0.154, height=34, width=47)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Hearts''')
        global _img4         
        _img4 = ImageTk.PhotoImage(Image.open('heart.png').resize((40,35),Image.ANTIALIAS))
        self.Button4.configure(image=_img4)

        self.Button5 = tk.Button(self.Frame1,command="")
        self.Button5.place(relx=0.822, rely=0.154, height=34, width=45)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Profile''')
        global _img5         
        _img5 = ImageTk.PhotoImage(Image.open('profile.png').resize((50,50),Image.ANTIALIAS))
        self.Button5.configure(image=_img5)


        

    
if __name__ == '__main__':
    start_gui()
