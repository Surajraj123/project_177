from tkinter import *
root = Tk()
root.title("ENCAPSULATION")
root.geometry("500x500")

label_name = Label(root, text = "Name:- ")
label_name.place(relx = 0.5, rely = 0.4)
Entry = (root)
Entry.place(relx = 0.5, rely = 0.7)

label_password = Label(root, text = "Password:- ")
label_password.place(relx = 0.7, rely = 0.4)
Entry = (root)
Entry.place(relx = 0.7, rely = 0.7)

label_captcha = Label(root, text = "Captcha:- ")
label_captcha.place(relx = 0.9, rely = 0.4)
Entry = (root)
Entry.place(relx = 0.9, rely = 0.7)