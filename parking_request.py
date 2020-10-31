from tkinter import *
import sqlite3
from tkinter import messagebox

poojith=Tk()
poojith.title("Parking Reguest Form")
#form inputs
name=StringVar()
mobil=IntVar(value="")
v_number=IntVar(value="")
p_place=IntVar(value="")
v_type=StringVar(value=False)


#functions
def box():
    messagebox.showinfo("information","YOUR REQUEST HAS BEEN RECORDED")
    name.set("")
    mobil.set("")
    v_number.set("")
    p_place.set("")
    v_type.set(False)

def QUIT():
    poojith.destroy()
    #select reg_no from signup join sign on signup.mobile==sign.mobil
    #SELECT signup.reg_no,signup.department,signup.gender,signup.email,signup.password,signup.confirm_password FROM signup JOIN sign ON signup.mobile==sign.mobil;


def check():
    if(name.get()=="" or mobil.get()=="" or v_number.get()=="" or p_place.get()=="" or v_type.get()==True):
        messagebox.showinfo("Information","Please Fill all details")
        poojith.mainloop()


def new():
    poojith.destroy()
    import home_page

        
def database():
    na=name.get()
    m=mobil.get()
    vn=v_number.get()
    pp=p_place.get()
    vt=v_type.get()
    data=sqlite3.connect("signup.db")
    #data.execute("Create table sign(name varchar(50),mobil int,vehicle_number int,parking_place int,vehicle_type text,time text);")
    data.execute("insert into sign(name,mobil,vehicle_number,parking_place,vehicle_type,time)values(?,?,?,?,?,datetime('now','localtime'))",(na,m,vn,pp,vt,))
    data.execute("SELECT signup.reg_no,signup.department,signup.gender,signup.email,signup.password,signup.mobile,signup.confirm_password FROM signup JOIN sign ON signup.mobile==sign.mobil")
    data.commit()


#form labels
Label(poojith,text="Parking Management System",font=("aerial", 19),fg="red",bg="gold").place(x=19,y=5)
Label(poojith,text="NAME",bg="pink").place(x=50,y=55)
Entry(poojith,textvar=name).place(x=180,y=55)
Label(poojith,text="MOBILE",bg="pink").place(x=50,y=90)
Entry(poojith,textvar=mobil).place(x=180,y=90)
Label(poojith,text="VEHICLE NUMBER",bg="pink").place(x=50,y=125)
Entry(poojith,textvar=v_number).place(x=180,y=125)
Label(poojith,text="PARKING PLACE",bg="pink").place(x=50,y=160)
Entry(poojith,textvar=p_place).place(x=180,y=160)
Label(poojith,text="VEHICLE TYPE",bg="pink").place(x=50,y=205)
R1=Radiobutton(poojith,text="2-Wheeler",variable=v_type,value="2-Wheeler",bg="pink").place(x=180,y=205)
R2=Radiobutton(poojith,text="3-Wheeler",variable=v_type,value="3-Wheeler",bg="pink").place(x=180,y=240)
R3=Radiobutton(poojith,text="4-Wheeler",variable=v_type,value="4-Wheeler",bg="pink").place(x=180,y=275)
Button(poojith,text="SUBMIT",relief=GROOVE,width=8,height=2,cursor="star",activebackground="black",activeforeground="white",fg="black",bg="gold",command=lambda:[check(),database(),box(),new()]).place(x=210,y=320)
Button(poojith,text="QUIT",command=QUIT,width=8,height=2,cursor="cross",activebackground="black",activeforeground="white",fg="black",bg="gold",relief=GROOVE).place(x=90,y=320)
poojith.geometry("380x400")
poojith.configure(background='pink')
poojith.mainloop()
