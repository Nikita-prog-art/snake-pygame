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
        else:
            global gameRunning
            print("Can't equlas these objects")
            exit()

    def __eq__(self, other):
        if isinstance(other, Vector2):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        elif isinstance(other, tuple):
            if self.x == other[0] and self.y == other[1]:
                return True
            else:
                return False
        else:
            global gameRunning
            print("Can't match these objects:", type(self), type(other))
            exit()

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

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

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
