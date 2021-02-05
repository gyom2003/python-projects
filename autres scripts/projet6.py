import pygame
import random
import time

pygame.init()
WIDTH = 500
HEIGHT = 500
pygame.display.set_caption("test collision rect, prites")
ecran = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

block_1 = pygame.Rect(250, 400, 20, 20)
block_2 = (200, 100, 25, 10)

def mouv():
    pass

def draw():
    pygame.draw.rect(ecran, (255, 255, 255), block_1)
    pygame.draw.rect(ecran, (0, 255, 0), block_2)

def bounce():
    pass


run = True
while run:
    draw()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    pygame.quit()
