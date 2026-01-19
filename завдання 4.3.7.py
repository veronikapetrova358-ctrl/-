from tkinter import *

def day():
    root["bg"] = "white"
    
root = Tk()
root.geometry('200x200+10+10')

but1 = Button(text="День", command=day)
but1.pack(pady=20)

root.mainloop()