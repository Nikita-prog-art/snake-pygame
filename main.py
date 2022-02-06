import pygame, random
from pygame import Color as palette

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return(Vector2(self.x + other.x, self.y + other.y))
        elif isinstance(other, tuple):
            return(Vector2(self.x + other[0], self.y + other[1]))

cell_size = 40

def draw_rect(x, y, surface, color):
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(surface, color, rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
    
    def draw_snake(self):
        for block in self.body:
            draw_rect(block.x, block.y, screen, palette('lime'))

    def move_snake(self):
        self.body = self.body[:-1]
        block = self.body[0]
        self.body.insert(0, self.body[0] + self.direction)

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

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == SCREEN_UPDATE:
            snake.move_snake()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)

    screen.fill(grassColor)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
