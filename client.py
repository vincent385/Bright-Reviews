import os
import sys
import pygame
from buttons import ImageButton
from settings import *


class Client:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hello, World!")
        self.clock = pygame.time.Clock()
        background_img = pygame.image.load(os.path.join("assets", "background.png"))
        self.background = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_buttons(self):
        b1_img = pygame.image.load(os.path.join("assets", "buttons", "b1.png"))
        ImageButton(self.display_surface, b1_img, (367, 526), None).draw(self.events)

    def run(self):
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)
            self.display_surface.blit(self.background, (0, 0))
            self.draw_buttons()
            pygame.display.update()
