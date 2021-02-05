
import pygame as pg
from os import path
import random
import time
from jump_g.settings import *

vec = pg.math.Vector2

class Spritesheet:
    #couper et remplacer les images dans le jeu
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = pg.Surface((int(width), int(height)))
        image.blit(self.spritesheet, (0, 0)) #, (x, y, width, height)
        image = pg.transform.scale(image, (30, 30))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.load_image()
        self.image = self.standing_frame[0] #self.game.spritesheets.get_image("614", "1063", "120", "191")
        self.image.set_colorkey(BLACK)
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0 #vitesse de l'animation
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_image(self):
        # amenner les iamges avec filename dans la classe Spritesheet
        self.standing_frame = [self.game.spritesheet.get_image("614", "1063", "120", "191"),
                                self.game.spritesheet.get_image("690", "406", "120" , "201")]

        self.walking_frame = [self.game.spritesheet.get_image("678", "860",  "120", "201"),
                                self.game.spritesheet.get_image("692", "1458", "120", "201")]


        self.walking_frame_l = []
        for frame in self.walking_frame:
            self.walking_frame.append(pg.transform.flip(frame, True, False))  # hozitontale, verticale
        self.jump_frame = [self.game.spritesheet.get_image("382", "763", "150", "181")]

    def jump(self):#checker si il y a une plateforme sous le joueur avec val tolerance qui est de 1, si oui, il peut sauter
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms,  False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -18
    def update(self):
        self.acc = vec(0, PLAYER_GRAV) #0.8 pour tomber de 0.8 pixel en y car vel incrémenté de acc qui lui meme est multiplié par acc dans pos
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks() #car on fonctionne en pfs
        if not self.jumping and not self.walking:
            if now - self.current_frame > 200: #millisecondes
                self.last_update = now
                self.current_frame  = (self.current_frame + 1) % len(self.standing_frame)
                self.image = self.standing_frame[self.current_frame]

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self) #la surface prend que la largeur et la hauteur self.image = pg.Surface((w, h))
        self.image = pg.Surface((w, h))
        self.image.fill((GREY))
        self.rect = self.image.get_rect() #pas besoin de rect la position en x et y des plateformes
        self.rect.x = x
        self.rect.y = y

class Nuages(pg.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]



