
import pygame as pg
import random
import time
from settings import *
from sprite import *
# ou
from jump_g.settings import *
from jump_g.sprite import *
import sys
from os import path
#class game se compose de tout les elements du main

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.pre_init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.menu = True
        self.load_data()

    def load_data(self):
        #charger le score le plus elevé
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "Players") #self.dir, "Animmation"
        #img_dir_walk = path.join(self.dir, "animation gauche")
        with open(path.join(self.dir, FILE), 'r') as f:#mode de lecture qui le créer et qui lis les valeurs
            try:
                self.hightscore = int(f.read())

            except:
                self.hightscore = 0
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHET)) #en fonction du tileset





    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATEFORMES_LISTES:
            p = Platform(*plat) #au lieu de plat[0], 1, 2, 3 pour chaque plateformes
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        pg.display.update()
        self.all_sprites.update()
        self.platforms.update()
        #self.nuage_group.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False) #self.plateforme pour pas tt mettre dans all sprite et coll avec joeur
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        #collision sur le coin de l'éran
        if self.player.rect.top <= (HEIGHT / 4): #si le haut du joeur est plus grand que 200 pix, sa pos en y + val max de sa velocité en y et aussi pr plat
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    self.score += 10
        #ecran scrolling
        if self.player.rect.bottom >= HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10) #ou la valeur extrème abs(self.vel.y)
                if sprite.rect.bottom < 0: #si elles sortent de l'écran elle sont supprimé
                    sprite.kill()
            if len(self.platforms) == 0: #et si il n'y a plus de plateformes on casse la boucle.
                self.playing = False
                self.show_go_screen()
                time.sleep(5)
        #generer des plateformes aléatoirements
        while len(self.platforms) < 6: #nombre de,plateformes dans l'écran
            width = random.randrange(50, 100)
            pl = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30), width, 20) #x, y, width, height pour y pour pas que les plateformes se touchent
            self.all_sprites.add(pl)
            self.platforms.add(pl)


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        pass
        # Game Loop - draw
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text("{}".format(str(self.score)), 22, (0, 0, 0), (WIDTH / 2), 10)



    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLUE)
        self.draw_text(TITLE, 45, WHITE, WIDTH / 2, 35)
        self.draw_text("les fleches pour bouger et la barre d'espace pour sauter", 25, WHITE, WIDTH / 2, 120)
        self.draw_text("appuie sur une touche pour jouer" ,30, BLACK, (WIDTH / 2), (HEIGHT / 2))
        self.draw_text(f"Hight score : {str(self.hightscore)}", 25, WHITE, WIDTH / 2, 15)
        pg.display.flip()#reinitialiser tout l'écran
        self.enter_press()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BLUE)
        self.draw_text("Game Over", 45, WHITE, WIDTH / 2, 35)
        self.draw_text("Score : " + (str(self.score)), 25, WHITE, WIDTH / 2, 120)
        self.draw_text("attend 5 secondes pour rejouer", 30, BLACK, (WIDTH / 2), (HEIGHT / 2))
        if self.score > self.hightscore:
            self.hightscore = self.score
            self.draw_text(f"Tu as battus ton record ! ", 25, WHITE, WIDTH / 2, (HEIGHT / 2) + 50)
            with open(path.join(self.dir, FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text(f"Hight score : {str(self.hightscore)}", 25, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.enter_press()


    def enter_press(self):
        while self.menu:
            for event in pg.event.get():
                self.clock.tick(FPS)
                if event.type == pg.QUIT:
                    self.menu = False
                    self.running = False
                    sys.exit()
                if event.type == pg.KEYUP:
                    self.menu = False

    def draw_text(self, text, size, color, x, y): # Sysfont(nom, taille, gras = Faux, italique = Faux)
        font = pg.font.SysFont(self.font_name, size, False, True)
        text_surface = font.render(text, True, color) #afficher le texte
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)#texte dur l'écran


g = Game()
g.show_start_screen()
while g.running:
    pg.display.update()
    g.new()
    g.show_go_screen()

pg.quit()
