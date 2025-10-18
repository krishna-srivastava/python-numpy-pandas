import tkinter as tk

root = tk.Tk()
root.title("kill jews")
root.geometry("400x400")

label = tk.Label(root,text = "enter your name:",font=("Arial",14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial",14))
entry.pack(pady=10)

def greet_user():
    name = entry.get()  # entry se text lo
    label.config(text=f"Hello, {name}!")  # label ka text update karo

button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 14))
button.pack(pady=10)

root.mainloop()