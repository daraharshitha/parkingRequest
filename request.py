from tkinter import *
top=Tk()
def callback3():
    top.destroy()
    import parking_request
def callback4():
    top.destroy()
    import return_request
top.title("HOME PAGE")
Label(top,text="PARKING MANAGEMENT SYSTEM",font=("courier",16),fg="black",bg="yellow").place(x=15,y=40)
b3=Button(top,text="PARKING REQUEST",cursor="plus",relief=RAISED,width=23,height=3,fg="blue",command=callback3,activebackground="black",activeforeground="yellow").place(x=85,y=120)
b4=Button(top,text="RETURN REQUEST",cursor="plus",relief=RAISED,width=23,height=3,fg="blue",command=callback4,activebackground="black",activeforeground="yellow").place(x=85,y=250)
top.configure(background="violet")
top.geometry("360x400")
top.mainloop()




