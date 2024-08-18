import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Hello, world!")

app = tk.Tk()
app.title("Test GUI")

button = tk.Button(app, text="Show Message", command=show_message)
button.pack(pady=20)

app.mainloop()
