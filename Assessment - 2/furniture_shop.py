from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_10_30_tts",
            port="3310"
        )


def total_data():
    total = 0
    try:
        quantity = int(e_q.get())
        price = float(e_price.get())
        total = quantity * price

        e_total.delete(0,'end')
        e_total.insert(0,str(total))

    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for quantity and price")


def insert_data():
    if e_id.get()=="" or e_pname.get()=="" or e_q.get()=="" or e_price.get()=="" or e_total.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into product(id,product_name,quantity,price,total) values(%s,%s,%s,%s,%s)"
        args = (e_id.get(),e_pname.get(),e_q.get(),e_price.get(),e_total.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_q.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully!!!")


def search_data():
    e_pname.delete(0,'end')
    e_q.delete(0,'end')
    e_price.delete(0,'end')
    e_total.delete(0,'end')


    if e_id.get()=="":
        msg.showinfo("Search Status","ID Is Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from product where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_pname.insert(0,row[0][1])
            e_q.insert(0,row[0][2])
            e_price.insert(0,row[0][3])
            e_total.insert(0,row[0][4])

        else:
            msg.showinfo("Search Status","ID Not Found")
        conn.close()


def update_data():
    if e_id.get()=="" or e_pname.get()=="" or e_q.get()=="" or e_price.get()=="" or e_total.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")

    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "update product set pname=%s, q=%s, price=%s, total=%s where id=%s"
        args = (e_pname.get(),e_q.get(),e_price.get(),e_total.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_q.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully!!!")


def delete_data():

    if e_id.get()=="":
        msg.showinfo("Delete Status","ID Is Mandatory")

    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from product where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_q.delete(0,'end')
        e_price.delete(0,'end')
        e_total.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully!!!")



root = Tk()
root.geometry("500x500")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_pname = Label(root,text="PRODUCT NAME")
l_pname.place(x=50,y=100)

l_q = Label(root,text="QUANTITY")
l_q.place(x=50,y=150)

l_price = Label(root,text="PRICE")
l_price.place(x=50,y=200)

l_total = Label(root,text="TOTAL")
l_total.place(x=50,y=250)

e_id = Entry(root)
e_id.place(x=150, y=50)

e_pname = Entry(root)
e_pname.place(x=150, y=100)

e_q = Entry(root)
e_q.place(x=150, y=150)

e_price = Entry(root)
e_price.place(x=150, y=200)

e_total = Entry(root)
e_total.place(x=150, y=250)

l_info = Label(root,text="Product Info.")
l_info.place(x=350,y=50)

l_info = Label(root,text="1.Chair")
l_info.place(x=350,y=80)

l_info = Label(root,text="2.Table")
l_info.place(x=350,y=105)

l_info = Label(root,text="3.Sofa")
l_info.place(x=350,y=130)

l_info = Label(root,text="4.Bed")
l_info.place(x=350,y=155)

l_info = Label(root,text="5.Wardrobe")
l_info.place(x=350,y=180)

insert = Button(root, text="INSERT", bg="black", fg="white", font=("Arial",12), command=insert_data)
insert.place(x=20,y=365)

search = Button(root, text="SEARCH", bg="black", fg="white", font=("Arial",12),command=search_data)
search.place(x=90,y=365)

update = Button(root, text="UPDATE", bg="black", fg="white", font=("Arial",12),command=update_data)
update.place(x=171,y=365)

delete = Button(root, text="DELETE", bg="black", fg="white", font=("Arial",12),command=delete_data)
delete.place(x=250,y=365)

total = Button(root, text="TOTAL", bg="black", fg="white", font=("Arial",12), command=total_data)
total.place(x=171,y=300)

root.mainloop()





