import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

current_file = None

def newfile():
    global current_file
    text.delete(1.0,tk.END)
    current_file = None
    root.title("Untitled - Notepad")

def openfile():
    global current_file
    file = filedialog.askopenfilename()
    if file:
        with open (file,"r") as f:
            content = f.read()
            text.delete(1.0,tk.END)
            text.insert(tk.END,content)
        current_file = file
        root.title(f"{file.split('/')[-1]} - Notepad")

def savefile():
    global current_file
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file :
        with open(file,"w") as f:
            f.write(text.get(1.0,tk.END))
        current_file = file
        root.title(f"{file.split('/')[-1]} - Notepad")

def exitapp():
    root.quit()

def show():
    messagebox.showinfo("About", "Ye ek simple Notepad app hai.\nBanaya gaya Python aur Tkinter se.\nkripya apni ma na chudaye help mang kr")

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x800")

text = tk.Text(root,font=("Arial",14)) #Yeh ek typing area banata hai
text.pack(fill="both",expand=True)  #text area poori window me fail jaata hai

#scroll bar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right",fill='y')

scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

# main menu
menubar = tk.Menu()
root.config(menu=menubar)

# file menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New",command=newfile)
file_menu.add_command(label="Open",command=openfile)
file_menu.add_command(label="Save",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exitapp)

# edit menu
edit_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="Cut",command=lambda:text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy",command=lambda:text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste",command=lambda:text.event_generate("<<Paste>>"))

# help menu
help_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_menu)

help_menu.add_command(label="About", command=show)

root.mainloop()