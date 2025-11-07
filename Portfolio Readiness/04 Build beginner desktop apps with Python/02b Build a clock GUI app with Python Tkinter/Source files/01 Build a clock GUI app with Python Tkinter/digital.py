from tkinter import *

root = Tk()
root.title("Digital Clock")
root.geometry("500x200")

clock = Label(root, text = "Clock", font = ("Helvetica", 50), pady = 50)

clock.pack()

root.mainloop()
