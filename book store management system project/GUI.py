#only maindashboard

from tkinter import * 
from tkinter import messagebox
from tkinter import simpledialog
import csv
from tkinter import ttk

a=Tk()
a.title("Book Store Management System")
#defination of the options
def hide():
    b1.configure(font=("aril",9))
    b2.configure(font=("aril",9))
    b3.configure(font=("aril",9))
    b4.configure(font=("aril",9))
    b5.configure(font=("aril",9))
a.iconbitmap("icon.ico")


def indicator(ind):
    hide()
    ind.configure(font=("aril",9,"italic","bold"))

def delete():
    for frame in mfr.winfo_children():
        frame.destroy()

###########for options

def blist(n):
    delete()
    frr=Frame(mfr,width=500,height=500,bg="white")
    Label(frr,text="Book List",font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
    Frame(frr,height=2,width=500).place(x=0,y=35)
    frr.pack()
    frm=Frame(frr)
    frm.place(x=32,y=80)
    sc1=Scrollbar(frm,orient=VERTICAL)
    sc2=Scrollbar(frm,orient=HORIZONTAL)
    my_tree=ttk.Treeview(frm,yscrollcommand=sc1.set,xscrollcommand=sc2.set)
    sc1.config(command=my_tree.yview)
    sc1.pack(side=RIGHT,fill=Y)

    sc2.config(command=my_tree.xview)
    sc2.pack(side=BOTTOM,fill=X)


    #Define Our Column.
    my_tree['column']=("Book Name","Author","Price")
    # formate columns
    my_tree.column("#0",width=0,minwidth=0)
    my_tree.column("Book Name",anchor=W,width=210)
    my_tree.column("Author",anchor=CENTER,width=160)
    my_tree.column("Price",anchor=W,width=60)

    #creating heading
    my_tree.heading("#0",text="Label",anchor=W)
    my_tree.heading("Book Name",text="Book Name",anchor=W)
    my_tree.heading("Author",text="Author",anchor=CENTER)
    my_tree.heading("Price",text="Price",anchor=W)
    my_tree.pack(side=LEFT)
    #add data

    fo=open('bookdata.txt','r')
    dat=fo.readlines()
    n11=0
    for i in dat:
        x=i.split("#")
        my_tree.insert(parent='',index='end',iid=str(n11),text="P",values=(x[0],x[1],x[2]))
        n11+=1
    fo.close()
    indicator(n)


def pb(n):
    delete()
    frr=Frame(mfr,width=500,height=500,bg="white")
    Label(frr,text="Purchase Book",font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
    Frame(frr,height=2,width=500).place(x=0,y=35)
    frr.pack()
    Label(frr,bg="white",text="Enter Name Of Book You Want To Purchase: ").place(x=60,y=75)
    e1=Entry(frr,width=50,bg="light grey",border=1)
    e1.place(x=60,y=100)
    def chk():
        fo=open("bookdata.txt","r")
        da=fo.readlines()
        ex=0
        v=''
        for i in da:
            x=i.split("#")
            if x[0]==e1.get():
                tx.insert(END,"Book Name : "+x[0]+"\nAuthor : "+x[1]+"\nPrice : "+x[2]+"\n"+"-"*500)
                v=x[0]
        return v
    Button(frr,text="-> Ok",width=12,bg="#681B99",fg="white",border=0,command=chk).place(y=98,x=380)
    global tx
    tx=Text(frr,height=8,width=40,border=2,relief=GROOVE,font=12)
    tx.place(x=60,y=130)
    def purchase():
        if e1.get()=='':
            messagebox.showinfo("","Please Fill Required Data")
        elif e1.get()==str(chk()):
            messagebox.showinfo("","Purchased Sucessfully")
        else:
            messagebox.showinfo("","Purchase Failed \ninvalid book name")
    Button(frr,text="Buy",bg="#681B99",fg="white",width=18,border=0,command=purchase).place(x=60,y=300)



def eb(n):
    delete()
    frr=Frame(mfr,width=500,height=500,bg="white")

    Label(frr,text="Book Name:",bg="white",fg="grey").place(x=35,y=80)
    Label(frr,text="Author:",bg="white",fg="grey").place(x=35,y=150)
    Label(frr,text="Price:",bg="white",fg="grey").place(x=35,y=220)


    e1_add=Entry(frr,bg="light grey",relief=SUNKEN,borderwidth=2,fg="black",font=("arial",12),border=0,width=34)
    e1_add.place(x=35,y=100)

    e2_add=Entry(frr,bg="light grey",relief=SUNKEN,borderwidth=2,fg="black",font=("arial",12),border=0,width=34)
    e2_add.place(x=35,y=170)

    e3_add=Entry(frr,bg="light grey",relief=SUNKEN,borderwidth=2,fg="black",font=("arial",12),border=0,width=34)
    e3_add.place(x=35,y=240)
    e3_add.insert(0,"Rs ")


    def addbook():
        a=str(e1_add.get())+"#"
        b=str(e2_add.get())+"#"
        c=str(e3_add.get())+"#"
        x=str(a+b+c+"\n")
        if a=="" or b=="" or c=="":
            messagebox.showerror("status","Do not left any information")
        else:
            with open("bookdata.txt","a") as f:
                f.write(x)

            messagebox.showinfo("","record added sucessfully")
            e1_add.delete(0,END)
            e2_add.delete(0,END)
            e3_add.delete(0,END)
            e3_add.insert(0,"Rs ")


    Button(frr,text="Add Book",bg="#681B99",border=0,activebackground="#249BFF",fg="white",activeforeground="white",width=12,command=addbook).place(x=35,y=300)

    Label(frr,text="Add Books",font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
    Frame(frr,height=2,width=500).place(x=0,y=35)
    frr.pack()
    indicator(n)

def rb(n):
    delete()
    frr=Frame(mfr,width=500,height=500,bg="white")
    Label(frr,text="Remove Book From List",font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
    Frame(frr,height=2,width=500).place(x=0,y=35)
    frr.pack()
    Label(frr,fg="grey",text="Enter Book Name: ",bg="white").place(x=100,y=130)
    e1=Entry(frr,width=30,border=0,bg="light grey",fg="black",font=12)
    e1.place(x=100,y=150)
    def searchbook():
        sb_f=open('bookdata.txt','r')
        data=sb_f.readlines()
        temp=0
        for i in data:
            x=i.split("#")
            if x[0]==str(e1.get()):
                temp+=1
        if temp==0:
            messagebox.showerror("","No Data Found")
        else:
            m=messagebox.askquestion("","confirm to delete")
            if m=="yes":
                foj=open("bookdata.txt","r")
                dataa=foj.readlines()
                lst_foj=[]
                for i in dataa:
                    z=i.split("#")
                    if z[0]==str(e1.get()):
                        pass
                    else:
                        lst_foj.append(z[0]+"#"+z[1]+"#"+z[2]+"#"+"\n")
                upd=open("bookdata.txt","w")
                upd.writelines(lst_foj)
                upd.close()
                messagebox.showinfo("","bookdata deleted sucessfully")
    Button(frr,bg="#681B99",text="Search",border=0,fg="white",width=12,command=searchbook).place(x=100,y=200)





    indicator(n)

def ab(n):
    delete()
    frr=Frame(mfr,width=500,height=500,bg="white")
    Label(frr,text="About Us",font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
    Frame(frr,height=2,width=500).place(x=0,y=35)
    Label(mfr,text="Book Store",fg="#5C5C5C",font=("",15),bg="white").place(x=30,y=60)
    Label(mfr,text="Management System",fg="#6A1B9A",font=("",20),bg="white").place(x=30,y=82)
    Label(mfr,text="Submitted To: ",fg="#BA68C8",font=("",12),bg="white").place(x=30,y=150)
    Label(mfr,text="Jaideep Kumar Sir ",fg="#681B99",font=("",14),bg="white").place(x=30,y=170)
    Label(mfr,text="Submitted By: ",fg="#BA68C8",font=("",12),bg="white").place(x=30,y=220)
    Label(mfr,text="Pranit Modanwal ",fg="#681B99",font=("",14),bg="white").place(x=30,y=240) 

    Label(mfr,text="Class: 12th A3 ",fg="#681B99",font=("",10),bg="white").place(x=30,y=265)
    Label(mfr,text="Roll No: 10 ",fg="#681B99",font=("",10),bg="white").place(x=30,y=285)


    frr.pack()
    indicator(n)

fr=Frame(a,bg="#4A148C")
im7=PhotoImage(file="shop.png")
Label(fr,image=im7,font=("arial",12,"bold"),bg="#4A148C",fg="white").pack(pady=7)
hr=Frame(fr,width=100,height=2,bg="#220B3F").pack(pady=5)

im1=PhotoImage(file="options1.png")
im2=PhotoImage(file="options2.png")
im3=PhotoImage(file="options3.png")
im4=PhotoImage(file="options4.png")
im5=PhotoImage(file="options5.png")
b1=Button(fr,image=im5,border=0,bg="#4A148C",activebackground="#4A148C",command=lambda:blist(b1))
b1.pack(fill=X,pady=5)
b2=Button(fr,image=im4,bg="#4A148C",border=0,activebackground="#4A148C",fg="white",activeforeground="white",command=lambda:pb(b2),font=("aril",9))
b2.pack(fill=X,pady=5)
b3=Button(fr,image=im3,bg="#4A148C",border=0,activebackground="#4A148C",fg="white",activeforeground="white",command=lambda:eb(b3),font=("aril",9))
b3.pack(fill=X,pady=5)
b4=Button(fr,image=im2,bg="#4A148C",border=0,activebackground="#4A148C",fg="white",activeforeground="white",command=lambda:rb(b4),font=("aril",9))
b4.pack(fill=X,pady=5)
b5=Button(fr,image=im1,bg="#4A148C",border=0,activebackground="#4A148C",fg="white",activeforeground="white",command=lambda:ab(b5),font=("aril",9))
b5.pack(fill=X,pady=5)

Button(fr,text="Close",command=quit,fg="white",bg="#34115E",border=0).pack(side=BOTTOM,fill=X)

fr.pack(side=LEFT)
fr.pack_propagate(False)
fr.configure(width=100,height=400)

mfr=Frame(a,bg="white")

#file object for csv.

f=open("users.csv","r")
fr=csv.reader(f)
data=[]
for i in fr:
    for j in i:
        data.append(j)
print(data[0])


Label(mfr,text="Hi,"+str(data[0]),font=("arial",15,"bold"),bg="white",fg="grey").place(x=35,y=10)
Frame(mfr,height=2,width=500).place(x=0,y=35)

Label(mfr,text="Choose Your Options\nFrom Left Side",font=("arial",12),bg="white",fg="#34115E").place(x=170,y=150)

mfr.pack(side=LEFT)

mfr.pack_propagate(False)
mfr.configure(height=400,width=500)


a.geometry('600x400')
a.configure(bg="white")
a.resizable(height=False,width=False)
a.mainloop()