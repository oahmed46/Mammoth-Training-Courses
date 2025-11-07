import tkinter
from tkinter import ttk

def main():

    root = tkinter.Tk()
    root.title("Random String Generator")

    frame = ttk.Frame(root) 
    frame.grid() 

    label = ttk.Label(frame, text="Welcome to the App")
    label.grid()

    button = ttk.Button(frame, text="Generate String")
    button.grid() 

    exit_button = ttk.Button(frame, text="Exit")
    exit_button.grid() 

    root.mainloop()

main()