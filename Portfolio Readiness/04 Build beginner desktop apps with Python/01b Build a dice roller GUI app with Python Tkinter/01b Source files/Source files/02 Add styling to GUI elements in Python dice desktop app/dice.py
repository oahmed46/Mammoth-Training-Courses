import tkinter as tk 

root = tk.Tk()
root.title("Dice Roller")
root.geometry("500x300")
root.configure(background = "white")

label = tk.Label(root, text = "1 to 6", background="white", foreground = "#DD571C",
    font = ("Helvetica", 60), pady = 30
)
label.pack()

def roll():
    print("Rolling")

button = tk.Button(root, text = "Roll", command = roll,
    bg="#DD571C", fg="#DD571C",
    activebackground="#DD571C", activeforeground="white",
    highlightbackground="#DD571C", highlightcolor="white",
    font = ("Helvetica", 60)
)
button.pack()

root.mainloop()