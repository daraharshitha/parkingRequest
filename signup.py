from tkinter import*
import sqlite3
import re
from tkinter import messagebox
poojith=Tk()

#form inputs
poojith.title("Create Form")
name=StringVar()
reg_no=IntVar(value="")
department=StringVar()
gender=StringVar(value=False)
email=StringVar()
mobile=IntVar(value="")
password=StringVar()
confirm_password=StringVar()
#functions
def QUIT():
    poojith.destroy()
def box():
    messagebox.showinfo("Information","Details have been added")
    name.set("")
    reg_no.set("")
    department.set("")
    gender.set(False)
    email.set("")
    mobile.set("")
    password.set("")
    confirm_password.set("")
def pas():
    if(password.get()!=(confirm_password.get())):
       messagebox.showinfo("Information","Password doesnot match")
       poojith.mainloop()
def check():
    if(name.get()=="" or reg_no.get()=="" or department.get()=="" or gender.get()==False or mobile.get()=="" or password.get()=="" or confirm_password.get()==""):
        messagebox.showerror(message="Please Fill all details")
        poojith.mainloop()  
def new():
    poojith.destroy()
    import request

#fetching databse
def database():
    na=name.get()
    re=reg_no.get()
    de=department.get()
    ge=gender.get()
    em=email.get()
    mo=mobile.get()
    pa=password.get()
    co=confirm_password.get()
    data=sqlite3.connect("signup.db")
    #data.execute("Create table signup(name varchar(50),reg_no int,department text,gender text,email text,mobile int,password varchar(20),confirm_password varchar(20));")
    data.execute("insert into signup(name,reg_no,department,gender,email,mobile,password,confirm_password)values(?,?,?,?,?,?,?,?)",(na,re,de,ge,em,mo,pa,co,))
    data.commit()

#form labels
Label(poojith,text="Parking Management System",font=("aerial", 19),fg="yellow",bg="red").place(x=19,y=5)
Label(poojith,text="NAME",bg="cyan").place(x=50,y=55)
Entry(poojith,textvar=name).place(x=180,y=55)
Label(poojith,text="REG_NO",bg="cyan").place(x=50,y=90)
Entry(poojith,textvar=reg_no).place(x=180,y=90)
Label(poojith,text="DEPARTMENT",bg="cyan").place(x=50,y=125)
Entry(poojith,textvar=department).place(x=180,y=125)
Label(poojith,text="GENDER",bg="cyan").place(x=50,y=160)
r1=Radiobutton(poojith,value="male",bg="cyan",text="MALE",variable=gender).place(x=170,y=160)
r2=Radiobutton(poojith,value="female",bg="cyan",text="FEMALE",variable=gender).place(x=240,y=160)
Label(poojith,text="EMAIL",bg="cyan").place(x=50,y=195)
Entry(poojith,textvar=email).place(x=180,y=195)
Label(poojith,text="MOBILE",bg="cyan").place(x=50,y=230)
Entry(poojith,textvar=mobile).place(x=180,y=230)
Label(poojith,text="PASSWORD",bg="cyan").place(x=50,y=265)
Entry(poojith,textvar=password,show="*").place(x=180,y=265)
Label(poojith,text="REENTER PASSWORD",bg="cyan").place(x=50,y=300)
Entry(poojith,textvar=confirm_password,show="*").place(x=180,y=300)
Button(poojith,text="SUBMIT",relief=GROOVE,width=8,height=2,cursor="star",activebackground="black",activeforeground="white",fg="black",bg="gold",command=lambda:[check(),pas(),database(),box(),new()]).place(x=210,y=350)
Button(poojith,text="QUIT",command=QUIT,width=8,height=2,cursor="cross",activebackground="black",activeforeground="white",fg="black",bg="gold",relief=GROOVE).place(x=90,y=350)
poojith.geometry("380x400")
poojith.configure(background='cyan')
poojith.mainloop()
