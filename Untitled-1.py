from tkinter import*

def click () :
    x = float (ent1.get())
    y = float (ent2.get())
    z = float (ent3.get())
    t = x > 0 and (y > 0 or z < 0)
    ent4.delete(0,END)
    ent4.insert(0,str(t))

win = Tk()
win.geometry('300x500')

lb1 = Label(text = 'Значення змінної х')
lb1.pack(pady =5)
ent1 = Entry()
ent1.pack(pady=5)

lb2 = Label(text 'Значення змінної y')
lb2.pack(pady =5)
ent2 = Entry
ent2.pack(pady=5)

lb3 = Label(text 'Значення змінної z')
lb3.pack(pady =5)
ent3 = Entry
ent3.pack(pady=5)

bt = Button(text = 'Обчислити', command = click)
bt.pack(pady =5)

lb4 = Label(text 'Результат')
lb4.pack(pady =5)
ent4 = Entry
ent4.pack(pady=5)
