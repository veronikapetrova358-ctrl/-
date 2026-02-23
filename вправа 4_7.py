from tkinter import* 
def click():
    s = 0
if choice.get() == 1: s = 10
    elif choice.get() == 2: s = 7
    elif choice.get() == 3: s = 4
    elif choice.get() == 4: s = 1
if choice1.get(): s += 5
    if choice2.get(): s += 5
    if choice3.get(): s += 5



root = Tk()
root.geometry("400x500")

choice = IntVar()
switch1 = Radiobutton(text = 'Більше 10', variable = choice, value = 1)
switch1.pack(pady = 10)
switch2 = Radiobutton(text = 'Більше 7, але не більше за 10', variable = choice, value = 2)
switch2.pack(pady = 10)
switch3 = Radiobutton(text = 'Більше 4, але не більше за 7', variable = choice, value = 3)
switch3.pack(pady = 10)
switch4 = Radiobutton(text = 'Не більше 4', variable = choice, value = 4)
switch4.pack(pady = 10)


choice1 = BooleanVar()
flag1 = Checkbutton(text = 'Предметні гуртки'. variable - choice1)
choice2 = BooleanVar()
flag1.pack(pady = 10)
flag2 = Checkbutton(text = 'Спортивні секції', variable = choice2)
flag2.pack(pady = 10)
choice3 = BooleanVar()
flag3 = Checkbutton(text = 'Театральна студія', variable = choice3)
flag3.pack(pady = 10)

button - Button(text - 'Обчислити', command - click)
button.pack(pady = 10)
lab1 = Label(text = 'Сумарний рейтинг')
lab1.pack(pady = 10)
lab2 - Label()
lab2.pack(pady = 10)
root.mainloop()