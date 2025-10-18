import tkinter as tk

current_player = "X" 

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")

label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn["state"] = "disabled"

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def check_winner():
    for i in range(3):
        if (buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != ""):
            return True

    for j in range(3):
        if (buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != ""):
            return True

    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != ""):
        return True
    if (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != ""):
        return True

    return False

def on_click(i, j):
    global current_player
    btn = buttons[i][j]
    if btn["text"] == "":
        btn["text"] = current_player
        btn["state"] = "disabled"
        
        if check_winner():
            label["text"] = f"Player {current_player} wins!"
            disable_all_buttons()
        elif check_draw():
            label["text"] = "It's a draw!"
            disable_all_buttons()
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            label["text"] = f"Player {current_player}'s Turn"

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", width=6, height=3, font=("Arial", 14),
            command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

def reset_game():
    global current_player
    current_player = "X"
    label["text"] = "Player X's Turn"
    for row in buttons:
        for btn in row:
            btn["text"] = ""
            btn["state"] = "normal"

reset_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()