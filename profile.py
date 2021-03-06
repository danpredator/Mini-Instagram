import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import login
import dbvalidate
from tkinter import filedialog
from tkinter import messagebox
import sys
import builtins
import random

def start_gui(user_id):
    
    global root,useridgol
    useridgol = user_id
    root = tk.Tk()
    Toplevel1 (root)
    root.mainloop()

class Toplevel1:
    def __init__(self, top=None):
        
        top.geometry("455x595+392+35")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Profile")
        top.configure(background="#b6b6b6")
        top.configure(highlightbackground="#e3fdf4")
        top.configure(highlightcolor="#46edfb")
        top.configure(highlightthickness="1")
        
        self.Framet = tk.Frame(top)
        self.Framet.place(relx=0.011, rely=0.008, relheight=0.983, relwidth=0.978)
        self.Framet.configure(relief='groove')
        self.Framet.configure(borderwidth="2")
        self.Framet.configure(relief="groove")
        self.Framet.configure(background="#c3c3c3")
        
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
        
        global _img1         
        _img1 = ImageTk.PhotoImage(Image.open('home.png').resize((50,50),Image.ANTIALIAS))
        self.Button1.configure(image=_img1)
        
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
            frame = F.__new__(F)
            self.frames[page_name] = frame
            

        self.show_frame("profileinfo")

    def show_frame(self, page_name):
        #swap btw the frames
        frame = self.frames[page_name]
        frame.__init__(parent=self.container, controller=self)
        
                       
        frame.tkraise()

class Newsfeed(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
                
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
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

        imgsurl = dbvalidate.newsfeed(useridgol)
        
        global _img         
        _img = imgsurl
        if _img == []:
            _img = ImageTk.PhotoImage(Image.open('nopost.jpg').resize((400,400),Image.ANTIALIAS))
            tk.Button(self.Frame_1,image=_img,background="#eeeeee",
                              borderwidth="0").grid(row=0,column=0,padx=10, pady=10)
        else:
            global imgcr
            imgcr=[]
            i=0
            
            for img in _img:
                
                imgcr.append(ImageTk.PhotoImage(Image.open(img[1]).resize((400,300),Image.ANTIALIAS)))
                bt = tk.Button(self.Frame_1,image=imgcr[i],background="#eeeeee",
                        borderwidth="0")
                bt.configure(command=lambda pic_id = img[0]: self.popup_dis(pic_id))
                bt.grid(row=i,column=0,padx=10, pady=10)
                i+=1
        
    def popup_dis(self,pic_id):
        win = tk.Toplevel()
        win.title("Img info")
        win.geometry("120x150")
        userid,likeNo,capt = dbvalidate.captlike(useridgol,pic_id)

        global like_i
        like_i=True
        tk.Label(win,foreground="#d11b60", text=str(userid[0])).grid(row=0, column=0,padx=10,pady=10)
        lik = tk.Label(win,foreground="#d11b60", text=str(likeNo[0])+" Likes")
        lik.grid(row=1, column=0,padx=10,pady=10)
        tk.Label(win,foreground="#d11b60", text=str(capt[0])).grid(row=2, column=0,padx=10,pady=10)
        tk.Button(win,foreground="#d11b60", text="Like", 
            command=lambda: self.liketoggle(lik,useridgol,pic_id)).grid(row=3, column=0)   

    def liketoggle(self,lik,useridgol,pic_id):
        global like_i
        if(like_i):
            lik.configure(text=str(dbvalidate.captlike(useridgol,pic_id,flag=True)[0])+" Likes")
            like_i = not like_i
        else:
            lik.configure(text=str(dbvalidate.captlike(useridgol,pic_id,flag=True)[0])+" Likes")
            like_i = not like_i
   

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

        self.Button_s = tk.Button(self,command=self.searchchk)
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

        imgsz = dbvalidate.getallpics()
        global _img_se
        random.shuffle(imgsz)
        _img_se =imgsz
        if _img_se == []:
            _img_se = ImageTk.PhotoImage(Image.open('nopost.jpg').resize((400,400),Image.ANTIALIAS))
            tk.Button(self.Frame_1,image=_img_se,background="#eeeeee",
                              borderwidth="0").grid(row=0,column=0,padx=10, pady=10)
        else:
            global imgcr
            imgcr=[]
            j=l=i=0
            
            for img in _img_se:
                
                imgcr.append(ImageTk.PhotoImage(Image.open(img[1]).resize((110,120),Image.ANTIALIAS)))
                bt = tk.Button(self.Frame_1,image=imgcr[l],background="#eeeeee",
                        borderwidth="0")
                bt.configure(command=lambda pic_id = img[0]: self.popup_dis(pic_id))
                bt.grid(row=j,column=i,padx=10, pady=10)
                l+=1
                if(i<2):
                    i+=1
                else:
                    i=0
                    j+=1   
                

    def popup_dis(self,pic_id):
        win = tk.Toplevel()
        win.title("Img info")
        win.geometry("120x150")
        userid,likeNo,capt = dbvalidate.captlike(useridgol,pic_id)

        global like_i
        like_i=True
        tk.Label(win,foreground="#d11b60", text=str(userid[0])).grid(row=0, column=0,padx=10,pady=10)
        lik = tk.Label(win,foreground="#d11b60", text=str(likeNo[0])+" Likes")
        lik.grid(row=1, column=0,padx=10,pady=10)
        tk.Label(win,foreground="#d11b60", text=str(capt[0])).grid(row=2, column=0,padx=10,pady=10)
        tk.Button(win,foreground="#d11b60", text="Like", 
            command=lambda: self.liketoggle(lik,useridgol,pic_id)).grid(row=3, column=0)   

    def liketoggle(self,lik,useridgol,pic_id):
        global like_i
        if(like_i):
            lik.configure(text=str(dbvalidate.captlike(useridgol,pic_id,flag=True)[0])+" Likes")
            like_i = not like_i
        else:
            lik.configure(text=str(dbvalidate.captlike(useridgol,pic_id,flag=True)[0])+" Likes")
            like_i = not like_i
    
    def searchchk(self):
        userz = self.Entry2.get() 
        if ( len(userz)!=0 and userz != useridgol):
            if(dbvalidate.searchck(userz)):
                
                record,folwerno,folwingno,imgsurl,postno = dbvalidate.profile(userz)
                
                self.Fra_sRes = tk.Frame(self)
                self.Fra_sRes.place(relx=0.011, rely=0.008, relheight=0.982
                                , relwidth=0.978)
                self.Fra_sRes.configure(relief='groove')
                self.Fra_sRes.configure(borderwidth="2")
                self.Fra_sRes.configure(relief="groove")
                self.Fra_sRes.configure(background="#d9d9d9")
                self.Fra_sRes.configure(highlightbackground="#d9d9d9")
                self.Fra_sRes.configure(highlightcolor="black")

                self.Label2 = tk.Label(self.Fra_sRes)
                self.Label2.place(relx=0.023, rely=0.018, height=31, width=104)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(background="#d9d9d9")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Arial} -size 9 -weight bold")
                self.Label2.configure(foreground="#000000")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(text=record[0]) #username

                self.Label3 = tk.Label(self.Fra_sRes)
                self.Label3.place(relx=0.409, rely=0.202, height=21, width=41)
                self.Label3.configure(activebackground="#f9f9f9")
                self.Label3.configure(activeforeground="black")
                self.Label3.configure(background="#d9d9d9")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font="-family {Arial} -size 12")
                self.Label3.configure(foreground="#000000")
                self.Label3.configure(highlightbackground="#d9d9d9")
                self.Label3.configure(highlightcolor="black")
                self.Label3.configure(text='''Post''')

                self.Label6 = tk.Label(self.Fra_sRes)
                self.Label6.place(relx=0.045, rely=0.33, height=23, width=112)
                self.Label6.configure(activebackground="#f9f9f9")
                self.Label6.configure(activeforeground="black")
                self.Label6.configure(background="#d9d9d9")
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(font="-family {Arial Black} -size 9 -weight bold")
                self.Label6.configure(foreground="#000000")
                self.Label6.configure(highlightbackground="#d9d9d9")
                self.Label6.configure(highlightcolor="black")
                self.Label6.configure(text=record[1]) #fullname

                self.Text1 = tk.Text(self.Fra_sRes)
                self.Text1.place(relx=0.045, rely=0.404, relheight=0.154, relwidth=0.441)                
                self.Text1.delete("1.0",tk.END)
                self.Text1.insert(tk.END,record[3])
                self.Text1.configure(state='disabled')

                self.Text1.configure(background="white")
                self.Text1.configure(font="TkTextFont")
                self.Text1.configure(foreground="black")
                self.Text1.configure(highlightbackground="#d9d9d9")
                self.Text1.configure(highlightcolor="black")
                self.Text1.configure(insertbackground="black")
                self.Text1.configure(selectbackground="#c4c4c4")
                self.Text1.configure(selectforeground="black")
                self.Text1.configure(wrap="word")

                self.Label7 = tk.Label(self.Fra_sRes)
                self.Label7.place(relx=0.409, rely=0.147, height=21, width=48)
                self.Label7.configure(activebackground="#f9f9f9")
                self.Label7.configure(activeforeground="black")
                self.Label7.configure(background="#d9d9d9")
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Segoe UI} -size 9 -weight bold")
                self.Label7.configure(foreground="#000000")
                self.Label7.configure(highlightbackground="#d9d9d9")
                self.Label7.configure(highlightcolor="black")
                self.Label7.configure(text=str(postno[0][1]))#postNO

                self.Label3_1 = tk.Label(self.Fra_sRes)
                self.Label3_1.place(relx=0.591, rely=0.202, height=21, width=71)
                self.Label3_1.configure(activebackground="#f9f9f9")
                self.Label3_1.configure(activeforeground="black")
                self.Label3_1.configure(background="#d9d9d9")
                self.Label3_1.configure(disabledforeground="#a3a3a3")
                self.Label3_1.configure(font="-family {Arial} -size 12")
                self.Label3_1.configure(foreground="#000000")
                self.Label3_1.configure(highlightbackground="#d9d9d9")
                self.Label3_1.configure(highlightcolor="black")
                self.Label3_1.configure(text='''Follower''')

                self.Label3_2 = tk.Label(self.Fra_sRes)
                self.Label3_2.place(relx=0.818, rely=0.202, height=21, width=64)
                self.Label3_2.configure(activebackground="#f9f9f9")
                self.Label3_2.configure(activeforeground="black")
                self.Label3_2.configure(background="#d9d9d9")
                self.Label3_2.configure(disabledforeground="#a3a3a3")
                self.Label3_2.configure(font="-family {Arial} -size 12")
                self.Label3_2.configure(foreground="#000000")
                self.Label3_2.configure(highlightbackground="#d9d9d9")
                self.Label3_2.configure(highlightcolor="black")
                self.Label3_2.configure(text='''Following''')


                global dp
                dp = ImageTk.PhotoImage(Image.open(record[2]).resize((120,80),Image.ANTIALIAS))
                self.Button6 = tk.Button(self.Fra_sRes,image=dp)
                self.Button6.place(relx=0.045, rely=0.11, height=90, width=125)
                self.Button6.configure(activebackground="#ececec")
                self.Button6.configure(activeforeground="#000000")
                self.Button6.configure(background="#f0f0f0")
                self.Button6.configure(borderwidth="0")
                self.Button6.configure(disabledforeground="#a3a3a3")
                self.Button6.configure(foreground="#000000")
                self.Button6.configure(highlightbackground="#d9d9d9")
                self.Button6.configure(highlightcolor="black")
                self.Button6.configure(pady="0")
                self.Button6.configure(text='''Dp''')

                self.Button7 = tk.Button(self.Fra_sRes)
                self.Button7.place(relx=0.591, rely=0.147, height=20, width=70)
                self.Button7.configure(activebackground="#ececec")
                self.Button7.configure(activeforeground="#000000")
                self.Button7.configure(background="#d9d9d9")
                self.Button7.configure(borderwidth="0")
                self.Button7.configure(disabledforeground="#a3a3a3")
                self.Button7.configure(font="-family {Segoe UI} -size 9 -weight bold")
                self.Button7.configure(foreground="#000000")
                self.Button7.configure(highlightbackground="#d9d9d9")
                self.Button7.configure(highlightcolor="black")
                self.Button7.configure(pady="0")
                self.Button7.configure(text=folwerno[0])#followerNo

                
                self.Button8 = tk.Button(self.Fra_sRes)
                self.Button8.place(relx=0.818, rely=0.147, height=21, width=67)
                self.Button8.configure(activebackground="#ececec")
                self.Button8.configure(activeforeground="#000000")
                self.Button8.configure(background="#d9d9d9")
                self.Button8.configure(borderwidth="0")
                self.Button8.configure(disabledforeground="#a3a3a3")
                self.Button8.configure(font="-family {Segoe UI} -size 9 -weight bold")
                self.Button8.configure(foreground="#000000")
                self.Button8.configure(highlightbackground="#d9d9d9")
                self.Button8.configure(highlightcolor="black")
                self.Button8.configure(pady="0")
                self.Button8.configure(text=folwingno[0])#FollwngNO


                font13 = "-family {Segoe UI} -size 13 -weight bold -slant "  \
                            "roman -underline 0 -overstrike 0"
                self.Button9 = tk.Button(self.Fra_sRes,command= lambda: self.followbt(userz))
                self.Button9.place(relx=0.045, rely=0.587, height=34, width=387)
                self.Button9.configure(activebackground="#ececec")
                self.Button9.configure(activeforeground="#000000")
                self.Button9.configure(background="#d9d9d9")
                self.Button9.configure(borderwidth="0")
                self.Button9.configure(disabledforeground="#a3a3a3")
                self.Button9.configure(font=font13)
                self.Button9.configure(foreground="#1892da")
                self.Button9.configure(highlightbackground="#d9d9d9")
                self.Button9.configure(highlightcolor="black")
                self.Button9.configure(pady="0")
                self.Button9.configure(text='''Follow''')

                self.Frame_s = tk.Frame(self.Fra_sRes)
                self.Frame_s.place(relx=0.011, rely=0.679, relheight=0.299
                        , relwidth=0.977)
                
                self.Canvas1 = tk.Canvas(self.Frame_s)
                self.Canvas1.place(relx=0.0, rely=0.0, relheight=1.0
                        , relwidth=1.0)
                self.Canvas1.configure(background="#d9d9d9")
                self.Canvas1.configure(borderwidth="2")
                self.Canvas1.configure(highlightbackground="#d9d9d9")
                self.Canvas1.configure(highlightcolor="black")
                self.Canvas1.configure(insertbackground="black")
                self.Canvas1.configure(relief="ridge")
                self.Canvas1.configure(selectbackground="#c4c4c4")
                self.Canvas1.configure(selectforeground="black")

                self.scrollbar=tk.Scrollbar(self.Frame_s,orient="vertical",command=self.Canvas1.yview)
                self.Canvas1.configure(yscrollcommand=self.scrollbar.set)
                self.scrollbar.pack(side="right",fill="y")

                self.Frame_1.destroy()
                self.Frame_1 = tk.Frame(self.Canvas1)# combine this to scrol
                self.Frame_1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
                self.Frame_1.configure(relief="groove")
                self.Frame_1.configure(background="#d9d9d9")
                self.Canvas1.create_window((0,0),window=self.Frame_1,anchor='nw')
                self.Frame_1.bind("<Configure>",lambda event: self.Canvas1.configure(scrollregion=self.Canvas3.bbox("all")))

        
                global _img_f         
                _img_f = imgsurl
                if _img_f == []:
                    
                    _img_f = ImageTk.PhotoImage(Image.open('nopost.jpg').resize((370,120),Image.ANTIALIAS))
                    tk.Button(self.Frame_1,image=_img_f,background="#eeeeee",
                            borderwidth="0").grid(row=0,column=0,padx=10, pady=10)
                else:
                    global imgcr
                    imgcr=[]
                    l=i=j=0
                    
                    for img in _img_f:
                        
                        imgcr.append(ImageTk.PhotoImage(Image.open(img[1]).resize((110,100),Image.ANTIALIAS)))
                        tk.Button(self.Frame_1,image=imgcr[l],background="#eeeeee",
                            command=lambda pic_id = img[0]: self.popup_dis(pic_id),
                            borderwidth="0").grid(row=j,column=i,padx=10, pady=10)
                        l+=1
                        if(i<2):
                            i+=1
                        else:
                            i=0
                            j+=1    



                
            
            else:
                messagebox.showerror("Error", "NO user by %s"%(userz))
        elif(userz == useridgol):
                messagebox.showwarning("warning", "you cant search your owm")
        else:
            messagebox.showwarning("warning", "Pls enter the field" )

    def followbt(self,userz):
        res = dbvalidate.followingotp(useridgol,userz)
        
        self.Button7.configure(text=res[0])
     
        

class uploadz(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        font12 = "-family {Arial Black} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
       
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.pic_url = None
        self.Button1 = tk.Button(self,command=self.uploadhere)
        self.Button1.place(relx=0.256, rely=0.093, height=155, width=200)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#eeeeee")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Upload here''')

        self.capt = tk.StringVar()
        self.Entry1 = tk.Entry(self,textvariable=self.capt)
        self.Entry1.place(relx=0.465, rely=0.467,height=30, relwidth=0.381)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.093, rely=0.467, height=41, width=94)
        self.Label1.configure(background="#eeeeee")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Caption''')

        self.Button2 = tk.Button(self,command=self.uploaddb)
        self.Button2.place(relx=0.372, rely=0.617, height=44, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#eeeeee")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(font=font12)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(pady="0")        
        self.Button2.configure(foreground="#00bfb6")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(text='''Upload''')

    def uploadhere(self):
        self.pic_url = filedialog.askopenfilename(filetypes=[('Images1', '*.png'),('Images2', '*.jpg')])
        global dis_up
        dis_up = ImageTk.PhotoImage(Image.open(self.pic_url).resize((140,120),Image.ANTIALIAS))
        self.Button1.configure(image=dis_up)
    
    def uploaddb(self):
        capt = self.capt.get() 
        if ( self.pic_url is not None and len(capt)!=0):
            if(dbvalidate.uploadpic(useridgol,self.pic_url,capt)):
                messagebox.showinfo("info"," your pic in uploaded")

        else:
            messagebox.showwarning("warning", "Pls enter all fields" )


class heart(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.controller =controller
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.Frame_s = tk.Frame(self) #add scroll to scr_lcan
        self.Frame_s.place(relx=0.022, rely=0.018, relheight=0.96, relwidth=0.962)

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

        
        font14 = "-family {Kristen ITC} -size 15 -weight normal -slant"  \
              " roman -underline 0 -overstrike 0"
        likerinfo = dbvalidate.getliker(useridgol)
        i=0
        for value in likerinfo:
            tk.Button(self.Frame_1, text= "%s liked your photo (%s)"%(value[0],value[1]),font=font14,height=3,width=35,
                anchor="w",borderwidth="0",foreground="#d11b60").grid(row=i,column=0)
            i+=1



class profileinfo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        font9 = "-family {Segoe UI} -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        self.userz = tk.StringVar()
        self.fname = tk.StringVar()

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
        self.Label2.configure(textvariable=self.userz) #username

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
        self.Label6.configure(textvariable=self.fname) #fname

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
        self.Frame_s.place(relx=0.022, rely=0.670, relheight=0.316, relwidth=0.962)

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

        font10 = "-family Arial -size 20 -weight bold -slant roman "  \
                   "-underline 0 -overstrike 0"
        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.844, rely=0.037, height=41, width=44)
        self.Label5.configure(background="#eeeeee")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text=''':''')

        self.Frame_l = tk.Frame(self)

        self.Label5.bind("<Button-3>", self.open_logout)
        self.Label5.bind("<Motion>", self.disable_log)
        self.Frame_l.bind("<Motion>",self.disable_log2)

        self.Frame_l.configure(relief='groove')
        self.Frame_l.configure(borderwidth="2")
        self.Frame_l.configure(relief="groove")
        self.Frame_l.configure(background="#d9d9d9")
        
        font12 = "-family Arial -size 11 -weight bold -slant roman "  \
               "-underline 0 -overstrike 0"

        self.Button11 = tk.Button(self.Frame_l,command = self.out_out)
        self.Button11.place(relx=0.118, rely=0.125, height=30, width=67)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(borderwidth="0")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(font=font12)
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Log Out''')

        
        self.Button_destroy = tk.Button(self.Frame_l,command = self.deactivate)
        self.Button_destroy.place(relx=0.118, rely=0.550, height=25, width=67)
        self.Button_destroy.configure(activebackground="#ececec")
        self.Button_destroy.configure(background="#d9d9d9")
        self.Button_destroy.configure(borderwidth="0")
        self.Button_destroy.configure(borderwidth="0")
        self.Button_destroy.configure(foreground="red")
        self.Button_destroy.configure(font="-family Arial -size 8 -weight bold -slant roman ")
        self.Button_destroy.configure(text='Deactivate')

        self.setvalue()
    
    def setvalue(self):
        record,folwerno,folwingno,imgsurl,postno = dbvalidate.profile(useridgol)
        self.userz.set(record[0])
        self.fname.set(record[1])
        global dp
        dp = ImageTk.PhotoImage(Image.open(record[2]).resize((120,80),Image.ANTIALIAS))
        self.Button6.configure(image=dp)

        self.Text1.delete("1.0",tk.END)
        self.Text1.insert(tk.END,record[3])
        self.Text1.configure(state='disabled')
        self.Button7.configure(text=folwerno[0])
        self.Button8.configure(text=folwingno[0])

        if(postno == []):
            self.Label7.configure(text="0")
        else:
            self.Label7.configure(text=str(postno[0][1]))

        global _img_f         
        _img_f = imgsurl
        if _img_f == []:
            self.Label7.config(text="0")
            _img_f = ImageTk.PhotoImage(Image.open('nopost.jpg').resize((370,120),Image.ANTIALIAS))
            tk.Button(self.Frame_1,image=_img_f,background="#eeeeee",
                    borderwidth="0").grid(row=0,column=0,padx=10, pady=10)
        else:
            global imgcr
            imgcr=[]
            l=i=j=0
            
            for img in _img_f:
                
                imgcr.append(ImageTk.PhotoImage(Image.open(img[1]).resize((110,100),Image.ANTIALIAS)))
                tk.Button(self.Frame_1,image=imgcr[l],background="#eeeeee",
                       borderwidth="0").grid(row=j,column=i,padx=10, pady=10)
                l+=1
                if(i<2):
                    i+=1
                else:
                    i=0
                    j+=1   

    def out_out(self):
        root.destroy()
        login.start_gui()
    
    def open_logout(self,event):
        try:
            self.Frame_l.place(relx=0.778, rely=0.118, relheight=0.190, relwidth=0.200)
            self.Frame_l.focus_set()
        except:
            pass

    def close_log(self,event):
        try:
            self.Frame_l.place_forget()
            self.Label5.unbind_all("<Button-1>")
        except:
            pass
    
    def disable_log(self,event):
        self.Label5.bind_all("<Button-1>",self.close_log)

   
    def disable_log2(self,event):
        self.Label5.unbind_all("<Button-1>")

    def deactivate(self):
        res = messagebox.askquestion("Deactivate", "Are You Sure?", icon='warning')
        if res == 'yes':
            print("Deleted")
            root.destroy()
            dbvalidate.deactivateuser(useridgol)
            login.start_gui()      


if __name__ == '__main__':
    pass
    
