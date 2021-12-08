from tkinter import *
from PIL import ImageTk, Image

class Background:

    IMAGE = None

    def __init__(self, canvas):
        self.image = ImageTk.PhotoImage(Image.open('photos/backgr.png')) if not Background.IMAGE else Background.IMAGE
        Background.IMAGE = self.image
        self.object = canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas = canvas