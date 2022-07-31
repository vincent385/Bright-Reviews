import sys
import pygame


class Client:
    width, height = (1366, 768)
    fps = 60

    def __init__(self):
        pygame.init()
        self.root = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bright Reviews")
        self.running = True

    def draw_root_window(self):
        self.root.fill((255, 0, 0))
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_root_window()


if __name__ == '__main__':
    client = Client()
    client.run()
