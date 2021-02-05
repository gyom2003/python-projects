#avec rect
import pygame
import random
import time
import sys
pygame.init()
WIDTH = 500
HEIGHT = 500
pygame.display.set_caption("test collision rect")
ecran = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# quelque variables
vitesse_x, vitesse_y = 5, 4
block2_vx, block2_vy = 2, 3
collision_tolerance = 10

block_1 = pygame.Rect(250, 400, 45 , 50)
block_2 = pygame.Rect(200, 100, 45, 40)


def draw_b_m():
    global vitesse_x, vitesse_y, block2_vx, block2_vy, collision_tolerance
    pygame.draw.rect(ecran, (255, 255, 255), block_1)
    pygame.draw.rect(ecran, (0, 255, 0), block_2)
    block_1.x += vitesse_x
    block_1.y += vitesse_y
    block_2.x += block2_vx
    block_2.y += block2_vy
    #sur les limite de l'écran
    if block_1.right >= WIDTH or block_1.left <= 0: #comme il avance se sera le coté droit qui sera en coll en x, Width
        vitesse_x *= -1
    if block_1.bottom >= HEIGHT or block_1.top <= 0: #en y Height
        vitesse_y *= -1
    #checker les collision des rebord avec le second rect
    if block_2.right > WIDTH or block_2.left <= 0:
        block2_vx *= -1
    if block_2.bottom > WIDTH or block_2.top <= 0:
        block2_vy *= -1
    #collision entre les rect et leurs positions
    if block_1.colliderect(block_2):
        if abs(block_2.top - block_1.bottom) < collision_tolerance:
            vitesse_y *= -1
        if abs(block_2.bottom - block_1.top) < collision_tolerance:
            vitesse_y *= -1
        if abs(block_2.left - block_1.right) < collision_tolerance - 5:
            vitesse_y *= -1
        if abs(block_2.right - block_1.left) < collision_tolerance - 5:
            vitesse_y *= -1
    #clecker les collisions à partir du block 2
    if block_2.colliderect(block_1):
        if abs(block_1.top - block_2.bottom) < collision_tolerance:
            block2_vy *= -1
        if abs(block_1.bottom - block_2.top) < collision_tolerance:
            block2_vy *= -1
        if abs(block_1.left - block_2.right) < collision_tolerance - 5:
            block2_vy *= -1
        if abs(block_1.right - block_2.left) < collision_tolerance - 5:
            block2_vy *= -1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    ecran.fill((30, 30, 30))
    draw_b_m()
    pygame.display.flip()
    clock.tick(50)

#avec les prites
