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
sprite1.rect = sprite1.image.get_rect() 
