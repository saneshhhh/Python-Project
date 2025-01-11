from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import mysql.connector
import requests, json
import matplotlib.pyplot as plt
import pandas as pd
import geocoder
import re

root = Tk()
root.title("E. M. S ")
root.geometry("800x800+50+50")
f = ("Arial", 30, "bold")
root.configure(bg="dark sea green")


g = geocoder.ip('me')
loc_label = Label(root,text="Location: " + str(g.city),font = f,bg="dark sea green")
loc_label.place(x=120,y=650)
loca = (g.city)

a1 = "https://api.openweathermap.org/data/2.5/weather"
a2 = "?q=" + (loca)
a3 = "&appid=" + "c5a8bc22207011ad41486c60c1c83357"
a4 = "&units=" + "metric"
wa = a1 + a2 + a3 + a4
res= requests.get(wa)
data = res.json()
tem = data ["main"]["temp"]

temp_label = Label(root,text="Temp: " + str(tem) ,font=f,bg="dark sea green")
temp_label.place(x=510,y=650)

def f1() :
	root.withdraw()
	aw.deiconify()

def f2() :
	aw.withdraw()
	root.deiconify()

def f3() :
	root.withdraw()
	vw.deiconify()
	vw_emp_data.delete(1.0, END)
	con = None
	try :
		con = mysql.connector.connect(host="localhost",user="root",	password="abc123",database="emp_mng_sys")
		cursor = con.cursor()
		sql = "select * from emp order by id"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data :
			info = info + " id = " +str(d[0]) + " name = " +str(d[1]) + " salary = " +str(d[2]) + "\n" + "*********************************************" +"\n"
		vw_emp_data.insert(INSERT, info)
	except Exception as e :
		showerror("issue ", e)
	finally :
		if con is not None :
			con.close()

def f4() :
	vw.withdraw()
	root.deiconify()

def f5():
	
	def validate_id(id):
		pattern = re.compile("^[0-9]+$")
		if not pattern.match(str(id)):
			return False
		if int(id) <= 0:
			return False
		return True

	def validate_name(name):
		pattern = re.compile("^[a-zA-Z]+$")
		if not pattern.match(name):	 
			return False
		return True 

	def validate_salary(salary):
		pattern = re.compile("^[1-9][0-9]*$")
		if not pattern.match(str(salary)):
			return False
		salary_int = int(salary)
		if salary_int <= 5000:
			return False
		return True


	con = None
	try:
		con = mysql.connector.connect(host="localhost",user="root",	password="abc123",database="emp_mng_sys")
		id = (aw_ent_id.get())
		if not validate_id(id) :
			showerror("ERROR","Only positive integers allowed for ID")
			return
		name = aw_ent_name.get()
		if not validate_name(name):
			showerror("ERROR","2 or more alphabets only allowed for Name")
			return
		salary = (aw_ent_salary.get())
		if not validate_salary(salary):
			showerror("ERROR","Salary should be in positive num and above 5000")
			return
		cursor = con.cursor()
		sql = "INSERT INTO emp (id, name, salary) VALUES (%s,%s,%s)"
		cursor.execute(sql, (id, name, salary))
		con.commit()
		showinfo("success", "record created")
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()

def f6() :
	answer = askyesno(title = 'confirmation', message = "Are you sure to exit ?")
	if answer :
			root.destroy()
root.protocol("WM_DELETE_WINDOW", f6)

def f7() :
	root.withdraw()
	uw.deiconify()

def f8() :
	uw.withdraw()
	root.deiconify()

def f9(): 

	def validate_id(id):
		pattern = re.compile("^[0-9]+$")
		if not pattern.match(str(id)):
			return False
		if int(id) <= 0:
			return False
		return True

	def validate_name(name):
		pattern = re.compile("^[a-zA-Z]+$")
		if not pattern.match(name):	 
			return False
		return True 

	def validate_salary(salary):
		pattern = re.compile("^[1-9][0-9]*$")
		if not pattern.match(str(salary)):
			return False
		salary_int = int(salary)
		if salary_int <= 5000:
			return False
		return True


	con = None
	try:
		con = mysql.connector.connect(host="localhost",user="root",	password="abc123",database="emp_mng_sys")
		id = (uw_ent_id.get())
		if not validate_id(id) :
			showerror("ERROR","Only positive integers allowed for ID")
			return
		name = uw_ent_name.get()
		if not validate_name(name):
			showerror("ERROR","Only alphabets allowed for Name")
			return
		salary = (uw_ent_salary.get())
		if not validate_salary(salary):
			showerror("ERROR","Salary should be positive num and above 5000")
			return
		cursor = con.cursor()
		cursor.execute("SELECT * FROM emp WHERE id=%s", (id,))
		if cursor.fetchone() is None:
			showerror("Error", "Invalid ID")
		else:
			cursor.execute("update emp set name=%s,salary=%s where id = %s", (name, salary, id))
			con.commit()
			showinfo("success","record updated")
	except Exception as e :
		con.rollback()
		showerror("Issue",e)
	finally :
		if con is not None :
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()


def f10() :
	root.withdraw()
	dw.deiconify()

def f11() :
	dw.withdraw()
	root.deiconify()

def f12() :

	def validate_id(id):
		pattern = re.compile("^[0-9]+$")
		if not pattern.match(str(id)):
			return False
		if int(id) <= 0:
			return False
		return True

	con = None
	try:
		con = mysql.connector.connect(host="localhost",user="root",	password="abc123",database="emp_mng_sys")
		id = (dw_ent_id.get())
		if not validate_id(id) :
			showerror("ERROR","Only positive integers allowed for ID")
			return
		cursor = con.cursor()
		sql = "SELECT * FROM emp WHERE id = %s"
		cursor.execute(sql, (id,))
		data = cursor.fetchall()
		if len(data) == 0:
			showerror("ERROR","Record not found for given ID")
			return
		sql = "DELETE FROM emp WHERE id = %s"
		cursor.execute(sql, (id,))
		con.commit()
		showinfo("success", "record deleted")
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()

def f13() :
	root.withdraw()
	cw.deiconify()

def f14() :
	con = mysql.connector.connect(host="localhost",user="root",	password="abc123",database="emp_mng_sys")
	cursor = con.cursor()
	sql = "SELECT name, salary FROM emp order by salary desc limit 5"
	cursor.execute(sql)
	results = cursor.fetchall()
	df = pd.DataFrame(results, columns=["name", "salary"])
	plt.bar(df["name"], df["salary"], color="darkblue")
	plt.xlabel("Name")
	plt.ylabel("Salary")
	plt.title("Top 5 Earners")
	plt.show()


def f15() :
	cw.withdraw()
	root.deiconify()

btn_add = Button(root, text="Add Emp", font=f, width = 15, command= f1)
btn_add.pack(pady=20)
btn_view =  Button(root,text = "View Emp", font = f, width = 15, command = f3)
btn_view.pack(pady=20)
btn_update = Button(root, text="Update Emp", font=f, width = 15, command= f7)
btn_update.pack(pady=20)
btn_delete = Button(root, text="Delete Emp", font=f, width = 15, command= f10)
btn_delete.pack(pady=20)
btn_chart = Button(root, text="Chart", font=f, width = 15, command= f13)
btn_chart.pack(pady=20)

#add
aw = Toplevel(root)
aw.title("Add Emp")
aw.geometry("800x800+50+50")
aw.configure(bg="LavenderBlush3")

aw_lab_id = Label(aw, text = "enter id", font = f,bg="LavenderBlush3")
aw_ent_id = Entry(aw, font=f, bd = 2)
aw_lab_name = Label(aw, text = "enter name", font = f,bg="LavenderBlush3")
aw_ent_name = Entry(aw, font=f, bd = 2)
aw_lab_salary = Label(aw, text = "enter salary", font = f,bg="LavenderBlush3")
aw_ent_salary = Entry(aw, font=f, bd = 2)
aw_btn_save = Button(aw, text = "Save", font = f, command = f5)
aw_btn_back = Button(aw, text = "Back", font = f, command = f2)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)

aw.withdraw()

#view
vw = Toplevel(root)
vw.title("View Emp")
vw.geometry("800x800+50+50")
vw.configure(bg="Lightsteelblue")

vw_emp_data = ScrolledText(vw, width=60, height=15, font = f, bg="light gray")
vw_btn_back = Button(vw, text = "Back", font = f, command = f4)
vw_emp_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

#update
uw = Toplevel(root)
uw.title("Update Emp")
uw.geometry("800x800+50+50")
uw.configure(bg="LightBlue1")


uw_lab_id = Label(uw, text = "enter id", font = f,bg="LightBlue1")
uw_ent_id = Entry(uw, font=f, bd = 2)
uw_lab_name = Label(uw, text = "enter name", font = f,bg="LightBlue1")
uw_ent_name = Entry(uw, font=f, bd = 2)
uw_lab_salary = Label(uw, text = "enter salary", font = f,bg="LightBlue1")
uw_ent_salary = Entry(uw, font=f, bd = 2)
uw_btn_save = Button(uw, text = "Save", font = f, command = f9)
uw_btn_back = Button(uw, text = "Back", font = f, command = f8)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()



# delete
dw = Toplevel(root)
dw.title("Delete Emp")
dw.geometry("500x600+50+50")
dw.configure(bg="lightyellow")


dw_lab_id = Label(dw, text = "Enter id", font = f,bg="lightyellow")
dw_ent_id = Entry(dw, font=f, bd = 2)
dw_btn_delete = Button(dw, text = "Delete", font = f, command = f12)
dw_btn_back = Button(dw, text = "Back", font = f, command = f11)

dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_delete.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()


# chart
cw = Toplevel(root)
cw.title("Top Earners")
cw.geometry("600x700+50+50")
cw.configure(bg="pink1")

cw_btn_create = Button(cw,text="Create Bar Chart",font=f,command = f14)
cw_btn_create.pack(pady =50)
cw_btn_back = Button(cw, text = "Back", font = f, command = f15)
cw_btn_back.pack(pady=10)
cw.withdraw()

root.mainloop()