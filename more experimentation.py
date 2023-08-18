import tkinter as tk
from tkinter import ttk
from tkinter import *


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        self.last_x = None
        self.last_y = None
        self.corner_1 = None
        self.corner_2 = None
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<Button-2>", self.get_point)
        self.bind("<Button-3>", self.add_line)

    def save_posn(self, event):
        self.last_x, self.last_y = event.x, event.y

    def get_point(self, event):
        self.corner_1, self.corner_2 = event.x, event.y

    def add_line(self, event):
        self.create_rectangle(self.last_x, self.last_y, self.corner_1, self.corner_2)
        self.save_posn(event)


window = tk.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


sketch = Sketchpad(window)
sketch.grid(row=0, column=0, sticky="nsew")

window.mainloop()
