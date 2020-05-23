from tkinter import *
from tkinter import messagebox
import os
import subprocess
import webbrowser


objects = []
window = Tk()
window.title("Password Storage")
window.withdraw()
appicon = PhotoImage(file="icons/appicon.png")
window.iconphoto(True, appicon)

class popupWindow(object):

	def __init__(self, master):
		top = self.top = Toplevel(master)
		top.title("Input Password")
		top.geometry("{}x{}".format(250, 100))
		self.l = Label(top, text="Password: ", font=("Meera", 14, "bold"))
		self.l.pack()
		self.e = Entry(top, width=50)
		self.e.pack()
		self.b = Button(top, text="Submit", command=self.clear, font=("Meera", 14, "bold"))
		self.b.pack()
		self.e.bind("<Return>", self.clear)

	def clear(self, *args):
		self.value = self.e.get()
		#Type in a password of your choice between the quotes. When you start the script, it will ask you for the password. Encrypt this script in order to hide the password.
		access = ""

		if self.value == access:
			messagebox.showinfo("Password Storage", "Correct password. You're logged in.")
			self.top.destroy()
			window.deiconify()
			

		else:
			messagebox.showerror("Password Storage", "Incorrect password. Try again...")

class entity_add:
	def __init__(self, master, n, p, e):
		self.passwd = p
		self.website = n
		self.email = e
		self.window = master

	def write(self):
		f = open("emails.txt", "a")
		n = self.website
		e = self.email
		p = self.passwd

		encryptedN = ""
		encryptedE = ""
		encryptedP = ""
		for letter in n:
			if letter == " ":
				encrytedN += " "
			else:
				encryptedN += chr(ord(letter) + 5)

		for letter in e:
			if letter == " ":
				encryptedE += " "
			else:
				encryptedE += chr(ord(letter) + 5)
		for letter in p:
			if letter == " ":
				encryptedP += chr(ord(letter) + 5)
			else:
				encryptedP += chr(ord(letter) + 5)
		f.write(encryptedN + "," + encryptedE + "," + encryptedP + ", \n")

class entity_display:
	def __init__(self, master, n, p, e, i):
		self.passwd = p
		self.website = n
		self.email = e
		self.window = master
		self.i = i

		decryptedN = ""
		decryptedE = ""
		decryptedP = ""

		for letter in self.website:
			if letter == " ":
				decryptedN += " "
			else:
				decryptedN += chr(ord(letter) - 5)

		for letter in self.passwd:
			if letter == " ":
				decryptedP += " "
			else:
				decryptedP += chr(ord(letter) - 5)

		for letter in self.email:
			if letter == " ":
				decryptedE += " "
			else:
				decryptedE += chr(ord(letter) - 5)

		self.label_website = Label(self.window, text=decryptedN, font=("Meera", 14, "bold"))
		self.label_passwd = Label(self.window, text=decryptedE, font=("Meera", 14, "bold"))
		self.label_email = Label(self.window, text=decryptedP, font=("Meera", 14, "bold"))
		self.deletebutton = Button(self.window, text="X", fg="red", command=self.delete)

	def display(self):
		self.label_website.grid(row=6 + self.i, sticky=W)
		self.label_email.grid(row=6 + self.i, column=1)
		self.label_passwd.grid(row=6 + self.i, column=2, sticky=E)
		self.deletebutton.grid(row=6 + self.i, column=3, sticky=E)

	def delete(self):
		answer = messagebox.askquestion("Delete", "Are you sure you want to delete this entry?")

		if answer == "yes":
			for i in objects:
				i.destroy()
			
			f = open("emails.txt", "r")
			lines = f.readlines()
			f.close()

			f = open("emails.txt", "w")
			count = 0

			for line in lines:
				if count != self.i:
					f.write(line)
					count += 1
				
			f.close()
			readfile()

	def destroy(self):
		self.label_website.destroy()
		self.label_email.destroy()
		self.label_passwd.destroy()
		self.deletebutton.destroy()

def closeapp(*args):
	window.destroy()

def onsubmit(*args):
	m = email.get()
	p = passwd.get()
	n = website.get()
	e = entity_add(window, n, p, m)
	e.write()
	website.delete(0, 	END)
	email.delete(0, END)
	passwd.delete(0, END)
	messagebox.showinfo("Success", "Successfully Added, \n" + "Website: " + n + "\nEmail: " + m + "\nPassword: " + p)
	readfile()

def clearfile():
	f = open("emails.txt", "w")

def readfile():
	f = open("emails.txt", "r")
	count = 0

	for line in f:
		entityList = line.split(",")
		e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
		objects.append(e)
		e.display()
		count += 1
	f.close()

def about(*args):
	top = Toplevel()
	abouttext = Label(top, text="This was coded by sketchyboi14 in python. To report issues, go to the issues section of the github project")
	abouttext.grid()
	githubiconbtn = Button(top, image=githubicon, command=open_github, relief="flat")
	githubiconbtn.grid()


def open_github():
	webbrowser.open_new("https://github.com/sketchyboi14")

m = popupWindow(window)

closeicon = PhotoImage(file="icons/closeicon.png")
githubicon = PhotoImage(file="icons/githubicon.png")
infoicon = PhotoImage(file="icons/infoicon.png")

entity_label = Label(window, text="Add Info", font=("Meera", 18, "bold"))
website_label = Label(window, text="Website: ", font=("Meera", 14, "bold"))
email_label = Label(window, text="Email: ", font=("Meera", 14, "bold"))
passwd_label = Label(window, text="Password: ", font=("Meera", 14, "bold"))
website = Entry(window, font=("Meera", 14, "bold"))
email = Entry(window, font=("Meera", 14, "bold"))
passwd = Entry(window, font=("Meera", 14, "bold"))

submit = Button(window, text="Add Info", command=onsubmit, font=("Meera", 14, "bold"))

entity_label.grid(columnspan=3, row=0)
website_label.grid(row=1)
email_label.grid(row=2)
passwd_label.grid(row=3)
website.grid(row=1, column=1)
email.grid(row=2, column=1)
passwd.grid(row=3, column=1)
submit.grid(columnspan=3)

website_label2 = Label(window, text='Website: ', font=('Meera', 14, "bold"))
email_label2 = Label(window, text='Email: ', font=('Meera', 14, "bold"))
pass_label2 = Label(window, text='Password: ', font=('Meera', 14, "bold"))

website_label2.grid(row=5)
email_label2.grid(row=5, column=1)
pass_label2.grid(row=5, column=2)

readfile()

filemenu = Menu(window)
submenu = Menu(filemenu, tearoff=False)

filemenu.add_cascade(label="File", font=("Meera", 10, "bold"), menu=submenu)
submenu.add_command(label="Close", font=("Meera", 10, "bold"), command=window.destroy, accelerator="Ctrl W", compound=LEFT, image=closeicon)

submenu = Menu(filemenu, tearoff=False)
filemenu.add_cascade(label="Help", font=("Meera", 10, "bold"), menu=submenu)
submenu.add_command(label="About", font=("Meera", 10, "bold"), command=about, accelerator="Ctrl H", compound=LEFT, image=infoicon)

window.bind("<Control-w>", closeapp)
window.bind("<Control-h>", about)
website.bind("<Return>", onsubmit)
email.bind("<Return>", onsubmit)
passwd.bind("<Return>", onsubmit)

window.config(menu=filemenu)

window.mainloop()
