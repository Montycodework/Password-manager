from tkinter import *
from tkinter import messagebox
import pyperclip #Do this in last
# * import all the classes but message box is not a class its a module
# select the messagebox right click on it and then click on go to and then implementation

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Here we can use our previous project password generator
# but make sure you are going to make some improvisation in the code
# like list comprehensions
# and as many as possible

# Create lists of alphabets, numbers, special characters
def generate_password():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ["!","#","$","%","&","*","(",")","+"]

    # import random
    from random import choice, randint, shuffle

    # nr_letter = random.randint(8, 10)
    # nr_number = random.randint(2, 4)
    # nr_symbol = random.randint(2, 4)

    # password_letter = [random.choice(alphabets) for _ in range(nr_letter)]
    password_letter = [choice(alphabets) for _ in range(randint(8, 10))]
    # password_number = [random.choice(numbers) for _ in range(nr_number)]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    # password_symbol = [random.choice(symbols) for _ in range(nr_symbol)]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    # Also if u dont want to use random. every where import all

    password_list = password_letter+password_number+password_symbol
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    # use join() instead of converting list to string

    password = "".join(password_list)
    # print(password)
    # Now embed all this into a def
    password_entry.insert(0, password)
    # This lib help u to automatic copy your password in your clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- # step 2
def save_password():


    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # with open('data.txt','a') as file:
    #     file.write(f"{website} | {email} | {password}\n")
    #     website_entry.delete(0, END)
    #     email_entry.delete(0, END)
    #     email_entry.insert(0, "@gmail.com")
    #     password_entry.delete(0, END) #After this line we are going to work on message box module



    # messagebox.showinfo(title="Title", message="message")
    # messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
    #                                               f"\nPassword: {password} \n Is it ok to save?")

# Validation
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="All fields are mandatory to fill")
    else:
        # Now we are using the return of message box to control the data transfer
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                                       f"\nPassword: {password} \n Is it ok to save?")
        if is_ok == True:
            with open('data.txt','a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "@gmail.com")
                password_entry.delete(0, END)
                # Now after this we have to validate the user did'nt leave the entry empty



# ---------------------------- UI SETUP ------------------------------- # step 1

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=mypass_img)
canvas.grid(row=0, column=1)

#Label

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus() # To make the cursor by default  in website entry

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2, columnspan=2)

Add_button = Button(text="Add", width=36, command=save_password)
Add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
