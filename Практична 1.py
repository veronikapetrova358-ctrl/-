from tkinter import *
def click()
    entry ['bg'] = 'red'
    entry ['font'] = 'Arial 14'
    entry ['width'] +=20 
    entry['fg'] = 'white' 
    entry.dlete(0, END)
    entry.insert(0, 'Ми використовуємо властивості поля!') 
root = TK()
root.geometry('400x300')

entry = Entry(width= '15', bd='3',)
entry.pack(pady = 30)

button = Button(width='10', trxt = '8 клас', fg = 'blue', bg = 'yellow', command=click)
button.pack(pady = 10)
root.mainloop()