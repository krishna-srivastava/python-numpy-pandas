# calculator using GUI
import tkinter as tk

def backspace():
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current[0:-1])

def clear():
    entry.delete(0, tk.END)

def click(val):
    entry.insert(tk.END,val)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x410")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['=', '⌫', '', '']
]

for i in range(5):
    for j in range(4):
        btntext = buttons[i][j]
        if(btntext == "C"):
            btn = tk.Button(root,text = btntext,width=5,height=2,font=("Arial",14),command=clear)
        elif(btntext == "="):
            btn = tk.Button(root,text = btntext,width=5,height=2,font=("Arial",14),command=calculate)
        elif(btntext == "⌫"):
            btn = tk.Button(root,text = btntext,width=5,height=2,font=("Arial",14),command=backspace)
        elif(btntext == ""):continue
        else:
            btn = tk.Button(root,text = btntext,width=5,height=2,font=("Arial",14),command=lambda val = btntext: click(val))
         
        btn.grid(row=i + 1, column=j, padx=5, pady=5)


root.mainloop()