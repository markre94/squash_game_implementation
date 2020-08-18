import pygame, sys

pygame.init()

screen = pygame.display.set_mode((900, 600))
x = 10
box = pygame.Rect(10, 10, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)


    #  Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box.x += 1
    elif keys[pygame.K_a]:
        box.x -= 1
    elif keys[pygame.K_w]:
        box.y -= 1
    elif keys[pygame.K_s]:
        box.y += 1

    # Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(surface=screen, color=(0, 200, 255), rect=box)

    pygame.display.flip()
