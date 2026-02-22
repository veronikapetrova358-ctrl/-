from tkinter import* 

root = Tk()
root.geometry("400x500")
choice1 = BooleanVar()
flag1 = Checkbutton(text = 'Предметні гуртки'. variable - choice1)
choice2 = BooleanVar()
flag1.pack(pady = 10)
flag2 = Checkbutton(text = 'Спортивні секції', variable = choice2)
flag2.pack(pady = 10)
choice3 = BooleanVar()
flag3 = Checkbutton(text = 'Театральна студія', variable = choice3)
flag3.pack(pady = 10)
s = 0
if choice.get() == 1: s = 10
elif choice.get() == 2: s = 7
elif choice.get() == 3: s = 4
elif choice.get() == 4: s = 1
if choice1.get(): s += 5
if choice2.get(): s += 5
if choice3.get(): s += 5
lb2[‘text’] = str(s)
root.mainloop() 