from tkinter import *
import random

def generate_password():
    length = int(insertentry.get())
    characters = randomslova
    if special_characters_var.get():
        characters += special_characters
    for i in range(length):
        password = ""
        for i in range(length):
            password += random.choice(characters)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.geometry("500x250")
window.title("Password Generator")
window.resizable(FALSE, FALSE)

randomslova = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
special_characters = "!@#$%^&*()[]{};:,./<>?\|`~-=_+"
special_characters_var = BooleanVar()
special_characters_var.set(False)

title_label = Label(window, text="Password Generator", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

length_frame = Frame(window)
length_frame.pack()

insertlength = Label(length_frame, text="Number of characters:", font=("Helvetica", 12))
insertlength.grid(row=0, column=0, padx=10, pady=5)

insertentry = Entry(length_frame, font=("Helvetica", 10), width=5)
insertentry.grid(row=0, column=1, padx=10, pady=5)

generate_button = Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=10)

password_label = Label(window, text="Generated Password:", font=("Helvetica", 12))
password_label.pack()

password_entry = Entry(window, font=("Helvetica", 10), width=30)
password_entry.pack(pady=5)

special_characters_checkbox = Checkbutton(window, text="Use special characters", variable=special_characters_var, font=("Helvetica", 12))
special_characters_checkbox.pack(pady=5)

window.mainloop()