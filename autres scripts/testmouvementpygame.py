import time

import pygame

pygame.init()
pygame.display.set_caption("test collision")
largeur = 500
hauteur = 500
ecran = pygame.display.set_mode((largeur, hauteur))
#variables du player
Player = pygame.Rect(250, 470, 30, 30)
myblock = pygame.Rect(300, 470, 30, 70)
blanc = (225, 255, 255)
vert = (0, 255, 0)



les_touches = {}
clock = pygame.time.Clock()
run = True
while run:
    pygame.draw.rect(ecran, blanc, Player)
    pygame.draw.rect(ecran, vert, myblock)
    ecran.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            if les_touches.get(pygame.K_RIGHT):
                pass
            elif les_touches.get(pygame.K_LEFT):
                pass
                les_touches = True
        if event.type == pygame.KEYDOWN:
            les_touches = True
        elif event.type == pygame.KEYUP:
            les_touches = False
    pygame.display.update()
    clock.tick(50)
pygame.quit()
