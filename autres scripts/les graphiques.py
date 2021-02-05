import turtle
from tkinter import *
import random
from tkinter.colorchooser import *

t = turtle.Pen()
w = turtle.Screen()
w.title("projet turtle")

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.clear()
t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)
t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)

t.reset()
t.color(1,1,0)
t.begin_fill()
t.circle(50)
t.end_fill()
#ou encore

def moncercle(rouge, vert, bleu):
    t.color(rouge, vert, bleu)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
moncercle(0, 1 ,0)
#def avec boucle
t.reset()
def moncarré(taille):
    for x in range(1, 5):
        t.forward(taille)
        t.left(90)
t.color(1, 0.5, 0)
t.color(0.9, 0.5, 0.15)


t.reset()
def monétoile(taille, plein):
    if plein == True:
        t.begin_fill() #debut remplissage
    for x in range(1, 19):
        t.forward(taille)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
    if plein == True:
        t.end_fill() #fin remplissage

t.color(0.9, 0.75, 0)

t.color(1,1,0)
t.begin_fill()
t.circle(50)
t.end_fill()

t.reset()
moncarré(25)
moncarré(50)
moncarré(60)
moncarré(70)

tk = Tk()
canvas = Canvas(tk, width=500, height =500)
canvas.pack()
mon_image = PhotoImage(file  = "C:\\Users\\guillaume\\pycharmproject")
canvas.create_image(0, 0, position = NW, image = mon_image)
canvas.create_arc(10,10,200,500, extent = 180, style = ARC)
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 300)
mon_polygone = canvas.create_polygon(10, 10, 100, 10, 100 , 110, fill = "red", outline = "black")
canvas.itemconfig(mon_polygone, fill = "blue") #itemconfig permet de changer des valeurs rappel boucle importer valeure c global


def rectangle_aleatoire(largeur, hauteur, coul_rempl):
    x1 = random.randrange(largeur)
    y1 = random.randrange(hauteur)
    x2 = x1 + random.randrange(largeur)
    y2 = y1 + random.randrange(hauteur)
    canvas.create_rectangle(x1, y1, x2, y2, fill  =  coul_rempl)
    #indique le couleur a remplir de rectangle avec turle begin_fill() end_fill()
for x in range(0, 50):
    c = askcolor()
    rectangle_aleatoire(400, 400, c[1])

#projet 6

canvas.create_polygon(10, 10, 100, 10, 60, 65)
for x in range(0, 60):  # pour compter de 0 a 59 secondes
    canvas.move(1, 5, 5)  # objet 1 de se deplacer de 5 pixels vers la droite et 5 en bas)
    tk.update()
    time.sleep(0.05)


def bouger_polygone(evenement):
    if evenement.keysym == "up":  # keysyme représente les symbole de touches
        canvas.move(1, 0, -3)  # 3 eme indice pour le vertical il faut qu'il soit negatif
    elif evenement.keysym == "down":
        canvas.move(1, 0, 3)
    elif evenement.keysym == "left":
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)


canvas.bind_all("KeyPress-Return", bouger_polygone)  # permet de caractériser la valeur de départ de la boucle

canvas.bind_all("KeyPress-Up", bouger_polygone)
canvas.bind_all("KeyPress-Down", bouger_polygone)
canvas.bind_all("KeyPress-Left", bouger_polygone)
canvas.bind_all("KeyPress-Right", bouger_polygone)




