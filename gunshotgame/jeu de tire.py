import pygame
from pygame.mixer import Sound
import random
import time
import sys
import os

pygame.init()
from pygame.mixer import Sound

clock = pygame.time.Clock()
WIDTH = 450
HEIGHT = 450
pygame.display.set_caption("jeu de tire")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/gunshotgame/fond.png")
pygame.mouse.set_visible(False)

class Viseur(pygame.sprite.Sprite):
    def __init__(self, filepath):
        super().__init__()
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        #self.gunsound = pygame.mixer.Sound.set_volume(self.gunsound, 4)
        self.gunsound = pygame.mixer.Sound('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/gunshotgame/gun.wav')


    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def gunshot(self):
        self.gunsound.play()

class Cible(pygame.sprite.Sprite):
    def __init__(self, filepath, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def message(self):
        print("test")

#creation viseur avec la classe Viseur
viseur = Viseur("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/gunshotgame/ciblemouse.png")
viseur_group = pygame.sprite.Group()
viseur_group.add(viseur)
viseur_group.update()
#creation cible avec la classe Cible

cible_group = pygame.sprite.Group()
for cible in range(10):
    nouvelle_cible = Cible("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/gunshotgame/Cible1.png", random.randrange(0, WIDTH - 60), random.randrange(0, HEIGHT - 60))
    cible_group.add(nouvelle_cible)
    cible_group.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            viseur.gunshot()
            viseur.update()
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        viseur_group.draw(screen)
        cible_group.draw(screen)
        viseur_group.update()
        clock.tick(45)
