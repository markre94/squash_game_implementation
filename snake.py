import pygame, sys, random


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake game implementation')

        self.disp_width = 900
        self.disp_height = 600
        self.screen = pygame.display.set_mode((self.disp_width, self.disp_height))
        self.box = pygame.Rect(450, 300, 10, 10)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.snake()
            self.move()
            pygame.display.flip()

    def snake(self):
        # pygame.draw.rect(surface=self.screen, color=(0, 200, 255), rect=self.box)

        # Drawing
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(surface=self.screen, color=(0, 200, 255), rect=self.box)
        # pygame.draw.circle(surface=screen, color=(0, 200, 100), center=circle_pos, radius=10)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_d]:
            self.box.x += 10
        elif keys [pygame.K_a]:
            self.box.x -= 3
        elif keys [pygame.K_w]:
            self.box.y -= 3
        elif keys [pygame.K_s]:
            self.box.y += 3

        if self.box.x == self.disp_width or self.box.x == 0:
            pass
        elif self.box.y == self.disp_height or self.box.y == 0:
            pass


if __name__ == '__main__':
    game = Game()
    game.main()
