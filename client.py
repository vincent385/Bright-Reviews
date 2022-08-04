import os
import sys
from tkinter import PhotoImage, Button, messagebox
from pywindows import Window, WindowChild


class Client(Window):
    width, height = (1366, 768)

    def __init__(self):
        # setup
        super().__init__("Bright Reviews", self.width, self.height, False)
        self.set_background_img(image_path=os.path.join("assets", "background.png"), fmt="png")

        # draw buttons
        btn1_img = PhotoImage(file=os.path.join("assets", "buttons", "b1.png"))
        top10_movies_btn = Button(image=btn1_img, borderwidth=0, highlightthickness=0,
                                  command=self.popup_notimplemented, relief="flat")
        top10_movies_btn.place(x=367, y=526, width=154, height=57)

        btn2_img = PhotoImage(file=os.path.join("assets", "buttons", "b2.png"))
        top10_shows_btn = Button(image=btn2_img, borderwidth=0, highlightthickness=0,
                                 command=self.popup_notimplemented, relief="flat")
        top10_shows_btn.place(x=606, y=526, width=154, height=57)

        btn3_img = PhotoImage(file=os.path.join("assets", "buttons", "b3.png"))
        top10_anime_btn = Button(image=btn3_img, borderwidth=0, highlightthickness=0,
                                  command=self.popup_notimplemented, relief="flat")
        top10_anime_btn.place(x=844, y=526, width=154, height=57)

        btn4_img = PhotoImage(file=os.path.join("assets", "buttons", "b4.png"))
        add_review_btn = Button(image=btn4_img, borderwidth=0, highlightthickness=0,
                                command=self.popup_notimplemented, relief="flat")
        add_review_btn.place(x=367, y=643, width=154, height=57)

        btn5_img = PhotoImage(file=os.path.join("assets", "buttons", "b5.png"))
        edit_review_btn = Button(image=btn5_img, borderwidth=0, highlightthickness=0,
                                 command=self.popup_notimplemented, relief="flat")
        edit_review_btn.place(x=606, y=643, width=154, height=57)

        btn6_img = PhotoImage(file=os.path.join("assets", "buttons", "b6.png"))
        search_review_btn = Button(image=btn6_img, borderwidth=0, highlightthickness=0,
                                   command=self.popup_notimplemented, relief="flat")
        search_review_btn.place(x=844, y=643, width=154, height=57)

    def popup_notimplemented(self):
        messagebox.showwarning("Error", "This feature is not implemented.")

    def run(self):
        self.display()

if __name__ == '__main__':
    client = Client()
    client.run()
