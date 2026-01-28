from tkinter import*

def click():
    x = float(entry1.get())
    y = float(entry2.get())
    z - x * y 
    entry3.delete(0, END)
    entry3.insert(0, str(z))

root = Tk()
 root.geometry("400x350")
label1 - Label(text - 'Перший множник')
label1.pack(pady - 10)
entry1= Entry()
entry1.pack(pady = 10) 
label2 = Label(text = 'Другий множник') 
label2.pack(pady - 10)
entry2 - Entry()
entry2.pack(pady - 10)
Label3 = Label(text= 'Добуток')
label3.pack(pady = 10)
entry3 = Entry(width = 10)
entry3.pack(pady - 5)

button - Button(text - 'Помножити', command-click)
button.pack(pady = 10)
root.mainloop()