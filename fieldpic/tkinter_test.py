from Tkinter import *

root = Tk()
root.geometry('400x850')

c = Canvas(root, width=400, height=850)
c.pack()

r = c.create_rectangle(0, 0, 50, 50, fill='red', outline='blue')

# keybindings
root.bind('<q>', quit)

root.mainloop()
