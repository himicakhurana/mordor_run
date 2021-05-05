from random import randint

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75, 75))
sprite1.image.fill((255, 0, 0))
sprite1.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((75, 75))
sprite2.image.fill((0, 255, 0))
sprite2.rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(75, 75)
all_group = pygame.sprite.Group([sprite2, sprite1])
test_group = pygame.sprite.Group(sprite2)
iter = 0

#inside loop

sprite1.rect.centerx = x
sprite1.rect.centery = y
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


all_group.draw(win)
###### adding image to characters
sprite1.image = pygame.image.load("image_path.png").convert()
sprite1.image = pygame.transform.scale(sprite1.image, (75,75))
sprite1.image = sprite1.image.convert_alpha()
sprite1.rect = sprite1.image.get_rect() 


#make character jump
#outside the loop
is_jump = False
# velocity 
v = 10
#mass
m = 1

###inside loop for jump

    if is_jump == False:

        # if space bar is pressed
        if keys[pygame.K_SPACE]:
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

            # setting original values to v and m
            v = 10
            m = 1
            #time stuff.
            #outside loop
   start_time = pygame.time.get_ticks()
   current_time= pygame.time.get_ticks()
   
####################################move obstacle closer to character
dirvect = pygame.math.Vector2(x - sprite2.rect.centerx,
                                      y - sprite2.rect.centery)
dirvect.normalize()
# Move along this normalized vector towards the player at current speed.
dirvect.scale_to_length(10)
sprite2.rect.move_ip(dirvect)
