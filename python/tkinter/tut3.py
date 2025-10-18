import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("400x200")

# Label 1
label1 = tk.Label(root, text="Enter your Name:")
label1.grid(row=0, column=0, padx=10, pady=10)

# Entry 1
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

# Label 2
label2 = tk.Label(root, text="Enter your password:")
label2.grid(row=1, column=0, padx=10, pady=10)

# Entry 2
entry2 = tk.Entry(root, show="*")
entry2.grid(row=1, column=1)

# Button
def show():
    name = entry1.get()
    password = entry2.get()
    full_label.config(text=f"Welcome {name}!")

button = tk.Button(root, text="Login", command=show)
button.grid(row=2, column=1, pady=10)

# Output label
full_label = tk.Label(root, text="")
full_label.grid(row=3, column=1)

root.mainloop() 
