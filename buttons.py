from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text='Closing...').pack()


cancelButton = Button(root, text='Stop Reading', padx=20, pady=20, command=myClick).pack()

root.mainloop()
