import tkinter as tk


def click():  # Контроллер: функция вызывается в момент нажатия на кнопку
    counter.set(counter.get() + 1)
    # метод get() возвращает текущее значение counter
    # метод set() - устанавливает новое значение counter


root = tk.Tk()

counter = tk.IntVar()  # Модель: создаем объект класса IntVar

counter.set(0)  # Обнуляем созданный объект с помощью метода set()

frame = tk.Frame(root)
frame.pack()

btn = tk.Button(frame, text='Click', command=click)
btn.pack()
# Создаем кнопку и указываем обработчик (функция click) при нажатии на неё

label = tk.Label(frame, textvariable=counter)
label.pack()

root.mainloop()

#
