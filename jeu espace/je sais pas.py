import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600)) #largeur x  hauteur y  (width, height).
pygame.display.set_caption("jeu espace")
icon = pygame.image.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/ufo.png') #permet de rajouter un icone
background = pygame.image.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/background.png')
#musique background
mixer.music.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/background.wav')
mixer.music.play(-1) #pour que la musique se repete indefiniment

pygame.display.set_icon(icon)

#le joueur
playerImg = pygame.image.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/player.png')
playerX = 370
playerY = 480
playerX_change = 0

#l'enemie
#creation de plusieurs enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


#projectile parametre #ready (on ne le voit pas sur l'écran) à l'inverse de fire
bulletImg = pygame.image.load('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/bullet.png')
bulletX = 0
bulletY = 480 #car playerY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
#le score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32) #32 pixels dans le coin gauche en haut
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    #font.render afficher sur l'ecran le texte avec sa valeur, couleur...
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (250, 200))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy (x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10)) #meme avec l'axe y sur le vaisseau, il faut que celui ci soit au centre en faisant cela.

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY - bulletY, 2))
    #qui est egal a math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = -5
            if event.type == pygame.K_RIGHT:
                playerX_change = 5
            if event.type == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound = mixer.Sound('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/laser.wav')
                    bullet_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound = mixer.Sound('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/laser.wav')
                    bullet_sound.play()


    #collisions joueur
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #collisions enemy et mouvement
    for i in range(num_of_enemies): #rajouter ces mouvements (gauche, droite) et collisions dans la liste i []
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[i] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('C:/Users/jean-/AppData/Local/Programs/Python/Python38-32/pcproject/image/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    #bullet mouvement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change #dans l'axe y on retrécie la taille avec cette variable

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
pygame.quit()
