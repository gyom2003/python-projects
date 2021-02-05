#remake snake avec ecran acueil à améliorer !!
import pygame
import random
import time
from pygame.font import *
import sys
pygame.font.init()
pygame.init()
pygame.display.set_caption("test collision")
largeur = 500
hauteur = 500
ecran = pygame.display.set_mode((largeur, hauteur))
#variables du player
#changer icon window
icon = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/mammal.png")
icon = pygame.transform.scale(icon, (15, 15))
pygame.display.set_icon(icon)
blanc = (225, 255, 255)
vert = (0, 255, 0)

class Joueur:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = [x, y, width, height]
        self.position_x = 200
        self.position_y = 200
        self.velocity = 3
        self.pomme_position_y = random.randrange(9, 475, 10)
        self.pomme_position_x = random.randrange(9, 470, 10)
        self.pomme = 10
        self.e = pygame.Rect(self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme) #random en x, y largeur, hauteur de 10
        self.position_serpend = []
        self.tete_serpend = []
        self.largeur_serpend = 10
        self.taille = 0
        self.menu = True
        self.score = 0
        self.image_pommes = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/mammal.png")
        #ecran.blit(self.image_tete(self.pomme_position_x, self.pomme_position_y, self.largeur_serpend, self.largeur_serpend))


    def draw(self, ecran):

        self.enemie = pygame.draw.rect(ecran, (255, 51, 51), self.e)
        self.joeur = pygame.draw.rect(ecran, (0, 255, 0),  self.rect)
        for partie_serpend in self.position_serpend:#il fat cree boucle for
            self.joeur = pygame.draw.rect(ecran, (0, 255, 0), (partie_serpend[0], partie_serpend[1], self.largeur_serpend, self.largeur_serpend))#pour la classe


        # les controles du joueur

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity
        self.rect = (self.x, self.y, self.width, self.height)

    #collision ecran
    def checkcollision(self):
        if self.x < 9 or self.x > 494 or self.y < 9 or self.y > 489:
            print("collision")
            pygame.quit()
        if self.joeur.colliderect(self.enemie):
            print("tu as mangé la pomme")
            self.e = pygame.Rect(random.randrange(9, 470, 10), random.randrange(9, 475, 10), self.pomme, self.pomme)
            self.taille += 1
            self.score += 1 #car il est dans le texte du score
        self.tete_serpend = []
        self.tete_serpend.append(self.x)
        self.tete_serpend.append(self.y)
        self.position_serpend.append(self.tete_serpend)#qui contient les coordonnées du serpend en x et y

        if len(self.position_serpend) > self.taille: #pour pas que la taille > sans toucher la pomme
            self.position_serpend.pop(0)
            #ecran.blit(self.image_tete(self.pomme_position_x, self.pomme_position_y, self.largeur_serpend, self.largeur_serpend))
        # si il se touche
        for partie_serpend in self.position_serpend[:0]: #pour ne pas prendre en compte la tete
            if partie_serpend == self.tete_serpend:
                sys.exit()

        self.dessiner_menu('moyenne', "Snake game", (200, 10, 100, 50), (255, 255, 255))
        self.dessiner_menu('moyenne', "{}".format(str(self.score)), (260, 50, 50, 50), (255, 255, 255))

    def dessiner_menu(self, font, message, message_rect, color):
        if font == 'petite':
            font = pygame.font.SysFont("Arial", 15, False, False)  # Sysfont(nom, taille, gras = Faux, italique = Faux)
        elif font == 'moyenne':
            font = pygame.font.SysFont("courier new", 20, False, True)
        elif font == 'grande':
            font = pygame.font.SysFont("comicsansms", 20, True, True)
        message = font.render(message, True, color)
        ecran.blit(message, message_rect)

class screenanimation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites_pommes = []
        self.sprites_pommes.append(pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/jumper animation/essaie/0.png"))
        self.sprites_pommes.append(pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/jumper animation/essaie/1.png"))
        self.sprites_pommes.append(pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/jumper animation/essaie/2.png"))
        self.sprites_pommes.append(pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/jumper animation/essaie/3.png"))
        self.sprites_pommes.append(pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/jumper animation/essaie/4.png"))
        self.current_speed = 0
        self.pommeimmage = self.sprites_pommes[self.current_speed]
        self.rect = self.pommeimmage.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def animated(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_speed += 0.2
            if self.current_speed >= len(self.sprites_pommes):
                self.current_speed = 0
            self.pommeimmage = self.sprites_pommes[int(self.current_speed)]




les_touches = {}
menu = True
run = True

image_menu = pygame.image.load("C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/entertainment.png")
image_menu = pygame.transform.scale(image_menu, (120, 120))
mouving_sprites = pygame.sprite.Group()
pomme = screenanimation(10, 10)

mouving_sprites.add(pomme)
#mouving_sprites.update()




j = Joueur(250, 250, 10, 10) #pour la boucle a partir des parametres de la classe
def redraww(ecran, joueur):#pour etre remplacé par j
    ecran.fill((0, 0, 0))
    pygame.draw.rect(ecran, (255, 255, 255), (9, 9, 485, 480), 3) #3 pour la largeur
    joueur.draw(ecran)
    joueur.checkcollision()
    joueur.move()

def dessiner_menu(font, message, message_rect, color):
    if font == 'petite':
        font = pygame.font.SysFont("Arial", 15, False, False) #Sysfont(nom, taille, gras = Faux, italique = Faux)
    elif font == 'moyenne':
        font = pygame.font.SysFont("courier new", 20, False, True)
    elif font == 'grande':
        font = pygame.font.SysFont("comicsansms", 20, True, True)
    message = font.render(message, True, color)
    ecran.blit(message, message_rect)

while menu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: #touche enter event.key, les touches.get(pygame.K_R...), key[pg.K...)
                menu = False
            if event.type == pygame.K_UP:
                pass
        #mouving_sprites.draw(ecran)
        #mouving_sprites.update()

        ecran.fill((0, 0, 0))
        dessiner_menu('petite', "tu dois atteindre un score maximal sans toucher les rebords",(100, 100, 200, 25), (255,255, 255))
        dessiner_menu('moyenne', "Pour cela tu dois manger des pommes", (30, 190, 200, 5), (255, 51, 51))
        dessiner_menu('grande', "presse sur enter pour commencer ta partie !", (0, 250, 200, 5), (51, 255, 51))
        ecran.blit(image_menu, (190, 350))
        pygame.display.flip()


while run:
    pygame.display.update()
    clock = pygame.time.Clock()
    ecran.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(50)
    redraww(ecran, j)#remplace par le joueur qui vient de la class Joeur dessiner par rect
pygame.quit()
