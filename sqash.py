# squash pygame implementation

import pygame, sys

s_width = 1200
s_height = 600
border = 20
ball_radius = 10


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_ball(self, surface, color):
        pygame.draw.circle(surface=surface, color=color, center=(self.x, self.y), radius=ball_radius)

    def update(self):
        pass


class Paddle:
    paddle_width = 20
    paddle_height = 80

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_paddle(self, surface, color):
        pygame.draw.rect(surface, color, (self.x, self.y, Paddle.paddle_width, Paddle.paddle_height))

    def update(self):
        pass


pygame.init()
screen = pygame.display.set_mode((s_width, s_height))

fg_color = pygame.Color("green")

pygame.draw.rect(screen, fg_color, (0, 0, s_width, border))
pygame.draw.rect(screen, fg_color, (0, s_height, s_width, -border))
pygame.draw.rect(screen, fg_color, (0, 0, border, s_height))

ball = Ball(s_width - ball_radius - Paddle.paddle_width, s_height // 2 - ball_radius)
ball.show_ball(screen, color=pygame.Color("white"))

pdd = Paddle(s_width - Paddle.paddle_width, s_height // 2 - Paddle.paddle_height)
pdd.show_paddle(screen, fg_color)

pygame.display.flip()

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
