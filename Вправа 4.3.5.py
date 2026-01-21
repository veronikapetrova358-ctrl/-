import tkinter as tk

# Функція яка спрацьовує при натисканні на кнопку
def button_click ()
# Змінюємо розмір вікна на 500х400
root.geometry(500x400)

# Змінюємо властивості напису:
Текст - назва закладу, колір тексту - синій, фон - жовтий
label.config(
    text=Рівненський лецей №1 , # Замініть на назву вашого закладу 
    fg-blue
    bg-yellow
    font-(Arial,  16,  bold)
    )
# Створення головного вікна
root = tk,Tk ( )
root,title(Завдання 4.3.5)

Початкові значення вікна (вибиримаємо самостійно)
root.geometry(300x200)

Початкові значення напису (вибираємо самостійно)
label - tk.Label(root, text-Тут буде назва закладу, font-(Arial , 12))
label.pack (pady-30)

# Створення кнопки, Параметр command вказує на функцію button_clikc
button-tk.BUtton(root, text=Змінити налаштування , command-button_click)

# Запуск головного циклу програми
root.mainloop ( )