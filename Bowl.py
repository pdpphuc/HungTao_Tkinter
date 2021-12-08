from tkinter import *
from PIL import ImageTk, Image

class Bowl:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/bowl.png')) if not Bowl.IMAGE else Bowl.IMAGE
        Bowl.IMAGE = self.image
        self.object = canvas.create_image(0, 420, anchor=NW, image=self.image)
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

    # Di chuyển cái bát
    def move(self, speed):
        if (speed < 0 and self.x > -60) or (speed > 0 and self.x < 640):
            self.canvas.move(self.object, speed, 0)
            self.canvas.update()