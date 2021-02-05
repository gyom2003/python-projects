import pygame
from pygame.locals import *
import time
import sys
import random



width = 420
height = 580
ecran = pygame.display.set_mode((width, height))
pygame.display.set_caption("JumpGame")
limite = pygame.Rect(0, 0, 420, 580) #x, y, largeur (width), hauteur (height)


class Joeur(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

        #redefinission rect en fonction joueur pour préparer les sprites
        #self.image = pygame.Surface((25, 25))
        #self.image.fill((255, 153, 51)) #255, 153, 51
        #self.rect_mage = self.image.get_rect()
        self.largeur_ecran = 420
        self.hauteur_ecran = 580
        self.vec = pygame.math.Vector2
        self.vel = 3
        self.pos = (width / 2, height / 2)
        #initier les valeurs pour le saut
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.nbr_saut = 0
        self.a_sauter = False

        #dessiner sol et gravite
        self.sol = Sol()
        self.gravite = (0, 10)
        self.resistance = (0, 0)
        self.ajustement = 8

    def draw(self, ecran):
        pygame.draw.rect(ecran, self.color, self.rect)
        self.sol.afficher(ecran) #afficher remplace la methode pygame.draw.rect dans la class sol



    def move(self):
        keys = pygame.key.get_pressed()
        self.y += self.gravite[1] + self.resistance[1] # donc descent en 0 sur l'axe des y
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel


        if keys[pygame.K_RIGHT] and self.x + 27 < self.largeur_ecran:
            self.x += self.vel


        if keys[pygame.K_UP]:
            if self.saut_descente:
                if self.saut_montee >= 2: #si atteint max 10 saut descente = saut = self.rect.y -= 1
                    self.saut_descente -= 1
                    self.saut = self.saut_descente
                else:
                    self.saut_montee += 1 #si < 10 saut_montee += 1 saut montee = self.saut = self.rect.y
                    self.saut = self.saut_montee
                if self.saut_descente < 0: #sinon on re initialise les valeursd
                    self.saut_montee = 0
                    self.saut_descente = 5
                    self.a_sauter = False
            self.y = self.y - (10 * (self.saut / 2))

        if keys[pygame.K_DOWN]:
            pass

        self.rect_sol = pygame.Rect(0, 500, 420, 80)
        self.rect_sol1 = pygame.Rect(30, 450, 100, 20)
        self.rect_sol2 = pygame.Rect(200, 400, 100, 20)

        hit = self.sol.rect_sol.colliderect(self.rect) #pygame.sprite.spritecollide(self, self.rect_sol, False)
        if hit:
            ##print(self.x, self.y)
            self.resistance = (0, -10)
            if self.y == 490:
                self.y = 477

        hit_p1 = self.sol.rect_sol1.colliderect(self.rect)
        if hit_p1:
            self.y = self.rect_sol1[1] - 20


        self.rect = (self.x, self.y, self.width, self.height)


class Sol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect_sol = pygame.Rect(0, 500, 420, 80)
        self.rect_sol1 = pygame.Rect(30, 450, 100, 20)
        self.rect_sol2 = pygame.Rect(200, 400, 100, 20)

    def afficher(self, ecran):
        pygame.draw.rect(ecran, (51, 255, 110), self.rect_sol)
        pygame.draw.rect(ecran, (51, 255, 110), self.rect_sol1)
        pygame.draw.rect(ecran, (51, 255, 110), self.rect_sol2)


def redrawWindow(ecran,joeur): #pour etre remplacé par j
    ecran.fill((51, 221, 255))
    joeur.draw(ecran)
    joeur.move()
    pygame.draw.rect(ecran, (255, 0, 0), limite, 2) #dessiner limite sur l'ecran en rouge avec une epaisseur de 2
    pygame.display.update()



run = True
j = Joeur(180, 300, 25, 25, (255, 153, 51)) #pour la boucle et fonction redraw
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawWindow(ecran, j)

pygame.quit()
