import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import MAIN as M
from PIL import Image,ImageTk
import os

required_files = [
    "LOGIN.py",
    "MAIN.py",
    "baground.jpg",
    os.path.join("pic", "pict.jpg")
]

missing_files = [file for file in required_files if not os.path.exists(file)]

if missing_files:
    print("The following required files are missing:")
    for file in missing_files:
        print(f"- {file}")
else:
    print("All required files are present.")

root=tk.Tk()
root.geometry("500x500")
root.title("login page")
root.resizable(0,0)
# to set main background
img_mainbg=Image.open("images.jpg")
img_mainbg=img_mainbg.resize((495,445),Image.Resampling.LANCZOS)
photo_mainbg=ImageTk.PhotoImage(img_mainbg)


lbl_tlt=tk.Label(root,text="LOGIN PAGE",font=("Letter Gothic Std",30,"bold"),fg="#C5A9D5",bg="#490F6A")
lbl_tlt.place(x=0,y=0,width=500,height=50)
frm_main=tk.Frame(root,bd=2,relief=RIDGE,bg="#9D7EAE")
frm_main.place(x=0,y=50,width=500,height=450)
# to place the main background
mainbg=Label(frm_main,image=photo_mainbg)
mainbg.place(x=0,y=0,width=495,height=445)
lbl_uname=tk.Label(frm_main,text="USERNAME:",font=("Letter Gothic Std",15,"bold"),fg="#B096D3",bg="#5B17B6")
lbl_uname.place(x=90,y=80,width=150,height=40)
lbl_passwd=tk.Label(frm_main,text="PASSWORD:",font=("Letter Gothic Std",15,"bold"),fg="#B096D3",bg="#5B17B6")
lbl_passwd.place(x=90,y=130,width=150,height=40)
global ent_passwd,ent_uname
ent_uname=tk.Entry(frm_main,font=("Letter Gothic Std",15,"bold"))
ent_uname.place(x=250,y=80,width=150,height=40)
ent_passwd=tk.Entry(frm_main,font=("Letter Gothic Std",15,"bold"),show="*")
ent_passwd.place(x=250,y=130,width=150,height=40)
def showpasswd():
    if ent_passwd.cget("show") == "*":
        ent_passwd.config(show="")
    else:
        ent_passwd.config(show="*")
def login():
    def passwd():
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from login where Username='"+ent_uname.get()+"'")
        data=my_cursor.fetchall()
        if len(data)==0:
            return str(len(data))
        else:
            return str(data[0][1])
    global pd    
    pd=passwd()
    connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
    if connection.is_connected()==False:
        print("Error***")
    my_cursor=connection.cursor()
    my_cursor.execute("select * from login")
    data=my_cursor.fetchall()
    global l1
    l1=[]
    for j in data:
        l1.append(j[0])
    #for i in data:
        
    if ent_uname.get() not in l1 and ent_passwd.get()!=pd:
        messagebox.showerror("ERROR","THE GIVE DETAILS ARE INCORRECT",parent=root)
    #elif ent_uname.get() in l1 and ent_passwd.get()==pd:
    #    messagebox.showerror("ERROR","THE GIVE DETAILS ARE IN CORRECT",parent=root)                
    else:
        if ent_passwd.get()==pd:
            window=Toplevel(root)
            login=M.cable(window)
            frm=Frame(root,bg="white",height=700,width=1000)
            frm.place(x=0,y=0)
        else:
            print(pd)
            messagebox.showerror("ERROR","THE PASSWORD IN CORRECT",parent=root)




        
def delete():
    yn=messagebox.askyesno("DELETE","ARE YOU SURE TO DELETE THE ACCOUNT",parent=root)
    if yn>0:
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from login where Username='"+ent_uname.get()+"'")
        data=my_cursor.fetchall()
        if len(data)==0:
            messagebox.showerror("ERROR","NO ACCOUNT TO DELETE",parent=root)
        elif len(data)!=0:
            my_cursor.execute("delete from login where Username='"+ent_uname.get()+"'")
            messagebox.showinfo("DELETED","THE EXISTING ACCOUNT IS DELETED PLS SIGN UP TO LOGIN AGAIN",parent=root)
          
def signup():
    def spasswd():
        if enr_passwd.cget("show") == "*":
            enr_passwd.config(show="")
        else:
            enr_passwd.config(show="*")
    sg=tk.Tk()
    sg.title("sign up")
    sg.geometry("400x400")
    sg.resizable(0,0)
    lbl_tlt=tk.Label(sg,text="SIGN UP",font=("Letter Gothic Std",30,"bold"),fg="#C5A9D5",bg="#490F6A")
    lbl_tlt.place(x=0,y=0,width=400,height=50)
    frm_sgup=tk.Frame(sg,bd=2,relief=RIDGE,bg="#9D7EAE")
    frm_sgup.place(x=0,y=50,width=400,height=350)
    lbl_uname=tk.Label(frm_sgup,text="USERNAME:",font=("Letter Gothic Std",15,"bold"),fg="#B096D3",bg="#5B17B6")
    lbl_uname.place(x=50,y=50,width=130,height=30)
    lbl_passwd=tk.Label(frm_sgup,text="PASSWORD:",font=("Letter Gothic Std",15,"bold"),fg="#B096D3",bg="#5B17B6")
    lbl_passwd.place(x=50,y=100,width=130,height=30)
    enr_uname=tk.Entry(frm_sgup,font=("Letter Gothic Std",15,"bold"))
    enr_uname.place(x=200,y=50,width=150,height=30)
    enr_passwd=tk.Entry(frm_sgup,font=("Letter Gothic Std",15,"bold"),show="*")
    enr_passwd.place(x=200,y=100,width=150,height=30)
    chk_showpd=tk.Checkbutton(frm_sgup,text="SHOW PASSWORD",font=("Letter Gothic Std",15,"bold"),command=spasswd,bg="#5B17B6")
    chk_showpd.place(x=150,y=150)


    def below():
        num=("1","2","3","4","5","6","7","8","9","0")
        trueu=0
        d=("!@#$%^&*()-+{}|~`';:")
        for i in enr_uname.get():
            if i in d:
                trueu=1
        
        if enr_uname.get()=="" or enr_passwd.get()=="":
            messagebox.showerror("ERROR","THE REQUIRED DETAILS NOT GIVEN",parent=sg)
        elif trueu>0 :
            messagebox.showerror("ERROR","THE USERNAME CONTAINS EXTRA SYMBOLS",parent=sg)
        
        elif enr_uname.get().startswith(num):
            messagebox.showerror("ERROR","THE USERNAME STARTSWITH NUMBERS",parent=sg)
        else:
            connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
            if connection.is_connected()==False:
                print("Error***")
            my_cursor=connection.cursor()
            my_cursor.execute("select * from login")
            data=my_cursor.fetchall()
            if len(data)==0:
                print("helloo")
                my_cursor.execute("insert into login values (%s,%s);",(enr_uname.get(),enr_passwd.get()))
                connection.commit()
                messagebox.showinfo("SUCCESS","ACCOUNT CREATED",parent=sg)
                sg.destroy()
            elif len(data)!=0:
                for i in data:
                    if i[0]==enr_uname.get():
                        messagebox.showerror("ERROR","THE USERNAME ALREADY EXISTS",parent=sg)
                    else:
                        my_cursor.execute("insert into login values (%s,%s);",(enr_uname.get(),enr_passwd.get()))
                        connection.commit()
                        messagebox.showinfo("SUCCESS","ACCOUNT CREATED",parent=sg)
                        sg.destroy()
    btn_sgup=Button(frm_sgup,text="CREATE",command=below,font=("Letter Gothic Std",15,"bold"),bg="#5B17B6",activebackground="#B096D3")
    btn_sgup.place(x=150,y=250,width=100,height=40)
    sg.mainloop()
chk_showpd=Checkbutton(root,text="SHOW PASSWORD",font=("Letter Gothic Std",15,"bold"),command=showpasswd,bg="#5B17B6")
chk_showpd.place(x=250,y=250)
btn_lgin=Button(root,text="LOGIN",command=login,font=("Letter Gothic Std",15,"bold"),bg="#5B17B6",activebackground="#B096D3")
btn_lgin.place(x=100,y=300,width=100,height=40)
btn_sgup=Button(root,text="SIGN UP",command=signup,font=("Letter Gothic Std",15,"bold"),bg="#5B17B6",activebackground="#B096D3")
btn_sgup.place(x=250,y=300,width=100,height=40)
btn_sgup=Button(root,text="DELETE ACCOUNT",command=delete,font=("Letter Gothic Std",15,"bold"),bg="#5B17B6",activebackground="#B096D3")
btn_sgup.place(x=130,y=350,width=200,height=40)

root.mainloop()
