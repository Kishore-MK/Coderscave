import random
import string
import pyperclip as pc
from tkinter import *

root=Tk()
root.geometry("700x400")
root.resizable(1,0)
length = 0
# Creating variables for Check box
pwlen=StringVar(value=0)
uppercase= IntVar()
lowercase= IntVar()
digits= IntVar()
special_chars= IntVar()
password =[]

def generatepw(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    if length and length>=use_lowercase+use_uppercase+use_digits+use_special_chars:
        # Defining character sets based on user preferences
        characters = ""
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation


        global password
        password = []
        if use_lowercase:
            password.append(random.choice(string.ascii_lowercase))
        if use_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_digits:
            password.append(random.choice(string.digits))
        if use_special_chars:
            password.append(random.choice(string.punctuation))
        # Generating the remaining characters randomly
        remaining_length = length - len(password)
        print(remaining_length)
        for _ in range(remaining_length):
            password.append(random.choice(characters))

        # Shuffling characters to make the password random
        random.shuffle(password)

        # Convertion of the list of characters to a string
        print(password)
        password = ''.join(password)
        pw.config(text=password,bg="green")
    else:
        pw.config(text="Insignificant length!",bg="red")
# Function to store the length of password given by user
def spinlength():
    global length
    length=int(pwlen.get())
    
def genbutton():
    a=uppercase.get()
    b=lowercase.get()
    c=digits.get()
    d=special_chars.get()
    print(a,b,c,d)

    try:
        generatepw(length,a,b,c,d)
    except:
        pw.config(text="Select atleast one character set!!",bg="red")

# Function to copy the generated password to clipboard using pyperclip module
def copytoc():
    pc.copy(str(password))
    copied.config(text="Copied to clipboard")

frame1 = Frame(root,bg="#FFFFFF")
frame1.pack(side=TOP, fill="x")

name = Label(frame1,text="Password length: ",font=("Helvetica",14),bg="#FFFFFF")
name.grid(row=0,column=0)

# Getting password length from the user using spinbox from Tkinter module
spin_len = Spinbox(frame1,from_=0,to=1000,font=("Helvetica",16),textvariable=pwlen,command=spinlength)
spin_len.grid(row=0,column=1,pady=20)

# Check boxes for character preferences
uppercheck = Checkbutton(frame1,text="Include Uppercase characters",font=("Helvetica",14),variable=uppercase,bg="#FFFFFF")
uppercheck.grid(row=1,column=0,columnspan=2)

lowercheck = Checkbutton(frame1,text="Include Lowercase characters",font=("Helvetica",14),variable=lowercase,bg="#FFFFFF")
lowercheck.grid(row=2,column=0,columnspan=2)

digitscheck = Checkbutton(frame1,text="Include Digits",font=("Helvetica",14),variable=digits,bg="#FFFFFF")
digitscheck.grid(row=3,column=0,columnspan=2)

specialcheck = Checkbutton(frame1,text="Include Special characters",font=("Helvetica",14),variable=special_chars,bg="#FFFFFF")
specialcheck.grid(row=4,column=0,columnspan=2)

generate = Button(frame1,text="Generate password",font=("Helvetica",12),command= genbutton,bg="#D9DDDC",borderwidth=0)
generate.grid(row=5,column=0,columnspan=2)
yourpw = Label(frame1,text="Your password: ",font=("Helvetica",14),bg="#FFFFFF")
yourpw.grid(row=6,column=0,pady=30)

pw = Label(frame1,text="Generate your random password here!",font=("Helvetica",14),bg="#FFFFFF")
pw.grid(row=6,column=1,pady=30)

copy = Button(frame1,text="Copy to clipboard",font=("Helvetica",14),command=copytoc,bg="#D9DDDC",borderwidth=0)
copy.grid(row=8,column=0,columnspan=2)
copied = Label(frame1,text="",font=("Helvetica",10),bg="#FFFFFF")
copied.grid(row=9,column=0,columnspan=2)



root.mainloop()