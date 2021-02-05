import pygame
import random
class Oeuf_chocolat(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran, panier):
        super().__init__()
        self.panier = panier
        self.panier_group = pygame.sprite.Group()
        self.panier_group.add(self.panier)
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.vitesse_chute = random.randint(2, 4)
        self.image = pygame.image.load(r"C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/assets/oeuf.png")
        self.rect = self.image.get_rect() #recuperer l'imgage sous forme (pares on etablit x, y
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect.x = random.randint(20, largeur_ecran - 20) #demande les deux valeur max et min largeur_ecran = 800

    def repositionner(self):
        self.rect.x = random.randint(20, self.largeur_ecran - 20)
        self.rect.y = 0 - self.image.get_height()
        self.vitesse_chute = random.randint(1, 3)


    def gravite(self, ):
        self.rect.y += self.vitesse_chute
        #regarder les collisions
        if pygame.sprite.spritecollide(self, self.panier_group, False, pygame.sprite.collide_mask) and self.rect.y >= 350: #collisions entre deux sprite limite en y
            print(f"il y a collision, {self.rect.y}")

            self.repositionner()
            #ajouter les points
            self.panier.ajouter_points()
        if self.rect.y >= self.hauteur_ecran:
            #enlever les points
            self.panier.enlever_points()
            self.repositionner()
