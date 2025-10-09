"""
File Name: drawing_recognition.py
Author: Parth Joshi
Purpose: Drawing Board and Predict Drawings
"""

from tkinter import *
from tensorflow.keras.models import load_model
from PIL import ImageGrab, ImageOps
import numpy as np


class main:
    def __init__(self, master):
        self.master = master

        self.bgColor = "white"
        self.brush_color = "black"

        self.label = Label(window, text="Prediction: ", font="Helvetica")
        self.label.pack()

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

        self.model = load_model("digital_model.keras")

    def paint(self, e):
        color = self.bgColor if self.erase_on else self.brush_color

        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, capstyle="round", smooth=True, width=10, fill=color)
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None
        self.prediction()

    def clear(self, e):
        self.canvas.delete(ALL)

    def erase(self, e):
        self.erase_on = True

    def brush(self, e):
        self.erase_on = False

    def prediction(self):
        image = self.get_image()
        processed_image = self.preprocess_image(img=image)
        prediction = self.model.predict(processed_image)
        digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        self.label.config(text = f"Prediction {digit} ({confidence:.2f}%)")
        print(prediction)

    #Gets The Image on the Canvas Section
    def get_image(self):
        x = self.master.winfo_rootx() + self.canvas.winfo_x()
        y = self.master.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        img = ImageGrab.grab(bbox=(x, y, x1, y1))
        return img

    def preprocess_image(self, img):
        img = ImageOps.grayscale(img)
        img = ImageOps.invert(img)
        img = img.resize((28, 28))
        img = np.array(img) / 255.0
        img = img.reshape(1, 28, 28, 1)
        return img


if __name__ == "__main__":
    window = Tk()
    window.title("Drawing Board")
    window.geometry("512x512") #128 * 4
    window.resizable(width=False, height=False)
    main(window)
    window.mainloop()

