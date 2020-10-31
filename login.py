from tkinter import *
import sqlite3
def Database():
    global conn, cursor
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    lbl_text.config(text="table doesnot exist",fg="red",bg="yellow",width="40", font=("Times",10,"bold italic"))
def Login(event=None):
    Database()
    if REG_NO.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please fill the all Fields", fg="red")
    else:
        cursor.execute("SELECT * FROM `signup` WHERE `reg_no` == ? AND `password` == ?", (REG_NO.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            REG_NO.set("")
            PASSWORD.set("")
        else:
            lbl_text.config(text="Invalid reg_no or password", fg="red")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
def HomeWindow():
    root.destroy()
    import request
    #creates next window
    #global Home
    #root.withdraw()
    #Home = Toplevel()
    #Home.title("car parking management")
    #width = 600
    #height = 500
    #screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()
    #x = (screen_width/2) - (width/2)
    #y = (screen_height/2) - (height/2)
    #root.resizable(0, 0)
    #Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #lbl_home = Label(Home, text="Successfully Login!", font=('time new roman', 20)).pack()
  #  btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
 

#Main Frame
root = Tk()
root.title("Parking management system")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
def Back():
    root.destroy()
    import home_page
#==============================VARIABLES======================================
REG_NO = StringVar()
PASSWORD = StringVar()
 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "Parking management system", font=('Arial', 15),bg="PeachPuff")
lbl_title.pack(fill=X)
lbl_reg_no = Label(Form, text = "Reg_no:", font=('Arial', 14), bd=15,fg="Blue")
lbl_reg_no.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('Arial', 14),fg="Blue",bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
reg_no = Entry(Form, textvariable=REG_NO, font=(14))
reg_no.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================

btn_back = Button(Form, text="Back", width=10, command=Back,bg="Red")
btn_back.grid(pady=20, row=3,columnspan=1)
btn_login = Button(Form, text="Login", width=10, command=Login,bg="LightGreen")
btn_login.grid(pady=20, row=3,columnspan=2)
btn_login.bind('<Return>', Login)

#functions

if __name__ == '__main__':
    root.mainloop()
