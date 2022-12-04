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
        b2_img = pygame.image.load(os.path.join("assets", "buttons", "b2.png"))
        b3_img = pygame.image.load(os.path.join("assets", "buttons", "b3.png")) 
        b4_img = pygame.image.load(os.path.join("assets", "buttons", "b4.png")) 
        b5_img = pygame.image.load(os.path.join("assets", "buttons", "b5.png")) 
        b6_img = pygame.image.load(os.path.join("assets", "buttons", "b6.png")) 

        ImageButton(self.display_surface, b1_img, (367, 526), None).draw(self.events)
        ImageButton(self.display_surface, b2_img, (606, 526), None).draw(self.events)
        ImageButton(self.display_surface, b3_img, (844, 526), None).draw(self.events)
        ImageButton(self.display_surface, b4_img, (367, 643), None).draw(self.events)
        ImageButton(self.display_surface, b5_img, (606, 643), None).draw(self.events)
        ImageButton(self.display_surface, b6_img, (844, 643), None).draw(self.events)

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
