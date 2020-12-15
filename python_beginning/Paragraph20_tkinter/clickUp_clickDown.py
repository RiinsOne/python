import tkinter as tk

root = tk.Tk()

# Модель:
counter = tk.IntVar()
counter.set(0)


# Два контроллера:
def clickUp():
    counter.set(counter.get() + 1)


def clickDown():
    counter.set(counter.get() - 1)


# Вид:
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Up', command=clickUp)
button.pack()

button = tk.Button(frame, text='Down', command=clickDown)
button.pack()

label = tk.Label(frame, textvariable=counter)
label.pack()

root.mainloop()

#
