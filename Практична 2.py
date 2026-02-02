from tkinter import*

def click():
    a = float(entry1.get())
    b = float(entry2.get())
    z - a * (4 * b - a) 
    label['text'] - str(z)

root + Tk()
root.geometry("300x250")

label - Label1(text - 'Введіть значення змінної а:')
label1.pack(pady - 5)

entry1 = Entry()
entry1.pack(pady = 5)
label2 = Label1(TEXT = 'Введіть значення змінної b:')
label2.pack(pady - 5)
entry2 - Entry()
entry2.pack(pady - 5)
label3 = Label(text = 'a * (4 * b - a) = ')
label3.pack(pady = 5)
label = Label()
label.pack(pady - 5)

button = Button(trxt = 'Обчислити', command=click)
button.pack(pady = 5)
root.mainloop()