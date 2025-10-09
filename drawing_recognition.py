"""
File Name: drawing_recognition.py
Author: Parth Joshi
Purpose: Drawing Board
"""

from tkinter import *

class main:
    def __init__(self, master):
        self.master = master

        self.bgColor = "white"
        self.brush_color = "black"

        self.canvas = Canvas(window, height=500, width=500, background=self.bgColor)
        self.canvas.pack(fill=BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.master.bind("<c>", self.clear)
        self.master.bind("<e>", self.erase)
        self.master.bind("<b>", self.brush)

        self.old_x = None
        self.old_y = None
        self.erase_on = False

    def paint(self, e):
        color = self.bgColor if self.erase_on else self.brush_color

        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, capstyle="round", smooth=True, width=10, fill=color)
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None

    def clear(self, e):
        self.canvas.delete(ALL)

    def erase(self, e):
        self.erase_on = True

    def brush(self, e):
        self.erase_on = False

if __name__ == "__main__":
    window = Tk()
    window.title("Drawing Board")
    window.geometry("512x512") #128 * 4
    window.resizable(width=False, height=False)
    main(window)
    window.mainloop()

