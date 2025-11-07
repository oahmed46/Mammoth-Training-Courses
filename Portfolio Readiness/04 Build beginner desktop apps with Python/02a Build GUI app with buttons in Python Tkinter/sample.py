import tkinter
from tkinter import ttk
import random

def generate_string(root):
    new_title=""
    for index in range(5):
        new_title += chr(ord("A") + random.randrange(26))
    root.title(new_title)

def exit(root):
    root.destroy()

def main():
    
    root = tkinter.Tk()
    root.title("Ramdon String Generator")

    frame = ttk.Frame(root)
    frame.grid()

    label = ttk.Label(frame,text="Welcome to the App")
    label.grid()

    button = ttk.Button(frame, text="Generate String")
    button.grid()
    button["command"] = lambda: generate_string(root)

    exit_button = ttk.Button(frame, text="Exit")
    exit_button.grid()
    exit_button["command"] = lambda: exit(root)

    root.mainloop()

main()