# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#list with all the character for password generator
import random
from tkinter import messagebox
import json
password_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v','x', 'y', 'z', 
'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
]

#function to generate password 15 character
def generate_password():
    password = ''
    passwordEntry.delete(0,END)
    for i in range(15):
        password += random.choice(password_list)
    passwordEntry.insert(0, password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
#function to save password
def save_password():
    website = websiteEntry.get()
    email = usernameEntry.get()
    password = passwordEntry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showinfo("Error", "Please fill all the fields!")
        return
    else:
        messagebox.askokcancel(title=website, message=f" Website: {website}\n Username: {email}\n Password: {password}\n is that ok to save?")
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                
        
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f,indent=4)
        else:
            #updating old data
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
                messagebox.showinfo(website, "Data saved succesfully!")
        finally:
            websiteEntry.delete(0,END)
            passwordEntry.delete(0,END)
        
            

    
        


        

# ---------------------------- LOAD PASSWORD ------------------------------- #
#function to load password
#copy password to clipboard
import pyperclip

def search():
    website = websiteEntry.get()
    try:
        with open('data.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message="No data file found")
    else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title= website, message= f' Email: {email}\n Password: {password}')
                pyperclip.copy(password)
            else:
                messagebox.showerror(title= "Error", message="Data not found")

# ----------------------------- Pawword to open app ---------------------------- #
#if first time ask password
def check_password():
    mdp = "0407"
    #loop to ask password
    while True:
        if entry.get() == mdp:
            intro_password.destroy()
        else:
            messagebox.showerror(title= "Error", message="Wrong password")
            break
       



    


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from PIL import Image,ImageTk
import random

#open window that ask password
intro_password = Tk()
intro_password.title("Password")
intro_password.config(padx=50, pady=50)

label = Label(text="Password")
label.grid(row=0, column=0)
#entry
entry = Entry(intro_password, width=30)
entry.grid(row=0, column=1)
#button
button = Button(text="OK", command=check_password)
button.grid(row=1, column=1)

intro_password.mainloop()



root = Tk()
root.title("Password Generator")
root.config(padx=50, pady=50)

canvas = Canvas(root, width=200, height=200)
logo_img= PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)



#Labels

#website
website= Label(text="Website:")
website.grid(row=1, column=0)

#username
username = Label(text="Email / Username:")
username.grid(row=2, column=0)

#password
password = Label(text="Password:")
password.grid(row=3, column=0)

#entries
websiteEntry = Entry(width=35,)
websiteEntry.grid(row=1, column=1, columnspan=2)
websiteEntry.focus()

usernameEntry = Entry(width=35)

usernameEntry = Entry(width=35)
usernameEntry.grid(row=2, column=1, columnspan=2)
usernameEntry.insert(0,"imohamed@live.fr")

passwordEntry = Entry(width=35)
passwordEntry.grid(row=3, column=1, columnspan=2)

#Buttons
GeneratorButton = Button(text="Generate Password",width=30,command=generate_password)
GeneratorButton.grid(row=4, column=1, columnspan=2)

Add_button= Button(text="Add",width=30, command=save_password)
Add_button.grid(row=5, column=1, columnspan=2)

Search_button= Button(text="Search",width=30, command=search)
Search_button.grid(row=6, column=1, columnspan=2)




root.mainloop()
