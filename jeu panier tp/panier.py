import pygame

pygame.init()

class Panier(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__() #apporter les sprites
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.point = 0
        self.maximum_points = 100
        self.image = pygame.image.load(r"C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/assets/panier.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = (largeur_ecran / 2) - self.image.get_width() / 2 #x = 400 moin la moitié de la largeur de l'image (240)
        self.rect.y = (hauteur_ecran) - 175
        self.vitesse = 5


    #ajouter les points (attraper oeufs)

    def ajouter_points(self):
        if self.point + 5 <= self.maximum_points: #fixer une limite gagne 5 perd 2pt
            print("+ 5 pt")
            self.point += 5
        elif self.point >= self.maximum_points:
            print("tu as gagné")

    #enlever les points oeufs touche le sol)
    def enlever_points(self):
        if self.point - 2 > 0:
            self.point -= 2
            print("- 2 pt")
        else:
            print("tu as perdus")



    def deplacement_droite(self):
        if self.rect.x + 102 < self.largeur_ecran: #ou self.rect.x + self.image.get_width()
            self.rect.x += self.vitesse


    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse
