import os
import sys
import pygame
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
        NotImplemented

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)
            self.display_surface.blit(self.background, (0, 0))
            self.draw_buttons()
            pygame.display.update()
