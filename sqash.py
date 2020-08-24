# squash pygame implementation

import pygame, sys

# global variables

s_width = 1200
s_height = 600
border = 20
ball_radius = 10
velo = -10
framerate = 35


class Ball:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def show_ball(self, surface, color):
        pygame.draw.circle(surface=surface, color=color, center=(self.x, self.y), radius=ball_radius)

    # TODO
    def update(self):
        self.show_ball(screen, pygame.Color("black"))
        self.x += self.vel_x
        self.y += self.vel_y
        # self.show_ball(screen, fg_color)

        if self.y <= (border + ball_radius) \
                or self.y >= (s_height - border - ball_radius):
            self.vel_y = self.vel_y * -1
            # self.x += self.vel_x

        elif self.x == Paddle.paddle_width and abs(self.y - pdd_left.y) < Paddle.paddle_height:
            self.vel_x = self.vel_x * - 1
            # self.y += self.vel_y


        elif self.x == ball_radius + s_width - Paddle.paddle_width and abs(self.y - pdd.y) < Paddle.paddle_height:
            self.vel_x = self.vel_x * -1

        self.show_ball(screen, fg_color)

    # TODO
    def game_over(self):
        if self.x > s_width:
            print("Game over")
            sys.exit(0)


class Paddle:
    paddle_width = 20
    paddle_height = 80

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_paddle(self, surface, color):
        pygame.draw.rect(surface, color, (self.x, self.y, Paddle.paddle_width, Paddle.paddle_height))

    def update(self, key_up, key_down):
        self.show_paddle(screen, pygame.Color("black"))

        if pygame.key.get_pressed() [key_up] and self.y > border:
            self.y -= 15
        if pygame.key.get_pressed() [key_down] and self.y + Paddle.paddle_height < s_height - border:
            self.y += 15

        self.show_paddle(screen, fg_color)


pygame.init()
screen = pygame.display.set_mode((s_width, s_height))

fg_color = pygame.Color("green")

pygame.draw.rect(screen, fg_color, (0, 0, s_width, border))
pygame.draw.rect(screen, fg_color, (0, s_height + 1, s_width, -border))
# pygame.draw.rect(screen, fg_color, (0, 0, border, s_height))

ball = Ball(s_width - ball_radius - Paddle.paddle_width, s_height // 2, velo, velo)
ball.show_ball(screen, color=pygame.Color("white"))

pdd = Paddle(s_width - Paddle.paddle_width, s_height // 2 - Paddle.paddle_height // 2)
pdd.show_paddle(screen, fg_color)

pdd_left = Paddle(0, s_height // 2 - Paddle.paddle_height // 2)
pdd_left.show_paddle(screen, fg_color)

clock = pygame.time.Clock()
# Linear regression implementation

# sample = open('game.csv', "w")
# print("x,y,vx,vy, Paddle.y", file=sample)
# game loop

run = True

while run:
    e = pygame.event.poll()

    if e.type == pygame.QUIT:
        sys.exit(0)

    clock.tick(framerate)
    pygame.display.flip()
    ball.update()
    pdd.update(key_up=pygame.K_UP, key_down=pygame.K_DOWN)
    pdd_left.update(key_up=pygame.K_w, key_down=pygame.K_s)

    # print(f"{ball.x}, {ball.y}, {ball.vel_x}, {ball.vel_y}, {pdd.y}", file=sample)
