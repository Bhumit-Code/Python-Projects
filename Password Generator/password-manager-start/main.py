from tkinter import messagebox
from tkinter import *
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # l_sample = random.randint(8, 10)
    # s_sample = random.randint(2, 4)
    # n_number = random.randint(2, 4)

    # letter_list = [random.choice(letters) for char3 in range(l_sample)]
    # symbol_list = [random.choice(symbols) for char1 in range(s_sample)]
    # number_list = [random.choice(numbers) for char2 in range(n_number)]
    letter_list = [choice(letters) for char3 in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char1 in range(randint(2, 4))]
    number_list = [choice(numbers) for char2 in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list
    # for char in range(l_sample):
    #     password.append(random.choice(letters))

    # for char in range(s_sample):
    #     password += random.choice(symbols)
    #
    # for char in range(n_number):
    #     password += random.choice(numbers)
    shuffle(password_list)
    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please dont leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the message entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
                entry_website.delete(0, 'end')
                entry_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(500, 400)
window.config(padx=20, pady=20)

# IMAGE CANVAS
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# LABEL
label_website = Label(text="Website:", fg="black", font=("Arial", 10, "bold"))
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:", fg="black", font=("Arial", 10, "bold"))
label_email.grid(column=0, row=2)
label_password = Label(text="Password:", fg="black", font=("Arial", 10, "bold"))
label_password.grid(column=0, row=3)

# TEXT BOX
entry_website = Entry(width=43)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
entry_website.focus()
entry_email = Entry(width=43)
entry_email.insert(0, "bhumitr1205@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, sticky="w")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, columnspan=1, sticky="w")

# BUTTON

button_pass = Button(text="Generate Password", font=("Arial", 9, "bold"), command=generate_password)
button_pass.grid(column=1, row=3, columnspan=2, sticky="e")
button_add = Button(text="ADD", width=36, font=("Arial", 9, "bold"), command=add)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
