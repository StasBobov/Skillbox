import os
import tkinter
from PIL import Image, ImageTk

path = os.path.join(os.path.dirname(__file__), 'images\\ticket_template.png')
path2 = os.path.join(os.path.dirname(__file__), 'images\\ticket_sample.png')


class PictureCoords:

    def __init__(self, path):
        self.image = Image.open(path)
        self.tk = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.tk, width=self.image.width, height=self.image.height)


    def run(self):
        im = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=im)
        self.canvas.pack()
        self.tk.update()
        self.canvas.bind_all("<Button-1>", self.get_coords)
        self.tk.mainloop()


    def get_coords(self, event):
        print(event.x, event.y)

ticket = PictureCoords(path)
ticket.run()
