import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
import profile
def start_gui():
    
    global root
    root = tk.Tk()
    toplevel (root)
    
    root.mainloop()

class toplevel:
    def __init__(self, top=None):
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font21 = "-family {Kristen ITC} -size 25 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"
        font24 = "-family Arial -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        
        font10 = "-family Arial -size 11 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family {Arial Black} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("450x600+475+42")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Instagram")
        top.configure(background="gray80")
        top.configure(highlightbackground="red2")

        self.container = tk.Frame(top)
        self.container.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.Lframe = tk.Frame(self.container)
        self.Lframe.place(relx=0.022, rely=0.017, relheight=0.967
                , relwidth=0.956)
        self.Lframe.configure(relief='groove')
        self.Lframe.configure(borderwidth="1")
        self.Lframe.configure(relief="groove")
        self.Lframe.configure(background="#ffffff")
        self.Lframe.configure(highlightbackground="#b9b9b9")
        self.Lframe.configure(highlightcolor="#bebebe")

        self.Label1 = tk.Label(self.Lframe)
        self.Label1.place(relx=0.14, rely=0.121, height=101, width=304)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font21)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Mini Instagram''')

        self.Label_u = tk.Label(self.Lframe)
        self.Label_u.place(relx=0.116, rely=0.338, height=22, relwidth=0.180)
        self.Label_u.configure(background="#f8f6f6")
        self.Label_u.configure(disabledforeground="#a3a3a3")
        self.Label_u.configure(font=font10)
        self.Label_u.configure(foreground="#888787")
        self.Label_u.configure(text="username")

        self.username = tk.StringVar()
        self.Entry1 = tk.Entry(self.Lframe)
        self.Entry1.place(relx=0.116, rely=0.379,height=40, relwidth=0.753)
        self.Entry1.configure(background="#e8e8e8")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.insert(0,"Username")
        self.Entry1.configure(textvariable=self.username)
        self.Entry1.bind("<FocusIn>",lambda event: self.Entry1.delete(0, tk.END))
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        
        self.Label_p = tk.Label(self.Lframe)
        self.Label_p.place(relx=0.116, rely=0.485, height=22, relwidth=0.180)
        self.Label_p.configure(background="#f8f6f6")
        self.Label_p.configure(disabledforeground="#a3a3a3")
        self.Label_p.configure(font=font10)
        self.Label_p.configure(foreground="#888787")
        self.Label_p.configure(text="password")

        self.password = tk.StringVar()
        self.Entry2 = tk.Entry(self.Lframe,show="*")
        self.Entry2.place(relx=0.116, rely=0.526,height=40, relwidth=0.753)
        self.Entry2.configure(background="#e8e8e8")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.insert(0,"Password")
        self.Entry2.configure(textvariable=self.password)
        self.Entry2.bind("<FocusIn>",lambda event: self.Entry2.delete(0, tk.END))
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Lframe,command=self.loginval)
        self.Button1.place(relx=0.14, rely=0.662, height=34, width=307)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#d9d9d9")
        self.Button1.configure(background="#1d95f8")
        self.Button1.configure(cursor="arrow")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font24)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(pady="0")
        self.Button1.configure(state='active')
        self.Button1.configure(text='Log In')

        self.TSeparator1 = ttk.Separator(self.Lframe)
        self.TSeparator1.place(relx=0.2, rely=0.783, relwidth=0.556)

        self.Label2 = tk.Label(self.Lframe)
        self.Label2.place(relx=0.222, rely=0.839, height=41, width=174)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Don't have an account?''')

        self.Button2 = tk.Button(self.Lframe,command=self.signup)
        self.Button2.place(relx=0.584, rely=0.847, height=31, width=72)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font12)
        self.Button2.configure(foreground="#00bfb6")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(highlightthickness="0")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='Sign up')
    
    def loginval(self):
        global user_id,passz
        user_id = self.username.get()
        passz = self.password.get()
        
        print(user_id,passz)

    def signup(self):
        self.Lframe.destroy()
        font10 = "-family Arial -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        
        font12 = "-family {Arial Black} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family Arial -size 9 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        self.Frame1 = tk.Frame(self.container)
        self.Frame1.place(relx=0.022, rely=0.017, relheight=0.975
                , relwidth=0.967)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.092, rely=0.068, height=41, width=134)
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#7d1206")
        self.Label1.configure(text='''Full Name''')

        self.fname = tk.StringVar()
        self.Entry1 = tk.Entry(self.Frame1,textvariable=self.fname)
        self.Entry1.place(relx=0.46, rely=0.068,height=30, relwidth=0.446)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.092, rely=0.171, height=31, width=139)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="fant10")
        self.Label2.configure(foreground="#7d1206")
        self.Label2.configure(text='''Username''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.115, rely=0.274, height=31, width=116)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#7d1206")
        self.Label3.configure(text='''Password''')

        
        self.Entry2 = tk.Entry(self.Frame1,textvariable=self.username)
        self.Entry2.place(relx=0.46, rely=0.171,height=30, relwidth=0.446)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry3 = tk.Entry(self.Frame1,textvariable=self.password)
        self.Entry3.place(relx=0.46, rely=0.274,height=30, relwidth=0.446)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(show="*")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.092, rely=0.393, height=31, width=116)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Arial} -size 13")
        self.Label4.configure(foreground="#7d1206")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Bio''')

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.46, rely=0.376, relheight=0.144, relwidth=0.446)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word") #.get("1.0",END)


        
        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.092, rely=0.581, height=31, width=116)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Arial} -size 13")
        self.Label5.configure(foreground="#7d1206")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Profile Pic''')

        self.dp_url=None
        self.Button2 = tk.Button(self.Frame1,command=self.upload_dp)
        self.Button2.place(relx=0.46, rely=0.581, height=44, width=194)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Upload''')


        self.Button1 = tk.Button(self.Frame1,command=self.signup_action)
        self.Button1.place(relx=0.207, rely=0.718, height=34, width=237)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(pady="0")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#00bfb6")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text='''Sign Up''')
        

    def upload_dp(self):
        self.dp_url = filedialog.askopenfilename(filetypes=[('Images1', '*.jpg'),('Images2', '*.png')])
        self.Button2.config(text=self.dp_url[-20:])
        

    def signup_action(self):
        global user_id,passz,fname,dp_url,bio

        user_id = self.username.get()
        passz = self.password.get()
        fname = self.fname.get()
        if(self.dp_url is not None):
            dp_url = self.dp_url
        bio = self.Text1.get("1.0",tk.END)
        dp_url=""
        print(user_id,passz,fname,dp_url,bio)

        
        
        
if __name__ == '__main__':
    start_gui()

