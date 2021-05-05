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

#pygame.mixer.music.load('02 Concerning Hobbits.mp3')
#pygame.mixer.music.play(0)
dead=False
path="/Users/schuylerb22/Desktop/thumb-1920-85585.jpg"
clock = pygame.time.Clock()
background_image = pygame.image.load('The_Shire.jpg').convert()
x, y = 75, 700
font = pygame.font.Font('freesansbold.ttf', 32)
score_text = font.render('Score : 0', True, GREEN, BLUE)
score_sprite = font.render('Score : 0', True, GREEN, BLUE)
health_text = font.render('Health : 100%', True, GREEN, BLUE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (100,100)
health_text_rect = health_text.get_rect()
health_text_rect.center = (500,100)
character_sprite = pygame.sprite.Sprite()
obstacle1_sprite = pygame.sprite.Sprite()
#sprite2.image.fill((0, 255, 0))
#sprite2.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
character_sprite.image = pygame.image.load("Character.png").convert()
character_sprite.image = pygame.transform.scale(character_sprite.image, (75,75))
character_sprite.image = character_sprite.image.convert_alpha()
character_sprite.rect = character_sprite.image.get_rect()
score_sprite = pygame.sprite.Sprite()
score_sprite.image = pygame.image.load("Untitled_Artwork 4.png").convert()
score_sprite.image = pygame.transform.scale(score_sprite.image, (75,75))
score_sprite.image = score_sprite.image.convert_alpha()
score_sprite.rect = score_sprite.image.get_rect()
obstacle1_sprite.image = pygame.image.load("Untitled_Artwork 3.png").convert()
obstacle1_sprite.image = pygame.transform.scale(obstacle1_sprite.image, (75,75))
obstacle1_sprite.image = obstacle1_sprite.image.convert_alpha()
obstacle1_sprite.rect = obstacle1_sprite.image.get_rect()
health_sprite = pygame.sprite.Sprite()
health_sprite.image = pygame.Surface((75, 75))
health_sprite.image.fill((3, 252, 232))
health_sprite.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
all_group = pygame.sprite.Group([obstacle1_sprite, score_sprite, character_sprite, health_sprite])
iter=0
score_group = pygame.sprite.Group(score_sprite)
test_group = pygame.sprite.Group(obstacle1_sprite)
health_group = pygame.sprite.Group(health_sprite)
score=0
health=100
is_jump = False
# velocity
v = 10
start_time = pygame.time.get_ticks()
#mass
m = 1
obstacle1_sprite.rect.centerx=800
while(dead==False):
    if health == 0 :
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        pressed = pygame.key.get_pressed()
        if is_jump == False:

        # if space bar is pressed
            if pressed[pygame.K_SPACE]:
            # make isjump equal to True
                is_jump = True
    if is_jump:
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F = (1 / 2) * m * (v ** 2)

        # change in the y co-ordinate
        y -= F

        # decreasing velocity while going up and become negative while coming down
        v = v - 1

        # object reached its maximum height
        if v < 0:
            # negative sign is added to counter negative velocity
            m = -1

        # objected reaches its original state
        if v == -11:
            # making isjump equal to false
            is_jump = False
            x, y = 75, 700
            # setting original values to v and m
            v = 10
            m = 1

    #print("Game is running")
    #screen.blit(background_image, [0, 0])
    current_time= pygame.time.get_ticks()
    if current_time >= start_time + 5000:
        print("5 seconds have passed")
        start_time = current_time
        score= score+1
    screen.blit(pygame.transform.scale(background_image, (800, 800)), (0, 0))
    #screen.fill((255,255,255))
    health_message='Health : '+str(health)+'%'
    health_text = font.render(health_message, True, GREEN, BLUE)
    screen.blit(health_text, health_text_rect)
    #changing score message
    score_message='Score : '+str(score)
    score_text = font.render(score_message, True, GREEN, BLUE)
    screen.blit(score_text, score_text_rect)
    #pygame.draw.polygon(screen, BLACK, [[x+10, y+10], [x+0, y+20], [x+20, y+20]], 5)
    #inside loop
    character_sprite.rect.centerx = x
    character_sprite.rect.centery = y
    all_group.draw(screen)
    iter+=1
    #dirvect = pygame.math.Vector2(x - obstacle1_sprite.rect.centerx,
                                     # y - obstacle1_sprite.rect.centery)
    #dirvect.normalize()
# Move along this normalized vector towards the player at current speed.
    #dirvect.scale_to_length(10)rrrrrrrrrrrr
    #obstacle1_sprite.rect.move_ip(dirvect)
    x_position = obstacle1_sprite.rect.centerx - randint(0,40)
    if x_position > 75:
        obstacle1_sprite.rect.centerx = x_position
        obstacle1_sprite.rect.centery = 700
    else:
        obstacle1_sprite.rect.centerx = 800
        obstacle1_sprite.rect.centery = 700
    collide = pygame.sprite.spritecollide(character_sprite, test_group, False)
    for s in collide:
        health=health-20
        print('collision')
    health_collide = pygame.sprite.spritecollide(character_sprite, health_group, False)
    for s in health_collide:
        health=health+5
        print('health')
    score_collide = pygame.sprite.spritecollide(character_sprite, score_group, False)
    for s in score_collide:
        score=score+20
        print('score')
    pygame.display.flip()
    clock.tick(clock_tick_rate)
