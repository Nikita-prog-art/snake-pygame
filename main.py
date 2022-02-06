import pygame, random
from pygame import Color as palette

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

cell_size = 40

def draw_rect(x, y, surface, color):
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(surface, color, rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    
    def draw_snake(self):
        for block in self.body:
            draw_rect(block.x, block.y, screen, palette('lime'))

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_width - 1)
        self.y = random.randint(0, cell_height - 1)

    def draw_fruit(self):
        draw_rect(self.x, self.y, screen, (126, 166, 114))

pygame.init()
cell_width = 20
cell_height = 15
screen = pygame.display.set_mode((cell_width * cell_size, cell_height * cell_size))
clock = pygame.time.Clock()
grassColor = (175, 215, 70)
gameRunning = True

fruit = FRUIT()
snake = SNAKE()

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    screen.fill(grassColor)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
