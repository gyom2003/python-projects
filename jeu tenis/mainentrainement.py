import pygame
from la_balle import Balle

from raquette import Raquette
from raquette import Raquette
import time
#la fenetre
pygame.init()
largeur = 500 #x
hauteur = 500 #y
pygame.display.set_caption("jeu tennis")
ecran = pygame.display.set_mode((largeur, hauteur))
les_touches = {}
fond = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/real-estate.png")
pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/deportes.png")
balle = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/tenis.png")
clock = pygame.time.Clock()#pour avoir l'objet tick
gris = (128, 128, 128)
noir = (0, 0, 0)
tentatives = 0
tentative_max = 10
dessin = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/sports-and-competition.png")
dessin = pygame.transform.scale(dessin, (50, 50))

raquette = Raquette(largeur, hauteur)
bal = Balle(largeur, hauteur, raquette)
largeur_barre = bal.tentatives

ballegroup = pygame.sprite.Group()
ballegroup.add(Balle(largeur, hauteur, raquette))

def printtentatives():
    pygame.display.init()
    if bal.rect.y >= 460:
        bal.tentatives -= 1
        if bal.tentatives == 0:
            ecran.blit(bal.over_text, (255, 255))
            pygame.quit()
        elif bal.tentatives == bal.tentatives_max:
            ecran.blit(bal.gagner, (255, 255))
        elif bal.tentatives != 0 and bal.tentatives != bal.tentatives_max:
            ecran.blit(bal.score, (10, 10))
            bal.repositionnement()
            time.sleep(2)

def dessiner():
    printtentatives()
    ecran.blit(bal.score, (10, 10))
    ecran.fill(gris)
    ecran.blit(fond, (0, 0))
    ecran.blit(raquette.image, raquette.rect)
    ballegroup.draw(ecran)
    pygame.draw.rect(ecran, (51, 255, 66), [10, hauteur - 50, largeur - 20, 32])
    pygame.draw.rect(ecran, (255, 51, 51), [10, hauteur - 50, largeur_barre, 32])
    #ecran.blit(dessin, (largeur_barre - int(dessin.get_width / 2)))

    pygame.display.update()
    ballegroup.update()


#main loop
run = True
while run:
    pygame.display.update()
    dessiner()
    for balle in ballegroup:
        ballegroup.remove(balle)
        balle.gravite()
        ballegroup.add(balle)

    if les_touches.get(pygame.K_RIGHT):
        raquette.deplacement_droite()
        #Raquette.deplacement_droite()
    elif les_touches.get(pygame.K_LEFT):
        raquette.deplacement_gauche()
        #Raquette.deplacement_gauche()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            les_touches[event.key] = True
        elif event.type == pygame.KEYUP:
            les_touches[event.key] = False
    clock.tick(30)
