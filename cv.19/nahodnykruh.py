from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack()

def random_circle(r):
    x = random.randint(0, 400)
    y = random.randint(0, 300)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='red')

random_circle(30)
random_circle(20)
random_circle(40)

window.mainloop()

# for i in range(10):
#     random_circle(i)