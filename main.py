import pygame, random
from pygame import Color as palette
from vector2 import Vector2


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
        self.body.insert(0, self.body[0] + self.direction)

    def add_block(self):
        self.body.insert(0, self.body[0] + self.direction)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        draw_rect(self.pos.x, self.pos.y, screen, (126, 166, 114))

    def randomize(self):
        self.pos = Vector2(random.randint(0, cell_width - 1), random.randint(0, cell_height - 1))

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_death()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_death(self):
        if not 0 <= self.snake.body[0].x <= cell_width:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cell_height:
            self.game_over()

    def game_over(self):
        global gameRunning
        gameRunning = False

pygame.init()
cell_width = 20
cell_height = 15
screen = pygame.display.set_mode((cell_width * cell_size, cell_height * cell_size))
clock = pygame.time.Clock()
grassColor = (175, 215, 70)
gameRunning = True

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == SCREEN_UPDATE:
            main_game.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
    
    screen.fill(grassColor)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
