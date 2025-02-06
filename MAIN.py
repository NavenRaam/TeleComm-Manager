import datetime as d
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tokenize import String
from traceback import print_tb
from PIL import Image,ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
import mysql.connector
import customtkinter as ctk

class cable:
    def  __init__(Cust,app):
        Cust.app=app
        Cust.app.geometry("1535x845+0+0")   
        Cust.app.title("TELE-COMMUNICATION SERVICE")
        Cust.app.config(background="#a2d2ff")
    

        #Variables
        Cust.var_CID=StringVar()
        Cust.var_SNO=StringVar()
        Cust.var_PNO=StringVar()
        Cust.var_DOP=StringVar()
        Cust.var_DOE=StringVar()
        Cust.var_MOP=StringVar()
        Cust.var_TOTAL_NOC=StringVar()
        Cust.var_NOC_SUBSCRIBED=StringVar()
        Cust.var_NOC_SUBSCRIBED.set("PACKAGE1")
        Cust.var_AMOUNT=StringVar()
        Cust.var_ADDRESS=StringVar()
        Cust.var_NAME=StringVar()
        Cust.var_ent=StringVar()
        Cust.var_spr=StringVar()
        Cust.var_tam=StringVar()
        Cust.var_cmd=StringVar()
        Cust.var_msc=StringVar()
        Cust.var_cid=StringVar()
        
        Cust.var_CID.set(str(Cust.cid()))    
        Cust.var_TOTAL_NOC.set(Cust.toc_chn()) 
        Cust.var_DOP.set(d.date.today())
        c=d.date.today()
        Cust.var_DOE.set(c+d.timedelta(days=31))
        # to set main background
        img_mainbg=Image.open("baground.jpg")
        img_secbg=Image.open("baground.jpg")
        Cust.photo_mainbg=ImageTk.PhotoImage(img_mainbg)
        img_secbg=img_mainbg.resize((1920,1080),Image.Resampling.LANCZOS)
        Cust.photo_secbg=ImageTk.PhotoImage(img_secbg)

        # Main Frame
        main_frame=Frame(Cust.app,bg="#a2d2ff")
        main_frame.place(x=0,y=0,width=1575,height=700)


        # to place the main background
        Cust.mainbg=Label(Cust.app,bg="#a2d2ff")#
        Cust.mainbg.place(x=0,y=0,width=1540,height=845)


        # to set the title 
        lbl_title=Label(Cust.app,text="TELE-COMMUNICATION SERVICES",font=("Verdana",38,"bold"),fg="#023047",bg="#a2d2ff")
        lbl_title.place(x=320,y=0,width=980,height=50)

        
        # company name
        lbl_title=Label(Cust.app,text="STREAM SYNC",font=("Unispace",40,"bold"),fg="#669bbc",bg="#a2d2ff")
        lbl_title.pack(padx=50,pady=50)
        

        # Upper Frame
        upper_frame=LabelFrame(Cust.app,bd=2,relief=RIDGE,bg="#F36E26",text="CUSTOMER INFORMATION",font=("Helvetica",10,"bold"),foreground="#7F9AD3",background="#bde0fe")
        upper_frame.place(x=50,y=150,width=1430,height=280)
    

        # labels and feilds entries
        # stb
        lbl_stb=Label(upper_frame,font=("Verdana",12),text="SET-TOP-BOX NO:",bg="#669bbc")
        lbl_stb.grid(row=0,column=3,padx=10,sticky=W)

        txt_stb=ttk.Entry(upper_frame,textvariable=Cust.var_SNO,width=22,font=("Verdana",12))
        txt_stb.grid(row=0,column=4,padx=10,pady=4)
        

        # Custid
        lbl_custid=Label(upper_frame,font=("Verdana",12),text="CUSTOMER ID:",bg="#669bbc")
        lbl_custid.grid(row=0,column=1,padx=10,sticky=W)

        
        txt_custid=Entry(upper_frame,text=Cust.var_CID,state=DISABLED,font=("Verdana",12),width=22)
        txt_custid.grid(row=0,column=2,padx=10,pady=4)
        

        # mop
        lbl_mop=Label(upper_frame,font=("Verdana",12),text="MODE OF PAYMENT:",bg="#669bbc")
        lbl_mop.grid(row=3,column=1,padx=10,sticky=W)
        combo_mop=ttk.Combobox(upper_frame,textvariable=Cust.var_MOP,font=("Verdana",12),width=17,state="readonly")
        combo_mop["values"]=("ONLINE","OFFLINE")
        combo_mop.grid(row=3,column=2,padx=10,pady=4,sticky=W)
        
        
        # Totnoc
        lbl_Totnoc=Label(upper_frame,font=("Verdana",12),text="TOTAL NO OF CHANNEL SUBSCRIBED:",bg="#669bbc")
        lbl_Totnoc.grid(row=2,column=3,padx=10,sticky=W)
        
        txt_Totnoc=Entry(upper_frame,text=Cust.var_TOTAL_NOC,state=DISABLED,font=("Verdana",12),width=22)
        txt_Totnoc.grid(row=2,column=4,padx=10,pady=4)
        
        
        # Nocsubs
        lbl_Nocsubs=Label(upper_frame,font=("Verdana",12),text="CHANNEL PACKAGE:",bg="#669bbc")
        lbl_Nocsubs.grid(row=3,column=3,padx=10,sticky=W)
        combo_Nocsubs=ttk.Combobox(upper_frame,textvariable=Cust.var_NOC_SUBSCRIBED,font=("Verdana",12),width=17,state="readonly")
        combo_Nocsubs["values"]=("PACKAGE1","PACKAGE2","PACKAGE3","PACKAGE4")
        combo_Nocsubs.grid(row=3,column=4,padx=10,pady=4,sticky=W)
        
        
        #Name
        lbl_add=Label(upper_frame,font=("Verdana",12),text="NAME:",bg="#669bbc")
        lbl_add.place(x=12,y=145)

        txt_add=ttk.Entry(upper_frame,textvariable=Cust.var_NAME,width=20,font=("Verdana",12))
        txt_add.place(x=82,y=145)
        
        #Adress
        lbl_add=Label(upper_frame,font=("Verdana",12),text="ADDRESS:",bg="#669bbc")
        lbl_add.place(x=302,y=145)

        txt_add=ttk.Entry(upper_frame,textvariable=Cust.var_ADDRESS,width=60,font=("Verdana",12))
        txt_add.place(x=400,y=145)

        
        # Ph no
        lbl_phno=Label(upper_frame,font=("Verdana",12),text="PHONE NO:",bg="#669bbc")
        lbl_phno.grid(row=2,column=1,padx=10,pady=7,sticky=W)

        txt_phno=ttk.Entry(upper_frame,textvariable=Cust.var_PNO,width=22,font=("Verdana",12))
        txt_phno.grid(row=2,column=2,padx=10,pady=4)
        
        
        # dop
        lbl_dop=Label(upper_frame,font=("Verdana",12),text="DATE OF PAYMENT:",bg="#669bbc")
        lbl_dop.grid(row=4,column=1,padx=10,pady=7,sticky=W)

        txt_custid=Entry(upper_frame,text=Cust.var_DOP,state=DISABLED,font=("Verdana",12),width=22)
        txt_custid.grid(row=4,column=2,padx=10,pady=4)

        
        # doe 
        lbl_doe=Label(upper_frame,font=("Verdana",12),text="DATE OF EXPIRE:",bg="#669bbc")
        lbl_doe.grid(row=4,column=3,padx=10,pady=7,sticky=W)
        
        txt_custid=Entry(upper_frame,text=Cust.var_DOE,state=DISABLED,font=("Verdana",12),width=22)
        txt_custid.grid(row=4,column=4,padx=10,pady=4)


        #tv image
        img_tv=Image.open("pic/pict.jpg")
        img_tv=img_tv.resize((340,190),Image.Resampling.LANCZOS)
        Cust.phototv=ImageTk.PhotoImage(img_tv)
        Cust.img_tv=Label(upper_frame,image=Cust.phototv)
        Cust.img_tv.place(x=1050,y=0,width=340,height=170)
        
        
        # Button Frame
        Button_frame1=Frame(upper_frame,bd=2,relief=RIDGE,bg="#bde0fe")
        Button_frame1.place(x=3,y=180,width=1420,height=80)     

        
        # Add
        btn_save=ctk.CTkButton(Button_frame1,text="ADD",command=Cust.add_detail,font=("Futura",16),width=170,height=50,corner_radius=10)
        btn_save.grid(row=0,column=0,padx=55,pady=12)
        
        
        # Delete
        btn_delete=ctk.CTkButton(Button_frame1,text="DELETE",command=Cust.delete_details,font=("Futura",16),width=170,height=50,corner_radius=10)
        btn_delete.grid(row=0,column=2,padx=55,pady=12)
        
        # Update
        btn_update=ctk.CTkButton(Button_frame1,text="UPDATE",command=Cust.update_details,font=("Futura",16),width=170,height=50,corner_radius=10)
        btn_update.grid(row=0,column=3,padx=55,pady=12)
        
        
        # Clear
        btn_clear=ctk.CTkButton(Button_frame1,text="CLEAR",command=Cust.clear_feilds,font=("Futura",16),width=170,height=50,corner_radius=10)
        btn_clear.grid(row=0,column=4,padx=55,pady=12)


        # Menu
        btn_menu=ctk.CTkButton(Button_frame1,text="MORE DETAILS",command=Cust.menu,font=("Futura",16),width=170,height=50,corner_radius=10)
        btn_menu.grid(row=0,column=5,padx=55,pady=12)

        # Lower Frame
        lower_frame=LabelFrame(Cust.app,bd=2,relief=RIDGE,bg="#F36E26",text="CUSTOMER INFORMATION TABLE",font=("Helvetica",10,"bold"),foreground="#7F9AD3",background="#bde0fe")
        lower_frame.place(x=50,y=480,width=1430,height=250)

        # Search Frame
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg="#F36E26",text="SEARCH CUSTOMER INFORMATION",font=("Helvetica",10,"bold"),foreground="#7F9AD3",background="#bde0fe")
        search_frame.place(x=10,y=0,width=1410,height=60)

        search_by=Label(search_frame,font=("Verdana",12),text="SEARCH BY:",fg="black",bg="#669bbc")
        search_by.grid(row=0,column=1,sticky=W,padx=10)

        #Search
        Cust.var_comb_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=Cust.var_comb_search,state="readonly",font=("Verdana",12),width=18)
        com_txt_search["value"]=("SELECT OPTION","CUST_ID","STB_NO")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=2,padx=10,sticky=W)

        Cust.var_search=StringVar()
        txt_dop=ttk.Entry(search_frame,textvariable=Cust.var_search,width=22,font=("Verdana",12))
        txt_dop.grid(row=0,column=3,padx=10,pady=7)
        
        
        btn_search=ctk.CTkButton(search_frame,text="SEARCH",command=Cust.search_details,font=("Futura",16),width=170,height=30,corner_radius=10)
        btn_search.grid(row=0,column=4,padx=50)

        btn_search=ctk.CTkButton(search_frame,text="SHOW ALL",command=Cust.fetch_data,font=("Futura",16),width=170,height=30,corner_radius=10)
        btn_search.grid(row=0,column=5,padx=50)  

        btn_search=ctk.CTkButton(search_frame,text="PACKAGES",command=Cust.package_lists,font=("Futura",16),width=170,height=30,corner_radius=10)
        btn_search.grid(row=0,column=6,padx=50)  

        
        def mmm():
            print("hi")


        #******************************** CUSTOMER TABLE *************************************
        # Table Frame
        table_frame=Frame(lower_frame,bd=3,relief=RIDGE,bg="#bde0fe")
        table_frame.place(x=10,y=62,width=1410,height=155)

        #Custroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Tree view
        Cust.customer_table=ttk.Treeview(table_frame,column=("CUST_ID","NAME","STB_NO","PH_NO","DOP","DOE","MOP",
        "NOC_SUBS","TOT_NOC","AMOUNT","ADDRESS"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=Cust.customer_table.xview)
        scroll_y.config(command=Cust.customer_table.yview)

        Cust.customer_table.heading("CUST_ID",text="CUSTOMER_ID")
        Cust.customer_table.heading("NAME",text="NAME")
        Cust.customer_table.heading("STB_NO",text="STB_NO")
        Cust.customer_table.heading("PH_NO",text="PHONE_NO")
        Cust.customer_table.heading("DOP",text="DOP")
        Cust.customer_table.heading("DOE",text="DOE")
        Cust.customer_table.heading("MOP",text="MOP")
        Cust.customer_table.heading("NOC_SUBS",text="CHANNEL PACKAGE")
        Cust.customer_table.heading("TOT_NOC",text="TOTOAL_NOC")
        Cust.customer_table.heading("AMOUNT",text="AMOUNT")
        Cust.customer_table.heading("ADDRESS",text="ADDRESS")

        Cust.customer_table["show"]="headings"

        Cust.customer_table.column("CUST_ID",width=100)
        Cust.customer_table.column("NAME",width=100)
        Cust.customer_table.column("STB_NO",width=100)
        Cust.customer_table.column("PH_NO",width=100)
        Cust.customer_table.column("DOP",width=100)
        Cust.customer_table.column("DOE",width=100)
        Cust.customer_table.column("MOP",width=100)
        Cust.customer_table.column("NOC_SUBS",width=150)
        Cust.customer_table.column("TOT_NOC",width=150)
        Cust.customer_table.column("AMOUNT",width=100)
        Cust.customer_table.column("ADDRESS",width=350)


        Cust.customer_table.pack(fill=BOTH,expand=0)

        Cust.customer_table.bind("<ButtonRelease>",Cust.get_cursor)

        Cust.fetch_data()
    
    
    #*************************** FUNCTION DECLAREATION ********************************
    #PAYMENT FOR SELECTED CUSTOMER
    def moredetails(Cust):
        Cust.root=tk.Tk()
        Cust.root.geometry("700x260")
        Cust.root.title("Payemnt Window")
        Cust.root.resizable(0,0)
        
        
        main_payframe=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#FF7800")
        main_payframe.place(x=0,y=0,width=700,height=260)

        graph_payframe=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#F19AA2")
        graph_payframe.place(x=10,y=100,width=680,height=150)

        report_frame=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#F19AA2")
        report_frame.place(x=700,y=0,width=590,height=260)

        lbl_paypg=tk.Label(main_payframe,text="MORE DETAILS",font=("Letter Gothic Std",40,"bold"),fg="#FF8700",bg="#80FF00")
        lbl_paypg.place(x=10,y=10,width=675,height=80)

        lbl_custname=tk.Label(graph_payframe,text="CUSTOMER ID:",font=("Comic Sans MS",15,"bold"),fg="#FF8700",bg="#80FF00")
        lbl_custname.place(x=150,y=10,width=180,height=40)

        global txt_cid,txt_cmd,txt_ent,txt_msc,txt_spr,txt_tam

        txt_cid=ttk.Entry(graph_payframe,textvariable=Cust.var_cid.get(),width=22,font=("MS Gothic",15,"bold"))
        txt_cid.place(x=350,y=10,width=180,height=40)

        btn_back=Button(graph_payframe,text="GENERATE REPORT",command=Cust.report,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_back.place(x=20,y=90,width=180,height=40)
        
        btn_back=Button(graph_payframe,text="BACK",command=Cust.root.destroy,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_back.place(x=250,y=90,width=180,height=40)

        btn_showgr=Button(graph_payframe,text="PIE COMPARE",command=Cust.piecomp,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_showgr.place(x=480,y=90,width=180,height=40)

        
        Cust.root.mainloop()


    def back(Cust):
        """img_logo=Image.open("logo.jpg")
        img_logo=img_logo.resize((300,160),Image.Resampling.LANCZOS)
        Cust.photo_logo=ImageTk.PhotoImage(img_logo)
        
        
        # to place the logo
        Cust.logo=Label(Cust.app,image=Cust.photo_logo)
        Cust.logo.place(x=190,y=0,width=50,height=50)"""
        Cust.root.geometry("700x260")


    def menu(Cust):
        Cust.root=tk.Tk()
        Cust.root.geometry("700x260")
        Cust.root.title("Payemnt Window")
        Cust.root.resizable(0,0)
        
        
        main_payframe=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#a2d2ff")
        main_payframe.place(x=0,y=0,width=700,height=260)

        graph_payframe=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#a2d2ff")
        graph_payframe.place(x=10,y=100,width=680,height=150)

        report_frame=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#a2d2ff")
        report_frame.place(x=700,y=0,width=590,height=260)

        lbl_paypg=tk.Label(main_payframe,text="MORE DETAILS",font=("Letter Gothic Std",40,"bold"),fg="#FF8700",bg="#80FF00")
        lbl_paypg.place(x=10,y=10,width=675,height=80)

        lbl_custname=tk.Label(graph_payframe,text="CUSTOMER ID:",font=("Comic Sans MS",15,"bold"),fg="#FF8700",bg="#80FF00")
        lbl_custname.place(x=150,y=10,width=180,height=40)

        global txt_cid,txt_cmd,txt_ent,txt_msc,txt_spr,txt_tam

        txt_cid=ttk.Entry(graph_payframe,textvariable=Cust.var_cid.get(),width=22,font=("MS Gothic",15,"bold"))
        txt_cid.place(x=350,y=10,width=180,height=40)

        btn_back=Button(graph_payframe,text="GENERATE REPORT",command=Cust.report,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_back.place(x=20,y=90,width=180,height=40)
        
        btn_back=Button(graph_payframe,text="BACK",command=Cust.root.destroy,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_back.place(x=250,y=90,width=180,height=40)

        btn_showgr=Button(graph_payframe,text="PIE COMPARE",command=Cust.piecomp,font=("MS Gothic",15,"bold"),width=13,bg="#88FF00",activebackground="#AAF4A8")
        btn_showgr.place(x=480,y=90,width=180,height=40)


    def piecomp(Cust):
        Cust.var_cid.set(txt_cid.get())
        cod=Cust.var_cid.get()
        cod=str(cod)
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from more_detail where CUST_ID='"+cod+"'")
        data=my_cursor.fetchall()
        print(cod)
        if cod=="":
            messagebox.showerror("ERROR","THE CUSTOMER NOT SPECIFIED",parent=Cust.root)
        elif len(data)==0:
            messagebox.showerror("ERROR","THE CUSTOMER NOT PRESENT",parent=Cust.root)
        else:    
            connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
            if connection.is_connected()==False:
                print("Error***")
            my_cursor=connection.cursor()
            my_cursor.execute("select * from more_detail where CUST_ID="+cod)
            data=my_cursor.fetchall()
            if len(data)!=0:
                if data[0][1]==0:
                    messagebox.showinfo("NOTE","THE CUSTOMER IS NEW",parent=Cust.root)
                else:
                    l=["Comedy","Music","Tamil","Entertainment","Sports"]
                    colour=["blue","yellow","pink","green","red"]
                    j=[]
                    for i in data:
                        for k in range(1,len(i)):
                            j.append(i[k])
                    plt.pie(j,colors=colour,labels=l,autopct='%2.1f%%')
                    plt.axis("equal")
                    plt.show()
            else:
                messagebox.showerror("ERROR","THE DATA IS MISMATCHED",parent=Cust.root)  
    

    # REPORT GENERETING
    def report(Cust):
        Cust.var_cid.set(txt_cid.get())
        cod=Cust.var_cid.get()
        cod=str(cod)
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from more_detail where CUST_ID='"+cod+"'")
        data1=my_cursor.fetchall()
        my_cursor.execute("select * from cust_details where CUST_ID='"+cod+"'")
        data2=my_cursor.fetchall()
        print(data1)
        print(data2)
        if cod=="":
            messagebox.showerror("ERROR","CUSTOMER ID NOT GIVEN",parent=Cust.root)
        elif len(data1)==0 or len(data2)==0:
            messagebox.showinfo("NOTE","NO CUSTOMER IN DATABASE",parent=Cust.root)
        elif len(data1)!=0 and len(data2)!=0:
            print("hi")
            Cust.root.geometry("1290x260")
            
            report_frame=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#a2d2ff")
            report_frame.place(x=700,y=0,width=590,height=260)

            
            rr_frame=tk.Frame(Cust.root,bd=2,relief=tk.RIDGE,bg="#a2d2ff")
            rr_frame.place(x=700,y=0,width=590,height=260)  
            lbl_ccid=Label(rr_frame,font=("MS Gothic",12,"bold"),text="CustID:",bg="#FF8700")
            lbl_ccid.place(x=10,y=10,width=130,height=25)
            lbl_sstb=Label(rr_frame,font=("MS Gothic",12,"bold"),text="STB NO:",bg="#FF8700")
            lbl_sstb.place(x=10,y=45,width=130,height=25)
            lbl_phno=Label(rr_frame,font=("MS Gothic",12,"bold"),text="PH NO:",bg="#FF8700")
            lbl_phno.place(x=10,y=80,width=130,height=25)
            lbl_ddop=Label(rr_frame,font=("MS Gothic",12,"bold"),text="DOP:",bg="#FF8700")
            lbl_ddop.place(x=10,y=115,width=130,height=25)
            lbl_ddoe=Label(rr_frame,font=("MS Gothic",12,"bold"),text="DOE:",bg="#FF8700")
            lbl_ddoe.place(x=10,y=150,width=130,height=25)
            lbl_mmop=Label(rr_frame,font=("MS Gothic",12,"bold"),text="MOP:",bg="#FF8700")
            lbl_mmop.place(x=10,y=185,width=130,height=25)
            lbl_tnoc=Label(rr_frame,font=("MS Gothic",12,"bold"),text="PACKAGE:",bg="#FF8700")
            lbl_tnoc.place(x=10,y=220,width=130,height=25)
            lbl_cpkg=Label(rr_frame,font=("MS Gothic",12,"bold"),text="TOT_NOC:",bg="#FF8700")
            lbl_cpkg.place(x=300,y=220,width=130,height=25)
            lbl_aamt=Label(rr_frame,font=("MS Gothic",12,"bold"),text="AMOUNT:",bg="#FF8700")
            lbl_aamt.place(x=300,y=10,width=130,height=25)
            lbl_eent=Label(rr_frame,font=("MS Gothic",12,"bold"),text="Entertainment:",bg="#FF8700")
            lbl_eent.place(x=300,y=45,width=130,height=25)
            lbl_sspr=Label(rr_frame,font=("MS Gothic",12,"bold"),text="Sports:",bg="#FF8700")
            lbl_sspr.place(x=300,y=80,width=130,height=25)
            lbl_ccmd=Label(rr_frame,font=("MS Gothic",12,"bold"),text="Comedy:",bg="#FF8700")
            lbl_ccmd.place(x=300,y=115,width=130,height=25)
            lbl_ttam=Label(rr_frame,font=("MS Gothic",12,"bold"),text="Tamil:",bg="#FF8700")
            lbl_ttam.place(x=300,y=150,width=130,height=25)
            lbl_mmsc=Label(rr_frame,font=("MS Gothic",12,"bold"),text="Music:",bg="#FF8700")
            lbl_mmsc.place(x=300,y=185,width=130,height=25)

            """txt_ccid=Entry(rr_frame,font=("Verdana",12),width=22)
            txt_ccid.place(x=150,y=10,width=140,height=25)"""
            txt_ccid=Label(rr_frame,text=data2[0][0],font=("Verdana",12),width=22)
            txt_ccid.place(x=150,y=10,width=140,height=25)
            txt_sstb=Label(rr_frame,text=data2[0][2],font=("Verdana",12),width=22)
            txt_sstb.place(x=150,y=44,width=140,height=25)
            txt_phno=Label(rr_frame,text=data2[0][3],font=("Verdana",12),width=22)
            txt_phno.place(x=150,y=80,width=140,height=25)
            txt_ddop=Label(rr_frame,text=data2[0][4],font=("Verdana",12),width=22)
            txt_ddop.place(x=150,y=115,width=140,height=25)
            txt_ddoe=Label(rr_frame,text=data2[0][5],font=("Verdana",12),width=22)
            txt_ddoe.place(x=150,y=150,width=140,height=25)
            txt_mmop=Label(rr_frame,text=data2[0][6],font=("Verdana",12),width=22)
            txt_mmop.place(x=150,y=185,width=140,height=25)
            txt_tnoc=Label(rr_frame,text=data2[0][7],font=("Verdana",12),width=22)
            txt_tnoc.place(x=150,y=220,width=140,height=25)
            txt_cpkg=Label(rr_frame,text=data2[0][8],font=("Verdana",12),width=22)
            txt_cpkg.place(x=440,y=220,width=140,height=25)
            txt_aamt=Label(rr_frame,text=data2[0][9],font=("Verdana",12),width=22)
            txt_aamt.place(x=440,y=10,width=140,height=25)
            txt_eent=Label(rr_frame,text=data1[0][1],font=("Verdana",12),width=22)
            txt_eent.place(x=440,y=50,width=140,height=25)
            txt_sspr=Label(rr_frame,text=data1[0][2],font=("Verdana",12),width=22)
            txt_sspr.place(x=440,y=80,width=140,height=25)
            txt_ccmd=Label(rr_frame,text=data1[0][3],font=("Verdana",12),width=22)
            txt_ccmd.place(x=440,y=115,width=140,height=25)
            txt_ttam=Label(rr_frame,text=data1[0][4],font=("Verdana",12),width=22)
            txt_ttam.place(x=440,y=150,width=140,height=25)
            txt_mmsc=Label(rr_frame,text=data1[0][5],font=("Verdana",12),width=22)
            txt_mmsc.place(x=440,y=180,width=140,height=25)
        
            
    #ADD RECORD FUNCTION
    def add_detail(Cust):
        if Cust.var_CID=="":# or Cust.var_STREET_NO==" ":
            messagebox.showerror("ERROR","ALL FEILDS NEED TO BE FILLED!!")
        else:
            try:
                CAMT=""
                if Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE1":
                    CAMT="200"
                elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE2":
                    CAMT="250"
                elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE3":
                    CAMT="300"
                elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE4":
                    CAMT="350"
                global c
                c=str(Cust.cid())
                Cust.var_CID.set(c)
                Cust.var_TOTAL_NOC.set(Cust.toc_chn())
                connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
                if connection.is_connected()==False:
                    print("Error***")
                my_cursor=connection.cursor()
                print(Cust.var_SNO.get())
                my_cursor.execute("insert into cust_details value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    Cust.var_CID.get(),
                                                                                                                    Cust.var_NAME.get(),
                                                                                                                    Cust.var_SNO.get(),
                                                                                                                    Cust.var_PNO.get(),
                                                                                                                    Cust.var_DOP.get(),
                                                                                                                    Cust.var_DOE.get(),
                                                                                                                    Cust.var_MOP.get(),
                                                                                                                    Cust.var_TOTAL_NOC.get(),
                                                                                                                    Cust.var_NOC_SUBSCRIBED.get(),
                                                                                                                    CAMT,
                                                                                                                    Cust.var_ADDRESS.get(),
                                                                                                                   
                                                                                                                 
                                                                                                                ))
                connection.commit()
                Cust.fetch_data()
                connection.close()
                messagebox.showinfo("SUCCESS","CUSTOMER DETAILS HAS BEEN ADDED!!",parent=Cust.app)
                connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
                if connection.is_connected()==False:
                    print("Error***")
                my_cursor=connection.cursor()
                my_cursor.execute("insert into more_detail values ("+ Cust.var_CID.get()+ ",0,0,0,0,0);")
                connection.commit()
            except Exception as es:
                messagebox.showerror("ERROR",f"Due to:{str(es)}",parent=Cust.app)



    #***************** FETCH DATA ********************

    def fetch_data(Cust):
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from cust_details;")
        data=my_cursor.fetchall()
        if len(data)!=0:
            Cust.customer_table.delete(*Cust.customer_table.get_children())
            for i in data:
                Cust.customer_table.insert("",END,values=i)
            connection.commit()
        connection.close()
   
   
   
    # get cursor
    def get_cursor(Cust,event=""):
        cursor_row=Cust.customer_table.focus()
        content=Cust.customer_table.item(cursor_row)
        data=content["values"]
        
        Cust.var_CID.set(data[0])
        Cust.var_NAME.set(data[1])
        Cust.var_SNO.set(data[2])
        Cust.var_PNO.set(data[3])
        Cust.var_DOP.set(data[4])
        Cust.var_DOE.set(data[5])
        Cust.var_MOP.set(data[6])
        Cust.var_TOTAL_NOC.set(Cust.toc_chn())
        Cust.var_NOC_SUBSCRIBED.set(data[8])
        Cust.var_AMOUNT.set(data[9])
        Cust.var_ADDRESS.set(data[10])

    #get customer id
    def cid(Cust):
        connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
        if connection.is_connected()==False:
            print("Error***")
        my_cursor=connection.cursor()
        my_cursor.execute("select * from cust_details;")
        data=my_cursor.fetchall()
        if len(data)==0:
            return 26331
        else:
            global l
            l=[]
            for k in range(len(data)):
                l.append(data[k][0])
            return max(l)+1

    #get total channel
    def toc_chn(Cust):
        f=Cust.var_NOC_SUBSCRIBED.get()
        if f=="PACKAGE1":
            return 15
        elif f=="PACKAGE2":
            return 20
        elif f=="PACKAGE3":
            return 25
        elif f=="PACKAGE4":
            return 30
    
    # UPDATE RECOED FUNCTION
    def update_details(Cust):
        if Cust.var_CID.get()=="" or Cust.var_SNO.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS NEED TO BE FILLED!!")
        else:
            try:
                update=messagebox.askyesno("UPDATE","ARE SURE TO UPDATE THE CUSTOMER DETAIL!!!",parent=Cust.app)
                if update>0:
                    CAMT=""
                    if Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE1":
                        CAMT="200"
                    elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE2":
                        CAMT="250"
                    elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE3":
                        CAMT="300"
                    elif Cust.var_NOC_SUBSCRIBED.get()=="PACKAGE4":
                        CAMT="350"
                    connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
                    if connection.is_connected()==False:
                        print("Error***")
                    my_cursor=connection.cursor()
                    Cust.var_TOTAL_NOC.set(Cust.toc_chn())
                    my_cursor.execute("update cust_details set NAME=%s,STB_NO=%s,PH_NO=%s,DOP=%s,DOE=%s,MOP=%s,TOTAL_NOC=%s,NOC_SUBS=%s,AMOUNT=%s,ADDRESS=%s where CUST_ID=%s;",(

                                                                                                                                                                                Cust.var_NAME.get(),                     
                                                                                                                                                                                Cust.var_SNO.get(),
                                                                                                                                                                                Cust.var_PNO.get(),
                                                                                                                                                                                Cust.var_DOP.get(),
                                                                                                                                                                                Cust.var_DOE.get(),
                                                                                                                                                                                Cust.var_MOP.get(),
                                                                                                                                                                                Cust.var_TOTAL_NOC.get(),
                                                                                                                                                                                Cust.var_NOC_SUBSCRIBED.get(),
                                                                                                                                                                                CAMT,
                                                                                                                                                                                Cust.var_ADDRESS.get(),
                                                                                                                                                                                Cust.var_CID.get()))
                else:
                    if not update:
                        return
                connection.commit()
                Cust.fetch_data()
                connection.close()
                messagebox.showinfo("SUCCESS","CUSTOMER DETAILS UPDATED SUCCESSFULLY!!!",parent=Cust.app)
            except Exception as es:
                messagebox.showerror("ERROR",f"Due to:{str(es)}",parent=Cust.app)


    
    #DELETE RECORD FUNCTION 
    def delete_details(Cust):
        if Cust.var_CID.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS NEED TO BE FILLED")
        else:
            try:
                delete=messagebox.askyesno("DELETE","ARE YOU SURE TO DELETE THE CUSTOMER DETAILS",parent=Cust.app)
                if delete>0:
                    connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
                    if connection.is_connected()==False:
                        print("Error***")
                    my_cursor=connection.cursor()
                    sql="delete from cust_details where CUST_ID=%s"
                    my_cursor.execute("delete from more_detail where CUST_ID=" + Cust.var_CID.get())
                    value=(Cust.var_CID.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                connection.commit()
                Cust.fetch_data() 
                connection.close()
                messagebox.showinfo("DELETED","CUSTOMER DETAILS DELETED SUCCESFULLY!!!",parent=Cust.app)
            except Exception as es:
                messagebox.showerror("ERROR","CUSTOMER DETAILS IS GIVEN WRONG",parent=Cust.app)



    # CLEAR ALL FEILDS
    def clear_feilds(Cust):
        Cust.var_CID.set(str(Cust.cid()))
        Cust.var_NAME.set("")
        Cust.var_SNO.set("")
        Cust.var_PNO.set("")
        Cust.var_DOP.set(d.date.today())
        c=d.date.today()
        Cust.var_DOE.set(c+d.timedelta(days=31))
        Cust.var_MOP.set("")
        Cust.var_TOTAL_NOC.set(Cust.toc_chn())
        Cust.var_NOC_SUBSCRIBED.set("")
        Cust.var_ADDRESS.set("")
        Cust.fetch_data()

    

    # SEARCH FUNCTION
    def search_details(Cust):
        if Cust.var_comb_search.get()=="" or Cust.var_search.get()=="":
            messagebox.showerror("ERROR","PLEASE GIVE THE CORRECT INPUT")
        else:
            try:
                connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
                if connection.is_connected()==False:
                    print("Error***")
                my_cursor=connection.cursor()
                my_cursor.execute('select * from cust_details where ' +str(Cust.var_comb_search.get()) + " LIKE '%" +str(Cust.var_search.get() + "%' "))
                global tot
                tot=str(Cust.var_search.get())
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    Cust.customer_table.delete(*Cust.customer_table.get_children())
                    for i in rows:
                        Cust.customer_table.insert("",END,values=i)
                connection.commit
                connection.close()

            except Exception as es:
                messagebox.showerror("ERROR","THE CUSTOMER DETAILS NOT FOUND",parent=Cust.app)
        

    
    
    def delete(Cust):
        yn=messagebox.askyesno("DELETE","ARE YOU SURE TO DELETE THE ACCOUNT",parent=Cust.app)
        if yn>0:
            connection= mysql.connector.connect(host="localhost",user="root",passwd="",database="ants_dishes")
            if connection.is_connected()==False:
                print("Error***")
            my_cursor=connection.cursor()
            my_cursor.execute("select * from login")
            data=my_cursor.fetchall()
            if len(data)==0:
                messagebox.showerror("ERROR","NO ACCOUNT TO DELETE PLS SIGN UP",parent=Cust.root)
            else:
                my_cursor.execute("delete from login where Username='"+data[0][0]+"'")
                messagebox.showinfo("DELETED","THE EXISTING ACCOUNT IS DELETED PLS SIGN UP TO LOGIN AGAIN",parent=Cust.root)

    def package_lists(Cust):
        mn=tk.Tk()
        mn.title("CHOOSE PACKAGES")
        mn.geometry("1000x700")
        mn.resizable(0,0)
        mn_frame=Frame(mn,bd=2,relief=RIDGE,bg="#a2d2ff")
        mn_frame.place(x=0,y=0,width=1000,height=700)
        lbl_n1=Label(mn_frame,font=("MS Gothic",12,"bold"),text="PACKAGE 1",fg="#0096c7",bg="#a2d2ff")
        lbl_n1.place(x=30,y=10,width=120,height=40)
        lbl_n2=Label(mn_frame,font=("MS Gothic",12,"bold"),text="PACKAGE 2",fg="#0096c7",bg="#a2d2ff")
        lbl_n2.place(x=490,y=10,width=120,height=40)
        lbl_n3=Label(mn_frame,font=("MS Gothic",12,"bold"),text="PACKAGE 3",fg="#0096c7",bg="#a2d2ff")
        lbl_n3.place(x=30,y=350,width=120,height=40)
        lbl_n4=Label(mn_frame,font=("MS Gothic",12,"bold"),text="PACKAGE 4",fg="#0096c7",bg="#a2d2ff")
        lbl_n4.place(x=490,y=350,width=120,height=40)
        p1_frame=Frame(mn,bd=2,relief=RIDGE,bg="#a2d2ff")
        p1_frame.place(x=50,y=45,width=300,height=300)
        p2_frame=Frame(mn,bd=2,relief=RIDGE,bg="#a2d2ff")
        p2_frame.place(x=510,y=45,width=300,height=300)
        p3_frame=Frame(mn,bd=2,relief=RIDGE,bg="#a2d2ff")
        p3_frame.place(x=50,y=380,width=450,height=300)
        p4_frame=Frame(mn,bd=2,relief=RIDGE,bg="#a2d2ff")
        p4_frame.place(x=510,y=380,width=450,height=300)

        #package1
        lbl_c1=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c1.grid(row=0,column=0,padx=2,pady=2)
        lbl_c2=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c2.grid(row=1,column=0,padx=2,pady=2)
        lbl_c3=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="K Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c3.grid(row=2,column=0,padx=2,pady=2)
        lbl_c4=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Zee Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c4.grid(row=3,column=0,padx=2,pady=2)
        lbl_c5=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Adthiya",fg="#0096c7",bg="#a2d2ff")
        lbl_c5.grid(row=4,column=0,padx=2,pady=2)
        lbl_c6=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Siripoli",fg="#0096c7",bg="#a2d2ff")
        lbl_c6.grid(row=5,column=0,padx=2,pady=2)
        lbl_c7=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="StarSportsTamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c7.grid(row=6,column=0,padx=2,pady=2)
        lbl_c8=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 1",fg="#0096c7",bg="#a2d2ff")
        lbl_c8.grid(row=7,column=0,padx=2,pady=2)
        lbl_c9=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 2",fg="#0096c7",bg="#a2d2ff")
        lbl_c9.grid(row=0,column=1,padx=2,pady=2)
        lbl_c10=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 3",fg="#0096c7",bg="#a2d2ff")
        lbl_c10.grid(row=1,column=1,padx=2,pady=2)
        lbl_c11=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Chutty Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c11.grid(row=2,column=1,padx=2,pady=2)
        lbl_c12=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Disney Channel",fg="#0096c7",bg="#a2d2ff")
        lbl_c12.grid(row=3,column=1,padx=2,pady=2)
        lbl_c13=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Hungama",fg="#0096c7",bg="#a2d2ff")
        lbl_c13.grid(row=4,column=1,padx=2,pady=2)
        lbl_c14=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c14.grid(row=5,column=1,padx=2,pady=2)
        lbl_c15=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="Isai Aruvi",fg="#0096c7",bg="#a2d2ff")
        lbl_c15.grid(row=6,column=1,padx=2,pady=2)
        lbl_p1=Label(p1_frame,font=("MS Gothic",12,"bold"),width=15,text="PRICE:200",fg="#0096c7",bg="#1d3557")
        lbl_p1.grid(row=7,column=1,padx=2,pady=2)

        #pacakge2
        lbl_c1=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c1.grid(row=0,column=0,padx=2,pady=2)
        lbl_c2=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c2.grid(row=1,column=0,padx=2,pady=2)
        lbl_c3=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="K Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c3.grid(row=2,column=0,padx=2,pady=2)
        lbl_c4=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Zee Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c4.grid(row=3,column=0,padx=2,pady=2)
        lbl_c5=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Adthiya",fg="#0096c7",bg="#a2d2ff")
        lbl_c5.grid(row=4,column=0,padx=2,pady=2)
        lbl_c6=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Siripoli",fg="#0096c7",bg="#a2d2ff")
        lbl_c6.grid(row=5,column=0,padx=2,pady=2)
        lbl_c7=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="StarSportsTamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c7.grid(row=6,column=0,padx=2,pady=2)
        lbl_c8=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 1",fg="#0096c7",bg="#a2d2ff")
        lbl_c8.grid(row=7,column=0,padx=2,pady=2)
        lbl_c9=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 2",fg="#0096c7",bg="#a2d2ff")
        lbl_c9.grid(row=0,column=1,padx=2,pady=2)
        lbl_c10=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 3",fg="#0096c7",bg="#a2d2ff")
        lbl_c10.grid(row=1,column=1,padx=2,pady=2)
        lbl_c11=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Chutty Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c11.grid(row=2,column=1,padx=2,pady=2)
        lbl_c12=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Disney Channel",fg="#0096c7",bg="#a2d2ff")
        lbl_c12.grid(row=3,column=1,padx=2,pady=2)
        lbl_c13=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Hungama",fg="#0096c7",bg="#a2d2ff")
        lbl_c13.grid(row=4,column=1,padx=2,pady=2)
        lbl_c14=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c14.grid(row=5,column=1,padx=2,pady=2)
        lbl_c15=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Isai Aruvi",fg="#0096c7",bg="#a2d2ff")
        lbl_c15.grid(row=6,column=1,padx=2,pady=2)
        lbl_c16=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Discovery",fg="#0096c7",bg="#a2d2ff")
        lbl_c16.grid(row=7,column=1,padx=2,pady=2)
        lbl_c17=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c17.grid(row=8,column=0,padx=2,pady=2)
        lbl_c18=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c18.grid(row=8,column=1,padx=2,pady=2)
        lbl_c19=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Movies",fg="#0096c7",bg="#a2d2ff")
        lbl_c19.grid(row=9,column=0,padx=2,pady=2)
        lbl_c20=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c20.grid(row=9,column=1,padx=2,pady=2)
        lbl_p2=Label(p2_frame,font=("MS Gothic",12,"bold"),width=15,text="PRICE:250",fg="#0096c7",bg="#1d3557")
        lbl_p2.grid(row=10,column=1,padx=2,pady=2)

        

        #package3
        lbl_c1=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c1.grid(row=0,column=0,padx=2,pady=2)
        lbl_c2=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c2.grid(row=1,column=0,padx=2,pady=2)
        lbl_c3=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="K Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c3.grid(row=2,column=0,padx=2,pady=2)
        lbl_c4=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Zee Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c4.grid(row=3,column=0,padx=2,pady=2)
        lbl_c5=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Adthiya",fg="#0096c7",bg="#a2d2ff")
        lbl_c5.grid(row=4,column=0,padx=2,pady=2)
        lbl_c6=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Siripoli",fg="#0096c7",bg="#a2d2ff")
        lbl_c6.grid(row=5,column=0,padx=2,pady=2)
        lbl_c7=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="StarSportsTamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c7.grid(row=6,column=0,padx=2,pady=2)
        lbl_c8=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 1",fg="#0096c7",bg="#a2d2ff")
        lbl_c8.grid(row=7,column=0,padx=2,pady=2)
        lbl_c9=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 2",fg="#0096c7",bg="#a2d2ff")
        lbl_c9.grid(row=0,column=1,padx=2,pady=2)
        lbl_c10=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 3",fg="#0096c7",bg="#a2d2ff")
        lbl_c10.grid(row=1,column=1,padx=2,pady=2)
        lbl_c11=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Chutty Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c11.grid(row=2,column=1,padx=2,pady=2)
        lbl_c12=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Disney Channel",fg="#0096c7",bg="#a2d2ff")
        lbl_c12.grid(row=3,column=1,padx=2,pady=2)
        lbl_c13=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Hungama",fg="#0096c7",bg="#a2d2ff")
        lbl_c13.grid(row=4,column=1,padx=2,pady=2)
        lbl_c14=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c14.grid(row=5,column=1,padx=2,pady=2)
        lbl_c15=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Isai Aruvi",fg="#0096c7",bg="#a2d2ff")
        lbl_c15.grid(row=6,column=1,padx=2,pady=2)
        lbl_c16=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Discovery",fg="#0096c7",bg="#a2d2ff")
        lbl_c16.grid(row=7,column=1,padx=2,pady=2)
        lbl_c17=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c17.grid(row=8,column=0,padx=2,pady=2)
        lbl_c18=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c18.grid(row=8,column=1,padx=2,pady=2)
        lbl_c19=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Movies",fg="#0096c7",bg="#a2d2ff")
        lbl_c19.grid(row=9,column=0,padx=2,pady=2)
        lbl_c20=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c20.grid(row=9,column=1,padx=2,pady=2)
        lbl_c21=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="DhoorDharshan",fg="#0096c7",bg="#a2d2ff")
        lbl_c21.grid(row=10,column=0,padx=2,pady=2)
        lbl_c22=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun News",fg="#0096c7",bg="#a2d2ff")
        lbl_c22.grid(row=10,column=1,padx=2,pady=2)
        lbl_c23=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Polimer News",fg="#0096c7",bg="#a2d2ff")
        lbl_c23.grid(row=0,column=3,padx=2,pady=2)
        lbl_c24=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Telugu",fg="#0096c7",bg="#a2d2ff")
        lbl_c24.grid(row=1,column=3,padx=2,pady=2)
        lbl_c25=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="Kalaingar Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=2,column=3,padx=2,pady=2)
        lbl_p3=Label(p3_frame,font=("MS Gothic",12,"bold"),width=15,text="PRICE:300",fg="#0096c7",bg="#1d3557")
        lbl_p3.grid(row=3,column=3,padx=2,pady=2)



        #package4
        lbl_c1=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c1.grid(row=0,column=0,padx=2,pady=2)
        lbl_c2=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c2.grid(row=1,column=0,padx=2,pady=2)
        lbl_c3=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="K Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c3.grid(row=2,column=0,padx=2,pady=2)
        lbl_c4=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Zee Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c4.grid(row=3,column=0,padx=2,pady=2)
        lbl_c5=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Adthiya",fg="#0096c7",bg="#a2d2ff")
        lbl_c5.grid(row=4,column=0,padx=2,pady=2)
        lbl_c6=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Siripoli",fg="#0096c7",bg="#a2d2ff")
        lbl_c6.grid(row=5,column=0,padx=2,pady=2)
        lbl_c7=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="StarSportsTamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c7.grid(row=6,column=0,padx=2,pady=2)
        lbl_c8=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 1",fg="#0096c7",bg="#a2d2ff")
        lbl_c8.grid(row=7,column=0,padx=2,pady=2)
        lbl_c9=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 2",fg="#0096c7",bg="#a2d2ff")
        lbl_c9.grid(row=0,column=1,padx=2,pady=2)
        lbl_c10=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Star Sports 3",fg="#0096c7",bg="#a2d2ff")
        lbl_c10.grid(row=1,column=1,padx=2,pady=2)
        lbl_c11=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Chutty Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c11.grid(row=2,column=1,padx=2,pady=2)
        lbl_c12=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Disney Channel",fg="#0096c7",bg="#a2d2ff")
        lbl_c12.grid(row=3,column=1,padx=2,pady=2)
        lbl_c13=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Hungama",fg="#0096c7",bg="#a2d2ff")
        lbl_c13.grid(row=4,column=1,padx=2,pady=2)
        lbl_c14=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c14.grid(row=5,column=1,padx=2,pady=2)
        lbl_c15=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Isai Aruvi",fg="#0096c7",bg="#a2d2ff")
        lbl_c15.grid(row=6,column=1,padx=2,pady=2)
        lbl_c16=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Discovery",fg="#0096c7",bg="#a2d2ff")
        lbl_c16.grid(row=7,column=1,padx=2,pady=2)
        lbl_c17=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c17.grid(row=8,column=0,padx=2,pady=2)
        lbl_c18=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Tamil",fg="#0096c7",bg="#a2d2ff")
        lbl_c18.grid(row=8,column=1,padx=2,pady=2)
        lbl_c19=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Movies",fg="#0096c7",bg="#a2d2ff")
        lbl_c19.grid(row=9,column=0,padx=2,pady=2)
        lbl_c20=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Music",fg="#0096c7",bg="#a2d2ff")
        lbl_c20.grid(row=9,column=1,padx=2,pady=2)
        lbl_c21=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="DhoorDharshan",fg="#0096c7",bg="#a2d2ff")
        lbl_c21.grid(row=10,column=0,padx=2,pady=2)
        lbl_c22=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Sun News",fg="#0096c7",bg="#a2d2ff")
        lbl_c22.grid(row=10,column=1,padx=2,pady=2)
        lbl_c23=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Polimer News",fg="#0096c7",bg="#a2d2ff")
        lbl_c23.grid(row=0,column=3,padx=2,pady=2)
        lbl_c24=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Rasi Telugu",fg="#0096c7",bg="#a2d2ff")
        lbl_c24.grid(row=1,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Kalaingar Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=2,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Jaya Tv",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=3,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Takkar",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=4,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Vijay Super",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=5,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="History Tv 18",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=6,column=3,padx=2,pady=2)
        lbl_c25=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="Sonic",fg="#0096c7",bg="#a2d2ff")
        lbl_c25.grid(row=7,column=3,padx=2,pady=2)
        lbl_p4=Label(p4_frame,font=("MS Gothic",12,"bold"),width=15,text="PRICE:350",fg="#0096c7",bg="#1d3557")
        lbl_p4.grid(row=8,column=3,padx=2,pady=2)




        mn.mainloop()
    
if __name__=="__main__":
    app=Tk()
    obj=cable(app)
    app.mainloop()
