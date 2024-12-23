import pygame
import os

pygame.init()
pygame.mouse.set_visible(False)
size = 500, 500
screen = pygame.display.set_mode(size)
image = pygame.image.load('arrow.png')
running = True
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(all_sprites)
sprite.image = image
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
rect = pygame.rect.Rect(0, 0, 500, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if rect.collidepoint(event.pos):
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                sprite.rect.x = event.pos[0]
                sprite.rect.y = event.pos[1]
                all_sprites.draw(screen)
                pygame.display.flip()
        else:
            screen.fill((0, 0, 0))
            pygame.display.flip()