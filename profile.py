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

        self.Button1 = tk.Button(self.Frame1,command=lambda: self.show_frame("Newsfeed"))
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

        self.Button2 = tk.Button(self.Frame1,command=lambda: self.show_frame("search"))
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

        self.Button3 = tk.Button(self.Frame1,command=lambda: self.show_frame("uploadz"))
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

        self.Button4 = tk.Button(self.Frame1,command=lambda: self.show_frame("heart"))
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

        self.Button5 = tk.Button(self.Frame1,command=lambda: self.show_frame("profileinfo"))
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

        self.frames = {}
        for F in (Newsfeed,search,uploadz,heart,profileinfo):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            #frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("profileinfo")

    def show_frame(self, page_name):
        #swap btw the frames
        frame = self.frames[page_name]
                       
        frame.tkraise()

class Newsfeed(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        font9 = "-family {Segoe UI} -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        #self.configure(relief='groove')
        #self.configure(borderwidth="2")
        #self.configure(relief="groove")
        #self.configure(background="#d9d9d9")
        #self.configure(highlightbackground="#d9d9d9")
        #self.configure(highlightcolor="black")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.0, rely=0.0, height=121, width=450)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#feb4c2")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''insta top stroy''')
        global _img_s         
        _img_s = ImageTk.PhotoImage(Image.open('storyimg.png').resize((450,130),Image.ANTIALIAS))
        self.Label1.configure(image=_img_s)

         #post for scroll
        self.Frame_s = tk.Frame(self) #add scroll to scr_can
        self.Frame_s.place(relx=0.0, rely=0.22, relheight=0.78, relwidth=1.0)
        self.Frame_s.configure(relief='groove')
        #self.scrl_can.configure(borderwidth="2")
        self.Frame_s.configure(relief="groove")
        self.Frame_s.configure(background="#d9d9d9")

        self.scrl_can = tk.Canvas(self.Frame_s)# combine this to scroll
        self.scrl_can.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.scrl_can.configure(relief="groove")
        self.scrl_can.configure(background="#d9d9d9")

        
        self.scrollbar=tk.Scrollbar(self.Frame_s,orient="vertical",command=self.scrl_can.yview)
        self.scrl_can.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")

        self.Frame_1 = tk.Frame(self.scrl_can)# combine this to scrol
        self.Frame_1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame_1.configure(relief="groove")
        self.Frame_1.configure(background="#d9d9d9")
        self.scrl_can.create_window((0,0),window=self.Frame_1,anchor='nw')
        self.Frame_1.bind("<Configure>",lambda event: self.scrl_can.configure(scrollregion=self.scrl_can.bbox("all")))

        global _img         
        _img = ImageTk.PhotoImage(Image.open('storyimg.png').resize((400,300),Image.ANTIALIAS))
        
        for i in range(0,5):
            #f = tk.Frame(self.Frame_1, height = 100, width = 100,bg="yellow")
            #f.pack_propagate(0) 
            #f.place(x = 0, y = i+100)
            tk.Button(self.Frame_1,text=None,font=font9,compound="right",image=_img,background="#eeeeee",borderwidth="0").grid(row=i,column=0,padx=10, pady=10)
            #tk.Label(self.Frame_1,text="Images",font=font9,image=_img,compound="right").grid(row=i,column=0)
            #tk.Label(self.Frame_1,image=img,bg="blue").grid(row=i+1,column=0)
        
    
   

class search(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        font10 = "-family Arial -size 11 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.022, rely=0.018,height=40, relwidth=0.787)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button_s = tk.Button(self,command="")
        self.Button_s.place(relx=0.822, rely=0.018, height=34, width=67)
        self.Button_s.configure(activebackground="#ececec")
        self.Button_s.configure(activeforeground="#000000")
        self.Button_s.configure(background="#eeeeee")
        self.Button_s.configure(borderwidth="0")
        self.Button_s.configure(disabledforeground="#a3a3a3")
        self.Button_s.configure(font=font10)
        self.Button_s.configure(foreground="#000000")
        self.Button_s.configure(highlightbackground="#d9d9d9")
        self.Button_s.configure(highlightcolor="black")
        self.Button_s.configure(pady="0")
        self.Button_s.configure(text='''Search''')

        self.Frame_s = tk.Frame(self) #add scroll to scr_lcan
        self.Frame_s.place(relx=0.022, rely=0.11, relheight=0.868, relwidth=0.962)

        self.Canvas3 = tk.Canvas(self.Frame_s)
        self.Canvas3.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas3.configure(background="#eeeeee")
        self.Canvas3.configure(borderwidth="2")
        self.Canvas3.configure(insertbackground="black")
        self.Canvas3.configure(relief="ridge")
        self.Canvas3.configure(selectbackground="#c4c4c4")
        self.Canvas3.configure(selectforeground="black")

        self.scrollbar=tk.Scrollbar(self.Frame_s,orient="vertical",command=self.Canvas3.yview)
        self.Canvas3.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")

        self.Frame_1 = tk.Frame(self.Canvas3)# combine this to scrol
        self.Frame_1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame_1.configure(relief="groove")
        self.Frame_1.configure(background="#d9d9d9")
        self.Canvas3.create_window((0,0),window=self.Frame_1,anchor='nw')
        self.Frame_1.bind("<Configure>",lambda event: self.Canvas3.configure(scrollregion=self.Canvas3.bbox("all")))

        global _img_se
        _img_se =[]
        if _img_se == []:
            _img_se = ImageTk.PhotoImage(Image.open('nopost.jpg').resize((400,400),Image.ANTIALIAS))
            tk.Button(self.Frame_1,image=_img_se,background="#eeeeee",
                              borderwidth="0").grid(row=0,column=0,padx=10, pady=10)
        else:
            global imgcr
            imgcr=[]
            j=l=i=0
            #print("1",_img)            
            for img in _img_se:
                #print("2",img)resize((110,120),Image.ANTIALIAS)
                imgcr.append(ImageTk.PhotoImage(Image.open("storyimg.png").resize((110,120),Image.ANTIALIAS)))
                bt = tk.Button(self.Frame_1,image=imgcr[l],background="#eeeeee",
                        borderwidth="0")
                bt.configure(command="")
                bt.grid(row=j,column=i,padx=10, pady=10)
                l+=1
                if(i<2):
                    i+=1
                else:
                    i=0
                    j+=1  
        

class uploadz(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
       
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.configure(background="blue")


class heart(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.configure(background="yellow")


class profileinfo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        font9 = "-family {Segoe UI} -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.044, rely=0.11, height=90, width=125)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#eeeeee")
        
        self.Button6.configure(borderwidth="0")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Dp''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.022, rely=0.018, height=31, width=134)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#eeeeee")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 9 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''USERNAME''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.4, rely=0.202, height=21, width=41)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#eeeeee")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Post''')

        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.044, rely=0.28, height=30, width=152)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#eeeeee")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Arial Black} -size 9 -weight bold")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''FName''')

        self.Text1 = tk.Text(self) #text area for bio
        self.Text1.place(relx=0.044, rely=0.404, relheight=0.154, relwidth=0.431)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Label7 = tk.Label(self)
        self.Label7.place(relx=0.4, rely=0.147, height=21, width=48)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#eeeeee")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''postNO''')

        self.Button7 = tk.Button(self)
        self.Button7.place(relx=0.578, rely=0.147, height=20, width=70)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#eeeeee")
        self.Button7.configure(borderwidth="0")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font9)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''FollowerNO''')

        self.Button8 = tk.Button(self)
        self.Button8.place(relx=0.8, rely=0.147, height=21, width=67)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#eeeeee")
        self.Button8.configure(borderwidth="0")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font9)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''FollwngNO''')


        self.Label3_1 = tk.Label(self)
        self.Label3_1.place(relx=0.578, rely=0.202, height=21, width=71)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#eeeeee")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Arial} -size 12")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Follower''')

        self.Label3_2 = tk.Label(self)
        self.Label3_2.place(relx=0.8, rely=0.202, height=21, width=64)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#eeeeee")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Arial} -size 12")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Following''')

        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.044, rely=0.661, height=41, width=404)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#eeeeee")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''image of feeds''')

        self.Button9 = tk.Button(self)
        self.Button9.place(relx=0.044, rely=0.587, height=34, width=387)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#eeeeee")
        self.Button9.configure(borderwidth="0")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font=font9)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Edit Profile''')

        self.Frame_s = tk.Frame(self) #add scroll to scr_lcan
        self.Frame_s.place(relx=0.022, rely=0.752, relheight=0.226, relwidth=0.962)

        self.Canvas1 = tk.Canvas(self.Frame_s)
        self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Canvas1.configure(background="#eeeeee")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.scrollbar=tk.Scrollbar(self.Frame_s,orient="vertical",command=self.Canvas1.yview)
        self.Canvas1.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")

        self.Frame_1 = tk.Frame(self.Canvas1)# combine this to scrol
        self.Frame_1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame_1.configure(relief="groove")
        self.Frame_1.configure(background="#d9d9d9")
        self.Canvas1.create_window((0,0),window=self.Frame_1,anchor='nw')
        self.Frame_1.bind("<Configure>",lambda event: self.Canvas1.configure(scrollregion=self.Canvas1.bbox("all")))

        ## image loop

        global _img         
        _img = ImageTk.PhotoImage(Image.open('storyimg.png').resize((110,100),Image.ANTIALIAS))
        
        for i in range(0,5):
           
            tk.Button(self.Frame_1,text=None,font=font9,compound="right",image=_img,background="#eeeeee",borderwidth="0").grid(row=i,column=0,padx=10, pady=10)
           


if __name__ == '__main__':
    start_gui()
