import pygame
import random
import time
from raquette import Raquette

pygame.init()

class Balle(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran, raquette):
        super().__init__()#permet d'apporter les sprite avec le parametre de la class
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.hauteur = 500
        self.largeur = 500
        self.raquette = raquette
        self.raquette_goup = pygame.sprite.Group()
        self.raquette_goup.add(self.raquette)
        self.image = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/tenis.png")
        self.rect = self.image.get_rect()
        self.chute = 5
        self.rect.x = random.randint(30, largeur_ecran - 24)
        self.velocity = [random.randint(1, 2), random.randint(1, 2)]
        self.tentatives = 0
        self.tentatives_max = 10
        self.font = pygame.font.Font('freesansbold.ttf', 10)
        self.over_font = pygame.font.Font('freesansbold.ttf', 10)
        self.over_text = self.over_font.render("GAME OVER", True, (0, 0, 0))
        self.score = self.font.render("SCORE : " + str(self.tentatives), True, (255, 255, 255))
        self.gagner = self.font.render("TU AS GAGNE ! " + str(self.tentatives), True, (51, 255, 66))




    def repositionnement(self):
        self.rect.x = random.randint(24, self.largeur_ecran - 24)
        self.rect.y = 0 - self.image.get_height() #permet de se repositionner en max sur y
        self.chute = 2

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-10, -8)#direction hazard
        self.chute = random.randint(1, 5)

    def rebondir(self):

        if self.rect.y > self.largeur_ecran:
            self.velocity[1] = +self.velocity[1]
        elif self.rect.x < self.largeur_ecran:
            self.velocity[0] = -self.velocity[0]
        elif self.rect.y < self.hauteur_ecran:
            self.velocity[1] = -self.velocity[1]
        elif self.rect.x > self.hauteur_ecran:
            self.velocity[0] = +self.velocity[0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def printcollision(self): #collisions avec les murs
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]  # direction hazard
        self.chute = random.randint(1, 5)

    def gravite(self):
        self.raquette_goup.update()
        self.rect.y += self.chute
        hits = pygame.sprite.spritecollide(self, self.raquette_goup, False) #spritecollide
        if self.rect.top <= 0 or self.rect.bottom >= self.hauteur_ecran:#+self.image.get_height
            self.printcollision()
        if self.rect.left <= 0 or self.rect.right >= self.largeur_ecran:#+ self.image.get_width
            self.velocity[1] += self.velocity[1]
        if hits:
            print(f"il y a collision en y, {self.rect.y}")
            self.raquette.ajouter_points()
            self.rebondir()
            self.update()
            self.bounce()
            #rajouter tentatives
        elif self.rect.y >= 460:
            print(f"il y a collision en x, {self.rect.x}")
            self.raquette.enlever_points()
            self.tentatives -= 1
            if self.tentatives < 0:
                self.score = self.over_text
                pygame.quit()
            elif self.tentatives == self.tentatives_max:
                self.score = self.gagner
            elif self.tentatives != 0 and self.tentatives != self.tentatives_max:
                self.repositionnement()
                time.sleep(2)
        if self.rect.y != 300 and self.rect.y == 300:
            self.rect.y += self.velocity[1]
