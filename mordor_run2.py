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

pygame.mixer.music.load('02 Concerning Hobbits.mp3')
pygame.mixer.music.play(0)
dead=False
path="/Users/schuylerb22/Desktop/thumb-1920-85585.jpg"
clock = pygame.time.Clock()
background_image = pygame.image.load(path).convert()
x, y = 250, 200
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score : 0', True, GREEN, BLUE)
health_text = font.render('Health : 100%', True, GREEN, BLUE)
textRect = text.get_rect()
textRect.center = (100,100)
health_text_rect = health_text.get_rect()
health_text_rect.center = (500,100)
sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75, 75))
sprite1.image.fill((255, 0, 0))
sprite1.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
obstacle1_sprite = pygame.sprite.Sprite()
#sprite2.image.fill((0, 255, 0))
#sprite2.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
obstacle1_sprite.image = pygame.image.load("Untitled_Artwork 3.png").convert()
obstacle1_sprite.image = pygame.transform.scale(obstacle1_sprite.image, (75,75))
obstacle1_sprite.image = obstacle1_sprite.image.convert_alpha()
obstacle1_sprite.rect = obstacle1_sprite.image.get_rect()
health_sprite = pygame.sprite.Sprite()
health_sprite.image = pygame.Surface((75, 75))
health_sprite.image.fill((3, 252, 232))
health_sprite.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
all_group = pygame.sprite.Group([obstacle1_sprite, sprite1, health_sprite])
iter=0
test_group = pygame.sprite.Group(obstacle1_sprite)
health_group = pygame.sprite.Group(health_sprite)
health=100
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        pressed = pygame.key.get_pressed()

    #print("Game is running")
    #screen.blit(background_image, [0, 0])
    #screen.blit(pygame.transform.scale(background_image, (800, 800)), (0, 0))
    screen.fill((255,255,255))
    health_message='Health : '+str(health)+'%'
    health_text = font.render(health_message, True, GREEN, BLUE)
    screen.blit(text, textRect)
    screen.blit(health_text, health_text_rect)
    #pygame.draw.polygon(screen, BLACK, [[x+10, y+10], [x+0, y+20], [x+20, y+20]], 5)
    #inside loop
    sprite1.rect.centerx = x
    sprite1.rect.centery = y
    all_group.draw(screen)
    iter+=1
    if iter % 2 == 0:
        obstacle1_sprite.rect.centerx = obstacle1_sprite.rect.centerx + randint(80, 100)
        obstacle1_sprite.rect.centery = obstacle1_sprite.rect.centery + randint(80, 100)
    else:
        obstacle1_sprite.rect.centerx = obstacle1_sprite.rect.centerx - randint(80, 100)
        obstacle1_sprite.rect.centery = obstacle1_sprite.rect.centery - randint(80, 100)
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)
    for s in collide:
        health=health-5
        print('collision')
    health_collide = pygame.sprite.spritecollide(sprite1, health_group, False)
    for s in health_collide:
        health=health+5
        print('health')
    pygame.display.flip()
    clock.tick(clock_tick_rate)
