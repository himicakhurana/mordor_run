import pygame
from pygame.locals import *
# initialize game engine
pygame.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
window_width=800
window_height=800

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)

screen = pygame.display.set_mode(size, HWSURFACE | DOUBLEBUF | RESIZABLE)
# Set title to the window
pygame.display.set_caption("Mordor Run")

dead=False
path="/Users/schuylerb22/Desktop/thumb-1920-85585.jpg"
clock = pygame.time.Clock()
background_image = pygame.image.load(path).convert()
x, y = 250, 200
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score : 0', True, GREEN, BLUE)
textRect = text.get_rect()
textRect.center = (100,100)
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:  y = y - 10
        if pressed[K_DOWN]: y = y + 10
        if pressed[K_LEFT]:  x = x - 10
        if pressed[K_RIGHT]:  x = x + 10

    #print("Game is running")
    #screen.blit(background_image, [0, 0])
    screen.blit(pygame.transform.scale(background_image, (800, 800)), (0, 0))
    screen.blit(text, textRect)
    pygame.draw.polygon(screen, BLACK, [[x+10, y+10], [x+0, y+20], [x+20, y+20]], 5)
    pygame.display.flip()
    clock.tick(clock_tick_rate)
