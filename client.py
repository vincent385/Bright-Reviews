import os
import sys
from pywindows import Window, WindowChild


class Client(Window):
    width, height = (1366, 768)

    def __init__(self):
        super().__init__("Bright Reviews", self.width, self.height, False)
        self.set_background_img(image_path=os.path.join("assets", "title.png"), fmt="png")

    def run(self):
        self.display()

if __name__ == '__main__':
    client = Client()
    client.run()
