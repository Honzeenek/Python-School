import tkinter as tk

root = tk.Tk()
root.title("Korálky na niti")

canvas = tk.Canvas(root, width=500, height=100, bg="white")
canvas.pack()

x = 10
radius = 10

for i in range(15):
    if i < 8:
        color = "red" 
    else:
        color = "blue" 
    canvas.create_oval(x, 20, x + 2 * radius, 20 + 2 * radius, fill=color)
    x += 2 * radius + 5 

root.mainloop()