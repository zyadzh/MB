from msilib.schema import ComboBox
from pickle import FRAME
from sqlite3 import Row
from struct import calcsize
from tkinter import *
from tkinter import ttk
from turtle import width
from db import Database
from tkinter import messagebox

db = Database("employees.db")






root = Tk()
root.title("MES")
root.geometry('1240x615+0+0')
root.resizable(False,False)
root.configure(bg='#2c3e50')

name=StringVar()
age=StringVar()
jop=StringVar()
gender=StringVar()
email=StringVar()
mobile=StringVar()


logo=PhotoImage(file='')
lbllogo=Label(root,image=logo,bg='#2c3e50')
lbllogo.place(x=80,y=520)



#====== Entries Frame 
entries_frame = Frame(root,bg ='#2c3e50')
entries_frame.place( x = 1 , y = 1 ,width=360,height=510)
title = Label(entries_frame , text='employee company',font=('Calibri',18,'bold'),bg='#2c3e50',fg='white')
title.place(x=10,y=1)

lblName= Label(entries_frame,text='name',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblName.place(x=10,y=50)
txtName=Entry(entries_frame,textvariable=name,width=20,font=('Calibri',16,))
txtName.place(x=120,y=50)

lblJop= Label(entries_frame,text='jop',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblJop.place(x=10,y=90)
txtJop=Entry(entries_frame,textvariable=jop,width=20,font=('Calibri',16,))
txtJop.place(x=120,y=90)

lblGender= Label(entries_frame,text='gender',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblGender.place(x=10,y=130)
comboGender= ttk.Combobox(entries_frame,textvariable=gender,state='readonly',width=18,font=('Calibri',16,))
comboGender['values'] = ('Male', 'Fmale')
comboGender.place(x=120,y=130)

lblAge= Label(entries_frame,text='age',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblAge.place(x=10,y=170)
txtAge=Entry(entries_frame,textvariable=age,width=20,font=('Calibri',16,))
txtAge.place(x=120,y=170)

lblEmail= Label(entries_frame,text='Email',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblEmail.place(x=10,y=210)
txtEmail=Entry(entries_frame,textvariable=email,width=20,font=('Calibri',16,))
txtEmail.place(x=120,y=210)

lblContact= Label(entries_frame,text='Mobile',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblContact.place(x=10,y=250)
txtContact=Entry(entries_frame,textvariable=mobile,width=20,font=('Calibri',16,))
txtContact.place(x=120,y=250)

lblAddress= Label(entries_frame,text='Address :',font=('Calibri',16,),bg='#2c3e50',fg='white')
lblAddress.place(x=10,y=290)
txtAddress=Text(entries_frame,width=30,height=2,font=('Calibri',16,))
txtAddress.place(x=10,y=330) 

#--------Define------------
def hide():
    root.geometry("375x515+0+0")

def show():
    root.geometry("1240x615+0+0")

btnhide=Button(entries_frame,text='HIDE',bg="white",bd=1,cursor='hand2', command=hide)
btnhide.place(x=270,y=10)
btnshow=Button(entries_frame,text='SHOW',bg="white",bd=1,cursor='hand2',command=show)
btnshow.place(x=310,y=10)


def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2]),
    jop.set(row[3]),
    email.set(row[4]),
    gender.set(row[5]),
    mobile.set(row[6]),
    txtAddress.delete(1.0,END),
    txtAddress.insert(END,row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)



def Add_Employe():
    if txtName.get()=="" or txtAge.get()=="" or txtJop.get()=="" or txtEmail.get()=="" or txtContact.get()=="" or comboGender.get()==""or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","please fill all the entry")
        return
    db.insert(
        txtName.get(),
        txtAge.get(),
        txtJop.get(),
        txtEmail.get(),
        txtContact.get(),
        comboGender.get(),
        txtAddress.get(1.0,END)
    )
    messagebox.showinfo("success" ,"A dded new employee")
    clear()
    displayAll()

def update():
    if txtName.get()=="" or txtAge.get()=="" or txtJop.get()=="" or txtEmail.get()=="" or txtContact.get()=="" or comboGender.get()==""or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","please fill all the entry")
        return
    db.update(row[0],
        txtName.get(),
        txtAge.get(),
        txtJop.get(),
        txtEmail.get(),
        txtContact.get(),
        comboGender.get(),
        txtAddress.get(1.0,END))
    messagebox.showinfo("Success","the employee data is update")
    clear()
    displayAll()


def clear():
    name.set("")
    jop.set("")
    age.set("")
    email.set("")
    mobile.set("")
    gender.set("")
    txtAddress.delete(1.0,END)


def Delete():
    db.remove(row[0])
    clear()
    displayAll()










#--------    buttons frame   ----------


btn_frame=Frame(entries_frame,bg='#2c3e50',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btnADD=Button(btn_frame,
                        text='Add Details',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#16a085',
                        bd=0,
                        cursor='hand2',
                        command=Add_Employe
                        ).place(x=4,y=5)


btnEdite=Button(btn_frame,
                        text='Update Details',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#2980b9',
                        bd=0,
                        cursor='hand2',
                        command=update
                        ).place(x=4,y=50)



btnDelete=Button(btn_frame,
                        text='Delete Details',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#c0392b',
                        bd=0,
                        cursor='hand2',
                        command=Delete
                        ).place(x=170,y=5)


btnClear=Button(btn_frame,
                        text='Clear Details',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#f39c12',
                        bd=0,
                        cursor='hand2',
                        command=clear
                        ).place(x=170,y=50)




#------- Table ------

tree_frame=Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=610)

style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13,),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13,))


tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8,),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="40")
tv.heading("2",text="Name")
tv.column("2",width="140")
tv.heading("3",text="Age")
tv.column("3",width="50")
tv.heading("4",text="Jop")
tv.column("4",width="120")
tv.heading("5",text="Email")
tv.column("5",width="160")
tv.heading("6",text="Gender")
tv.column("6",width="90")
tv.heading("7",text="Mobile")
tv.column("7",width="150")
tv.heading("8",text="Address")
tv.column("8",width="150")
tv['show'] ='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=1,height=610,width=875)

displayAll()



root.mainloop()
