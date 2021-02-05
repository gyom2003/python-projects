import pygame

import time
pygame.init()


class Raquette(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()  # permet d'apporter les sprite avec le parametre de la class
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.image = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/sports.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() / 2
        self.rect.y = (hauteur_ecran - 180)
        self.position_raquette = [self.rect.x + self.rect.y]
        self.vitesse = 6
        self.tentatives = 0
        self.tentatives_max = 10

    def deplacement_droite(self):
        if self.rect.x + 70 < self.largeur_ecran: #ou self.rect.x + self.image.get_width()
            self.rect.x += self.vitesse

    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse

    def ajouter_points(self):
        if self.tentatives + 0.5 <= self.tentatives_max: #fixer une limite gagne 5 perd 2pt
            print("+ 5 pt")
            self.tentatives += 0.5
        elif self.tentatives >= self.tentatives_max:
            print("tu as gagné")

    #enlever les points oeufs touche le sol)
    def enlever_points(self):
        if self.tentatives - 0.5 > 0:
            self.tentatives -= 0.5
            print("- 2 pt")
        else:
            print("tu as perdus")
