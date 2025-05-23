import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def klik(mys):
    width = canvas.winfo_width()
    left_zone = width / 3
    right_zone = width * 2 / 3
    
    if mys.x < left_zone:
        color = 'red'
    elif mys.x < right_zone:
        color = 'yellow'
    else:
        color = 'green'
        
    canvas.create_oval(mys.x, mys.y, mys.x + 10, mys.y + 10, fill=color)

canvas.bind('<B1-Motion>', klik)
canvas.mainloop()

