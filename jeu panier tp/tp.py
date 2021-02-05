#tp graven pygame
import pygame
from panier import Panier
from oeuf import Oeuf_chocolat
pygame.init()
largeur = 800
hauteur = 480
pygame.display.set_caption("Chasse aux oeufs")
ecran = pygame.display.set_mode((largeur, hauteur))
#les images les variables,
touches_actives = {}
fond = pygame.image.load(r"C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/assets/fond.jpg")
sol = pygame.image.load(r"C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/assets/sol.png")
panier = Panier(largeur, hauteur)
over_font = pygame.font.Font('freesansbold.ttf', 32)
over_text = over_font.render("GAME OVER", True, (0, 0, 0))
ecran.blit(over_text, (250, 200))
#creation barre de chocolat
barre_chocolat = pygame.image.load(r"C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/assets/chocolate.png")
barre_chocolat = pygame.transform.scale(barre_chocolat, (60, 60))
#creer le rect de la barre, couleur
chocolat_couleur = (87, 64, 53)

oeufs = pygame.sprite.Group()
oeufs.add(Oeuf_chocolat(largeur, hauteur, panier))
oeufs.add(Oeuf_chocolat(largeur, hauteur, panier))
running = True
while running:
    pygame.display.update()
    ecran.blit(fond, (0, 0))
    oeufs.draw(ecran) #au lieu de tout blit le sprite Oeuf_chocolat(largeur, hauteur...
    ecran.blit(panier.image, panier.rect) #ou panier.draw(ecran) pour tout les composants
    ecran.blit(sol, (0, 0))
    largeur_chocolat = panier.point * 3 - 20
    #dessiner l'arriere de la barre
    pygame.draw.rect(ecran, (51, 255, 82), [10, hauteur - 50, largeur - 20, 32])
    #appeler la fonction gravité de l'oeuf en plus de l'afficher su l'écran
    pygame.draw.rect(ecran, chocolat_couleur, [10, hauteur - 50, largeur_chocolat, 32]) #Surface, couleur, x, y, largeur, hauteur
    ecran.blit(barre_chocolat, (largeur_chocolat - barre_chocolat.get_width() / 2, 420))


    for oeuf in oeufs:
        oeuf.gravite()


    #print(touches_actives)
    if touches_actives.get(pygame.K_RIGHT):
        panier.deplacement_droite()
    elif touches_actives.get(pygame.K_LEFT):
        panier.deplacement_gauche()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            touches_actives[event.key] = True #au lieu de copier dans Keyup ou encore avec la variable keys = pygame.key.get_presse()
        elif event.type == pygame.KEYUP:
            touches_actives[event.key] = False
