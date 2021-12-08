from tkinter import *
from PIL import ImageTk, Image
from random import randint

class Apple:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/apple.png')) if not Apple.IMAGE else Apple.IMAGE
        Apple.IMAGE = self.image
        self.object = canvas.create_image(randint(10, 690), -20, anchor=NW, image=self.image)
        self.canvas = canvas

    @property
    def coords(self):
        return self.canvas.coords(self.object)

    @property
    def x(self):
        return self.canvas.coords(self.object)[0]

    @property
    def y(self):
        return self.canvas.coords(self.object)[1]

    @coords.setter
    def coords(self, new_coords):
        self.canvas.coords(self.object, new_coords)

    # Bắt đầu rơi
    def begin(self):
        self.coords = [randint(10, 690), -20]

    # Quả táo rơi
    def fall(self, speed):
        self.canvas.move(self.object, 0, speed)
        self.canvas.update()