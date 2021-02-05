# game options/settings
TITLE = "Jumpgame!"
WIDTH = 480
HEIGHT = 600
FPS = 70
FONT_NAME = 'arial'
FILE = "hightscore.txt"
SPRITESHET = "spritesheet_jumper.png" #charger a partir du tileset qu'on trouve avec dir et img_dir
 #nom de base qu'on change en fonction de l'image avec filename dans sa classe
#liste des plateformes

PLATEFORMES_LISTES = [(0, HEIGHT - 40, WIDTH, 40),
                      (220, HEIGHT - 140, 100, 20),
                      (80, HEIGHT - 200, 100, 20),
                      (350, HEIGHT - 250, 80, 20),
                      (175, 140, 100, 20)]
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (33, 183, 251)
YELLOW = (255, 255, 0)
GREY = (158, 155, 154)
ORANGE = (251, 127, 3)

#player mouvement
PLAYER_ACC = 0.6
PLAYER_FRICTION = -0.08
PLAYER_GRAV = 0.8

