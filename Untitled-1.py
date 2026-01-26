from tkinter import *
from tkinter.messagebox import * 
def click(event) :
    entry['bg'] = 'yellow'
    entry['fg'] = 'red'
    entry ['font'] = 12
    label ['text'] = entry.get ()
    x = entry.get()
   showinfo ('Поле', x+ '!')

root = Tk()
root.geometry ("300x250")

entry = Entry ()
entry.pack(pady = 20)
entry.focus_set()
entry.bind ('<1>',click)

label = Label ()
label.pack (pady=10)