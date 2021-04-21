import pygame
from random import randint
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
sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75, 75))
sprite1.image.fill((255, 0, 0))
sprite1.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((75, 75))
sprite2.image.fill((0, 255, 0))
sprite2.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
all_group = pygame.sprite.Group([sprite2, sprite1])
iter=0
test_group = pygame.sprite.Group(sprite2)
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            if(y-10)>0:
                y = y - 10
            else:
               print("You are on edge.")
        if pressed[K_DOWN]:
            if(y+10)<800:
                
                    y = y + 10
            else:
                print("You are on edge.")
        if pressed[K_LEFT]:
            x = x - 10
        if pressed[K_RIGHT]:
            x = x + 10
        if x>=800 or x<=0:
            print("You're outside the window!")
        if y>=800 or y<=0:
            print("You're outside the window!")
    #print("Game is running")
    #screen.blit(background_image, [0, 0])
    screen.blit(pygame.transform.scale(background_image, (800, 800)), (0, 0))
    screen.blit(text, textRect)
    #pygame.draw.polygon(screen, BLACK, [[x+10, y+10], [x+0, y+20], [x+20, y+20]], 5)
    #inside loop
    sprite1.rect.centerx = x
    sprite1.rect.centery = y
    all_group.draw(screen)
    iter+=1
    if iter % 2 == 0:
        sprite2.rect.centerx = sprite2.rect.centerx + randint(1, 20)
        sprite2.rect.centery = sprite2.rect.centery + randint(1, 20)
    else:
        sprite2.rect.centerx = sprite2.rect.centerx - randint(1, 20)
        sprite2.rect.centery = sprite2.rect.centery - randint(1, 20)
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)
    for s in collide:
        print('collision')
    pygame.display.flip()
    clock.tick(clock_tick_rate)
