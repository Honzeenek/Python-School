import tkinter as tk
import random

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack()

def rada(y):
    x = 10
    for i in range(20):
        canvas.create_rectangle(x, y, x + 10, y + 10, fill='grey')
        if i < 19:
            x += 10 + random.randint(12, 20)

for i in range(15):
    rada(5 + i * 15)

window.mainloop()
