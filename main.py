import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
grassColor = (175, 215, 70)
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    screen.fill(grassColor)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
