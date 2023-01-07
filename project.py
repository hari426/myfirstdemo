from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

def insert():
    id=e_id.get()
    std_name=e_std_name.get()
    course=e_course.get()
    if(id=="" or std_name=="" or course==""):
        MessageBox.showinfo("insert status","All Fields are required")
    else:
        con=mysql.connect(host='localhost',user='root',password='amma@143',database='abc')
        cursor=con.cursor()
        cursor.execute("insert into student values('"+ id +"','"+ std_name +"','"+ course + "')")
        cursor.execute("commit")
        e_id.delete(0,'end')
        e_std_name.delete(0,'end')
        e_course.delete(0,'end')
        show()

        MessageBox.showinfo("insert status","inserted successfully")
        con.close()

def delete():
        if(e_id.get() == ""):
            MessageBox.showinfo("Delete Status","ID is compolsary for delete")
        else:
            con = mysql.connect(host='localhost', user='root', password='amma@143', database='abc')
            cursor = con.cursor()
            cursor.execute("delete from student where id='"+e_id.get()+"'")
            cursor.execute("commit")
            e_id.delete(0, 'end')
            e_std_name.delete(0, 'end')
            e_course.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete status", "Delete successfully")
            con.close()

def update():
    id=e_id.get()
    std_name=e_std_name.get()
    course=e_course.get()
    if(id=="" or std_name=="" or course==""):
        MessageBox.showinfo("update status","All Fields are required")
    else:
        con=mysql.connect(host='localhost',user='root',password='amma@143',database='abc')
        cursor=con.cursor()
        cursor.execute("update  student set  std_name='"+ std_name +"',course='"+ course +"'where id='"+ id + "'")
        cursor.execute("commit")
        e_id.delete(0,'end')
        e_std_name.delete(0,'end')
        e_course.delete(0,'end')
        show()

        MessageBox.showinfo("update status","updated successfully")
        con.close()

def get():
        if (e_id.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connect(host='localhost', user='root', password='amma@143', database='abc')
            cursor = con.cursor()
            cursor.execute("select * from student where id='" + e_id.get() + "'")
            rows=cursor.fetchall()

            for row in rows:

               e_std_name.insert(0, row[1])
               e_course.insert(0, row[2])

            con.close()
def show():
   con = mysql.connect(host='localhost', user='root', password='amma@143', database='abc')
   cursor = con.cursor()
   cursor.execute("select * from student ")
   rows=cursor.fetchall()
   list.delete(0, list.size())

   for row in rows:
                insertdata= str(row[0])+ '            '+row[1]
                list.insert(list.size()+1, insertdata)

   con.close()

root=Tk()
root.geometry('600x300')
root.title('python_tkinter')

id=Label(root,text='ID',font=('Bold',10),fg='black')
id.place(x=20,y=50)
std_name=Label(root,text='STD_NAME',font=('Bold',10),fg='black')
std_name.place(x=20,y=90)
course=Label(root,text='COURSE',font=('Bold',10),fg='black')
course.place(x=20,y=130)

e_id=Entry()
e_id.place(x=150,y=50)
e_std_name=Entry()
e_std_name.place(x=150,y=90)
e_course=Entry()
e_course.place(x=150,y=130)

insert=Button(root,text='insert',font=('bold',10),fg='black',bg='blue',command=insert)
insert.place(x=20,y=180)
delete=Button(root,text='delete',font=('bold',10),fg='black',bg='red',command=delete)
delete.place(x=80,y=180)
update=Button(root,text='update',font=('bold',10),fg='black',bg='green',command=update)
update.place(x=140,y=180)
get=Button(root,text='get',font=('bold',10),fg='black',bg='brown',command=get)
get.place(x=200,y=180)

list=Listbox(root,width=200,height=300)

list.place(x=40,y=250)
show()
root.mainloop()
