from tkinter import*
w = Tk()
w.geometry('300x400')

def cl():
    x = float (ent1.get())
    p = float (ent2.get())
    a = float (ent3.get())
    n = 0
    while x<a
    x = x+x*p/100
    n = n+1
    ent4.delete(0, END)
    ent4.insert(0,str(n))



lb1=Label(text = 'Початкова сума')
lb1.pack()
ent1=Entry()
ent1.pack()

lb2=Label(text = 'Річні відсотки')
lb2.pack()
ent2=Entry()
ent2.pack(pady = 5)

lb3=Label(text = 'Кінцева сума')
lb3.pack()
ent3=Entry()
ent3.pack(pady = 5)

bt = Button(text = 'Обчислити', command = cl)
bt.pack(pady = 5)

lb4=Label(text = 'Кількість років')
lb4.pack()
ent4=Entry()
ent4.pack(pady = 10)