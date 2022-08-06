import os
from tkinter import PhotoImage, messagebox
from pywindows import Window
from buttons import DefaultButton


class Client(Window):
    width, height = (1366, 768)

    def __init__(self):
        # setup
        super().__init__("Bright Reviews", self.width, self.height, False)
        self.set_background_img(image_path=os.path.join("assets", "background.png"), fmt="png")

        # draw buttons
        b1_img = PhotoImage(file=os.path.join("assets", "buttons", "b1.png"))
        DefaultButton(self, b1_img, 367, 526, 154, 57, self.popup_notimplemented)

        b2_img = PhotoImage(file=os.path.join("assets", "buttons", "b2.png"))
        DefaultButton(self, b2_img, 606, 526, 154, 57, self.popup_notimplemented)

        b3_img = PhotoImage(file=os.path.join("assets", "buttons", "b3.png"))
        DefaultButton(self, b3_img, 844, 526, 154, 57, self.popup_notimplemented)

        b4_img = PhotoImage(file=os.path.join("assets", "buttons", "b4.png"))
        DefaultButton(self, b4_img, 367, 643, 154, 57, self.popup_notimplemented)

        b5_img = PhotoImage(file=os.path.join("assets", "buttons", "b5.png"))
        DefaultButton(self, b5_img, 606, 643, 154, 57, self.popup_notimplemented)

        b6_img = PhotoImage(file=os.path.join("assets", "buttons", "b6.png"))
        DefaultButton(self, b6_img, 844, 643, 154, 57, self.popup_notimplemented)

    def popup_notimplemented(self):
        messagebox.showwarning("Error", "This feature is not implemented.")

    def run(self):
        self.display()

if __name__ == '__main__':
    client = Client()
    client.run()
