from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# update label
my_label["text"] = "New Text"

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)


window.mainloop()
