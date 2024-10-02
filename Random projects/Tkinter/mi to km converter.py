from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# LABEL
my_label1 = Label(text="Miles", font=("Arial", 14))
my_label1.grid(column=2, row=0)
my_label2 = Label(text="is equal to", font=("Arial", 14))
my_label2.grid(column=0, row=1)
my_label3 = Label(text="0", font=("Arial", 14))
my_label3.grid(column=1, row=1)
my_label4 = Label(text="Km", font=("Arial", 14))
my_label4.grid(column=2, row=1)


def button_clicked():
    print("clicked")
    new_word = round(float(input.get()) * 1.6)
    my_label3["text"] = new_word


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())

window.mainloop()
