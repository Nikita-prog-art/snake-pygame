import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill('blue')
test_rect = test_surface.get_rect(topright = (200 ,250))
grassColor = (175, 215, 70)
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    screen.fill(grassColor)
    test_rect.right += 1
    screen.blit(test_surface, test_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
