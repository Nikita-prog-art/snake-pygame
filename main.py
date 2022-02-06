import pygame, random

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_width - 1)
        self.y = random.randint(0, cell_height - 1)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()
cell_size = 40
cell_width = 20
cell_height = 15
screen = pygame.display.set_mode((cell_width * cell_size, cell_height * cell_size))
clock = pygame.time.Clock()
grassColor = (175, 215, 70)
gameRunning = True

fruit = FRUIT()

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    screen.fill(grassColor)
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
