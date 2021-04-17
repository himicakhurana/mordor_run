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

#inside loop
all_group.draw(win)
