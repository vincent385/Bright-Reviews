import pygame
from typing import List, Tuple


class Button:
    def __init__(self, surface: pygame.surface.Surface, text: str, text_font: object, text_colour: Tuple[int, int, int], width: int,
                 height: int, position: Tuple[int, int], elevation: int, *, button_colour = None, button_highlight_colour = None,
                 button_shadow_colour = None, command = None, disabled = False):
        # maths to draw buttons using position as the centre origin of the button
        position = (position[0] - width/2, position[1] - height/2)

        self.surface = surface
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = position[1]
        self.command = command
        self.disabled = disabled

        # button colours
        if button_colour:
            self.button_colour = button_colour
        else:
            self.button_colour = "#475F77"
        if button_highlight_colour:
            self.button_highlight_colour = button_highlight_colour
        else:
            self.button_highlight_colour = "#D74B4B"
        if button_shadow_colour:
            self.button_shadow_colour = button_shadow_colour
        else:
            self.button_shadow_colour = "#354B5E"

        # button colours disabled
        if self.disabled:
            self.button_colour = "#767676"
            self.button_shadow_colour = "#555555"

        self.top_rect = pygame.Rect(position, (width, height))
        self.top_colour = self.button_colour

        self.bottom_rect = pygame.Rect(position, (width, height))
        self.bottom_colour = self.button_shadow_colour

        self.text_surface = text_font.render(text, True, text_colour)
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def check_if_clicked(self) -> None:
        cursor_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(cursor_pos):
            self.top_colour = self.button_highlight_colour
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    if self.command:
                        self.command()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = self.button_colour

    def draw(self) -> None:
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.surface, self.bottom_colour, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.surface, self.top_colour, self.top_rect, border_radius=12)
        self.surface.blit(self.text_surface, self.text_rect)

        if not self.disabled:
            self.check_if_clicked()


class ImageButton:
    def __init__(self, surface: pygame.surface.Surface, image: pygame.surface.Surface, position: Tuple[int, int], command = None):
        self.image = image
        self.surface = surface
        self.position = position
        self.rect = image.get_rect(topleft=position)
        self.command = command

    def check_if_clicked(self, events):
        cursor_pos = pygame.mouse.get_pos()
        for event in events:
            if self.rect.collidepoint(cursor_pos[0], cursor_pos[1]) and event.type == pygame.MOUSEBUTTONDOWN:
                self.command()

    def draw(self, events: List[pygame.event.Event]):
        self.surface.blit(self.image, self.rect)
        self.check_if_clicked(events)
