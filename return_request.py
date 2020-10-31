from tkinter import *
import sqlite3
def Database():
   global conn, cursor
   conn = sqlite3.connect("signup.db")
   cursor = conn.cursor()
def Proceed(event=None):
   Database()
   
   if Reg_no.get() == "" or Password.get() == "" or Vehicle.get() == "" or C.get() == "" or Vehicle_no.get() == "":
      label = Label(root,text="fill all places", width="40", fg="red", bg="Yellow").place(x=100,y=100)
   else:
       cursor.execute("SELECT * FROM `sign` WHERE `name` == ? AND `mobil` == ? AND `vehicle_number` == ? AND `parking_place` == ? AND `vehicle_type` == ?", (Reg_no.get(),Password.get(),Vehicle.get(),C.get(),Vehicle_no.get()))
       if cursor.fetchone() is not None:
          HomeWindow()
          label = Label(root,text="valid DATA provided", width="40", fg="red", bg="Yellow" ).place(x=100,y=100)
      
       else:
          label = Label(root,text="Invalid DATA provided", width="40", fg="red", bg="Yellow").place(x=100,y=100)   
   cursor.close()
   conn.close()
def HomeWindow():                                       #creates next window
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("car parking management")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home= Label(Home, text="\nThank You\n\n Please visit again", font=('times new roman', 60),fg="black",).pack()
   # btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
root = Tk()
root.geometry('500x500')
root.title("return request")


Reg_no=StringVar(value="")
Password=IntVar(value="")
Vehicle_no=StringVar(value="")
Vehicle=IntVar(value="")
C=IntVar(value="")
   
   
             
label_0 = Label(root, text="Return Request",bg="#008080",width=20,font=("bold", 20),fg="ORANGE")
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name   ",width=20,bg="#008080", font=('Courier', 14),fg="Yellow")
label_1.place(x=40,y=130)

entry_1 = Entry(root,textvariable=Reg_no)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Mobile  ",width=20,bg="#008080", font=('Courier', 14),fg="Yellow")
label_2.place(x=40,y=180)

entry_2 = Entry(root,textvariable=Password)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Vehicle_no",width=20,bg="#008080", font=('Courier', 14),fg="Yellow")
label_3.place(x=40,y=230)

entry_6 = Entry(root,textvariable=Vehicle)
entry_6.place(x=240,y=230)

label_4 = Label(root, text="parking_place ",width=20,bg="#008080", font=('Courier', 14),fg="Yellow")
label_4.place(x=40,y=280)

entry_5 = Entry(root,textvariable=C)
entry_5.place(x=240,y=280) 

label_4 = Label(root, text="Vehicle-type ",bg="#008080",width=20, font=('Courier', 14),fg="Yellow")
label_4.place(x=40,y=330)

entry_3 = Entry(root,textvariable=Vehicle_no)
entry_3.place(x=240,y=330)



Button(root, text='PROCEED',width=20,fg='white',bg='black',command=Proceed).place(x=180,y=380)
root.configure(background="#008080")
root.mainloop()
