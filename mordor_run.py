# Import and initialize the pygame library
import pygame
import time
from pygame.locals import *
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
# Set up the drawing window
screen = pygame.display.set_mode((800, 800), HWSURFACE | DOUBLEBUF | RESIZABLE)
#screen = pygame.display.set_mode([1000, 1000])
image=pygame.image.load(r'/Users/schuylerb22/Desktop/thumb-1920-85585.jpg')
#screen.blit(image, (0, 0))
#screen.fill((255, 255, 255))
screen.blit(pygame.transform.scale(image, (800, 800)), (0, 0))
game_running=True
while game_running:
    time.sleep(1)

    print("Game is running")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((245, 218, 218))
    image=pygame.image.load(r'/Users/schuylerb22/Desktop/thumb-1920-85585.jpg')
    screen.blit(image, (0, 0))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    #pygame.draw.polygon(screen, green, ((25,75+200),(75+200,125+200),(126+200,26)))



time.sleep(1)
pygame.quit()
