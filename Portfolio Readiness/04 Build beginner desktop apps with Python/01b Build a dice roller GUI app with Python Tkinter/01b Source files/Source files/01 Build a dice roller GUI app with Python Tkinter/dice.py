import tkinter as tk 

root = tk.Tk()
root.title("Dice Roller")
root.geometry("500x300")

label = tk.Label(root, text = "1 to 6")
label.pack()

def roll():
    print("Rolling")

button = tk.Button(root, text = "Roll", command = roll)
button.pack()

root.mainloop()