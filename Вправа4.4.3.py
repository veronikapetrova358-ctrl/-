from tkinter import*

def click(): 
    PI = 3.1416
    entry2.delete(0, END)
    r = float(entry.get())
    s = PI*r**2
    entry2.delete(0, END)
    entry2.insert(0, str(s))

root = Tk()
root.geometry("400x300")
label = Label(text = 'Радіус круга')
label1.pack(pady = 10)
entry1 = Entry()
entry1.pack(pady = 10)
label2 = Label(text = 'Площа круга')
label2.pack(pady = 10)
entry2 = Entry()
entry2.pack(pady = 10)
button = Button(text = 'Площа круга', command=click)
button.pack(pady = 10)
root.mainloop() 