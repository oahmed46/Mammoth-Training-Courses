from tkinter import *

root = Tk()
root.title("Form")
root.geometry("500x350")

fields = "First Name", "Last Name", "Course Name", "Country"

def build_form(root, fields):
    entries = []
    for field in fields:
        frame = Frame(root)
        label = Label(frame, text=field, pady=20, font=("Helvetica", 20))
        entry = Entry(frame)
        label.pack(side=LEFT)
        frame.pack(side=TOP)
        entry.pack(side=RIGHT)
        entries.append((field,entry))
    return entries

entries = build_form(root, fields)

def print_form(entries):
    for entry in entries:
        print("%s:%s"%(entry[0], entry[1].get()))

button = Button(root, text="Print", command=(lambda e = entries: print_form(entries)), font=("Helvetica", 20))
button.pack()

root.mainloop()