from tkinter import *

window = Tk()
# TITLE
window.title("My First GUI")
# WINDOW SIZE
window.minsize(width=500, height=400)
# PADDING
window.config(padx=20, pady=20)

# LABEL
my_label = Label(text="HELLO", font=("Arial", 23, "bold"))
# my_label.pack(side="top")
my_label["text"] = "New Text"
# my_label.config(text = "whats upp")
# my_label.place(x = 0, y =0)
my_label.grid(column=0, row=0)
# PADDING
my_label.config(padx=50,pady=50)


# BUTTONS

def button_clicked():
    print("clicked")
    new_word = input.get()
    my_label["text"] = new_word


button = Button(text="press me", command=button_clicked)
new_button = Button(text="New_button", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=3, row=0)
# ENTRY
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=4, row=3)

window.mainloop()
