from pathlib import Path
from tkinter import PhotoImage, Button


class DefaultButton(Button):
    def __init__(self, master, image, x, y, width, height, command):
        super().__init__(master, image=image, borderwidth=0, highlightthickness=0, command=command,
                         relief="flat")
        self.place(x=x, y=y, width=width, height=height)
