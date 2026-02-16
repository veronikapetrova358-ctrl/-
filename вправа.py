from tkinter import* 
def move(event):
    button['width'] += 5
    if button['width'] > 50:
    button['width'] = 15
root = Tk()
root.geometry("500x250")
button = Button(text = 'Кнопка', width=15)
botton.pack(pady = 20)
button.bind ('<Motion>', move)
root.mainloop()
