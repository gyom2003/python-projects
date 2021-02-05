
from statistics import mean
from random import shuffle, randint, randrange, choice
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image
import string
from tkinter import *
import pygame
import sys
import os
import time
import time # gerer le temps
import sys
from pygame.locals import *
import tkinter
import numpy
import math
#exo
#password = input("entrer mdp")
#passsword_length = len(password)
#print(passsword_length)

#mdp inferieur 8 charactères.

if password_length <= 8:
    print("mdp trop court")
elif passsword_length > 8 and passsword_length < 12:
    print("mdp moyen")
else:
    print("mot de passe valide")

online_players = ["guillaume", "gustave", "maman","kevin"]
print(online_players[0])
#maman?
print(online_players[len(online_players) - 1])
#online_players.insert(2,"vincent")
#modifier gustave a gus
online_players[1] = "gus"
online_players[2:4] = ["paul", "jack"]
print(online_players[2:4])
online_players.append("gameur 123")
online_players.extend(["joueur1", "joueur2"])
online_players.insert(0,"bernad")
print(online_players)
online_players.clear()



notes = [8, 10, 16, 8, 20]
print(notes)
result = mean(notes)
print("la moyenne de l'élève est de {}".format(result))
print(notes)
shuffle(notes)
print(notes)

text = input("entrez une chaine sous la forme (émail-pseudos-motdepasse)").split("-")
print(text)
#on a donc une chaine
print("salut {}, ton émail {}, ton mot de passe".format(text[1], text[0], text[2]))

from random import shuffle
chained_word = input("entrez une chaine sous la forme (mot1/mot2/mot3/mot4)").split("/")
shuffle(chained_word)
word_len = len(chained_word)
if (word_len) < 10:
    print(chained_word[0:1])
else:
    print(chained_word[word_len-1], chained_word[word_len-2], chained_word[word_len-3])


#boucle for pour une valeur de départ et la valeur d'arrivé
for num_client in range (1, 6):
    print("vous etes le client numero {}".format(num_client))
#for each : pour chacune des valeurs d'une liste donnée.

emails = ["guillaume.leformal@lp.net", "gustave1.leformal@gmail?com", "contact.gui@yahoo.pt"]
#créer une black liste apres condition
blacklist = ["gui123@gmail.com, steelrose@laposte.net"]
for email in emails:
    print("email envoyé a :", email)

 if email in blacklist:
print("email {] interdi envoie impossible...".format(email))
continue

salary  = 1500
while salary < 2000:
    salary += 120
    print("votre salair actuel est de:",salary,"euros")

suscriber_count = 2500
mounth = 0
while mounth <= 24:
    suscriber_count *= 1.10
    mounth += 1
    print("vous avez actuellement {} abonnées".format(suscriber_count))


just_price = 100
while just_price in range (1, 1001):
number = int(input("entrez un nombre"))
text = ("c'est moin ","c'est plus")[number < just_price]

#2 manieres
if number == just_price:
    print("vous avez gagné")
    break
elif number < just_price:
    print("c'est moin")
elif number > just_price:
    print("c'est plus")
#foonctions
def welcome():
    print("bienvenue")
    result = (5 + 6)
    print("le resultat du calcul est de", result)

welcome()

def next_year():
    global years
    print("c'est la fin de l'année {} ".format(years))
    years += 1
    print("début de l'année",years)

years = 2018
next_year()
next_year()


def addition():
    result = 5 + 5
    return result

print("le résultat est", addition())
#plus rapidement
def multiply():
    return 5 * 8
print("le résultat est de ", multiply())
#ou avec les parametres
def multiply2(n):
    return 5 * n
print("le résultat est de ", multiply(5))

def max(a,b):
    if a < b:
        return b
    else:
        return a

valeur_une = int(input("entrez la valeur de a"))
valeur_deux = int(input("entrez la valeur de b"))
print("la valeur max est",(max(valeur_deux, valeur_deux)))


#fonction boucle (recusivité)
def add(a):
    a += 1
    print(a)
    if a < 10:
    add(a)

add(2)



def get_vowels_numbers(word):
    compteur = 0

word = input("entrez un mot")


for voyelles in word:
    if voyelles in ["a","e","i","o","u","y"]:
        compteur = 0
        compteur += 1
return compteur


compte_voyelle = get_vowels_numbers(words)
print("il y a ", compte_voyelle,"voyelles dans le mot", word )

valeur_une = int(input("entrez la valeur b"))
valeur_deux = int(input("entrez la valeur a"))

#max sans def max():
if valeur_une > valeur_deux:
    print("la valeur la plus grande est la valeur b")
else:
    print("la valeur la plus grande est la valeur a")
#la meme

while [x, y, z] in range(1, 11):

x = int(input("entrez la valeur x"))
y = int(input("entrez la valeur y"))
z = int(input("entrez la valeur z"))
if x > y and x > z:
    print("le nombre le plus grand est x")
elif y > x and y > z:
    print("le nombre le plus grand est y")
else:
    print("le noombre le plus grand est z")

# avec def max():
while [x, y, z,] in range (1, 11):
x = int(input("entrez la valeur x"))
y = int(input("entrez la valeur y"))
z = int(input("entrez la valeur z"))

def max(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
print("le nombre le plus grand est", max)

#avec module random tu as shuffle randit (creé nombre au hazard) ou choice (au hazard dans une liste établit avant
from random import choice
dessert = ["glace", "crepe", "gateau"]
print(choice(dessert))

#time exemple avec fonctions (parametres)
import time
def plein_de_nombre(maximum):
    t1 = time.time()
    for x in range(0, maximum):
        print(x)
        t2 = time.time()
        print("il a fallut {} secondes".format(t2 - t1))


plein_de_nombre(1000)

#exos

for y in range(1, 11):
    for z in range(1,11):
        if y + z <= 10 and 2 * y + 5 * z == 30:
            print(10-y-z,y,z)
            break

a = int(input("entrez votre age!"))
if a <= 8:
    p = 5
    print("le prix est de [/]".format(p))
elif a <= 16:
    p = 10
    print("le prix de votre place est de []".format(p))
else:
    p = 20
print(p)

#les objets methode ..
class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage


class player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("bienvenue au joueur",pseudo, "/ point de vie:", health, "/ attaque",attack)
#methode getter
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def get_damage(self,damage):
        self.health -= damage
        print("vous venez de subir",damage,"degats")

    def attack_player(self, target_player,player2):
        target_player.damage(self.attack)
        #permet de montrer ses dommages qu'il inflige
        if self.weapon():
            damage += self.weapon.get_damage_amount()

    def set_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        return self.weapon is not None

class Warrior(player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3

    def get_damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
            super().get_damage(damage)


    def blade(self):
        self.armor = 3

    def get_armor_point(self):
        return self.armor

player = player("guillaume", 20, 3)
player.get_damage(3)
warrior = Warrior("darkwarrior", 30, 4)
warrior.get_damage(5)
print("vie:", warrior.get_health(),"armure",warrior.get_armor_point())

if issubclass(Warrior, player):
    print("warrior spécialisation de player")



#print("le pseudo est",player1.get_pseudo())
player = player("guillaume", 20, 3)
knife = Weapon("Couteau", 3)
#permet de l'équiper de l'arme
player1.set_weapon(knife)

print("maintenant vous avez",player1.get_health(),"point de vie")
player2 = player("bob", 20, 5)
player1.attack_player(player2)

print(player1.get_pseudo(),"attaque",player2.get_pseudo())
print("bienvenue au joueur", player1.get_pseudo(), "/ point de vie:", player1.get_health(), "/ attaque", player1.get_attack_value())

print("bienvenue au joueur", player2.get_pseudo(), "/ point de vie:", player2.get_health(), "/ attaque", player2.get_attack_value())

#tp objets superclasse
class batiment:
    def __init__(self, adresse, nombre_etage):
        self.adresse = adresse
        self.nombre_etage = nombre_etage
        print("le batiment est a", adresse, "et a ", nombre_etage, "étages")

    def avoir_adresse(self):
        return self.adresse

    def avoir_nombre_etage(self):
        return self.nombre_etage

btiment = batiment("12 avenues paris", 5)


class supermarche (batiment):
    def __init__(self, nombre_etage, rayons, adresse):
        super().__init__(adresse, nombre_etage)
        self.rayon = rayons
        print("le supermarché a",nombre_etage, "étages pour un nombre de rayons de ", rayons, "son adresse", adresse)

    def avoir_rayons(self):
        return self.rayon
supmarche = supermarche(3, 6, "22 avenue verdun")
supmarche2 = supermarche(5, 6, "23 avenue mechou")

class banques(batiment):
    def __init__(self, adresse, nombre_etage, enseigne, nombre_coffre):
        super().__init__(adresse, nombre_etage)
        self.enseigne = enseigne
        self.nombre_coffre = nombre_coffre
        print("la banque se situe a", adresse, "et a ", nombre_etage,"étages", "et se nomme",banques.avoir_enseigne(enseigne),"et a ", banques.avoir_nombre_coffre(nombre_coffre))

    def avoir_enseigne(self):
        return self.enseigne

    def avoir_nombre_coffre(self):
        return self.nombre_coffre

 bque = banques("26 av dujardin", 12, "guibanque", 9)

class Immeuble(batiment):

    def __init__(self, adresse, nombre_etage, nombre_balcon):
        super().__init__(adresse, nombre_etage)
        self.nombre_balcon = nombre_balcon

    def avoir_nomre_balcon(self):
        return self.nombre_balcon

immeuble1 = Immeuble("26 rue de la Gravengui", 3, 3)
immeuble2 = Immeuble("28 rue de la gui12", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble5 = Immeuble("120 rue pleiades", 8, 4)

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("logo.ico")
        self.window.config(background='#41B77F')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_youtube_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Hey salut à tous c'est Graven", font=("Courrier", 25), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Ouvrir Youtube", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.open_graven_channel)
        yt_button.pack(pady=25, fill=X)

    def open_graven_channel(self):
        webbrowser.open_new("http://youtube.com/gravenilvectuto")


# afficher
app = MyApp()
app.window.mainloop()

#entrainement jeu
#le pendue
from random import randint, shuffle
mot = input("Entrez votre mot")

liste=[]
votre_liste=[]

for x in mot:
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))

nb_erreur = 0
while nb_erreur < 9 :
    lettre = input("Entrez votre lettre")

    if len(lettre)>1:
        if lettre ==mot:
            print("vous avez trouvé")
            break

    if lettre in liste:
        for (index,x) in enumerate(liste):
            if x==lettre:
                votre_liste[index] = x
        v = ''.join(votre_liste)
        print("bonne lettre ",v)

        if liste==votre_liste:
            print("vous avvez trouvé")
            break
    else:
        nb_erreur +=1
        print('Mauvaise lettre, il vous reste %s essais'%(9-nb_erreur))

if nb_erreur ==9:
    print('vous avez perdu')


 #tp
keys = 0
snake_jar = randint(1, 5)
print("bienvenue dans le jeu!")
choix_level = int(input("Ecrit 1:facile, 2:moyen, 3:difficile"))

while keys != 3:
    jarre = ["K", "K", "K", "K", "K"] #rajouter serpent
    for i in range(0, choix_level):
        print("un serpent a été rajouté dans une jarre")
        jarre[i] = "S"
    print(jarre)
    shuffle(jarre)

    choix = int(input("Choisit une jarre : 1, 2, 3, 4, 5"))
    if jarre[choix-1] == "K":
        keys += 1
        print("Gagné ! vous avez obtenu une clé (", keys, "/3) !")
    else:
        keys -= 1
        print("Perdu ! vous tombez dans le piège (", keys, "/3) !")
    if keys > 0:
        keys -= 1
        print(f"tu as actuellement {keys}/3")

print("Tu deviens roi du temple")
#entrainement tkinter
import string

def add_score():
    global score
    global reponse
    score += 1
    label_score.config(text=score)
    hello = "hello" + entree_proposition.get()
    mylabel = Label(canvas, text=hello)
    mylabel.pack()

def delete_all():
    mybox.delete(0, END)

#les variables
color = "#08DD6B"
score = 0
width = True
height = True
width1 = 50
height1 = 50

#création de la fenetre
fenetre = Tk()
fenetre.geometry("600x300")
fenetre.title("entrainement tkinter")
fenetre.config(bg=color)
fenetre.minsize(width=False, height=False)
fenetre.iconbitmap(r"C:/Users/pcproject/image/programacion-web.ico")#png, jpg en ico

#création de la boite
frame = Frame(fenetre)

#creation menu
menu = Menu(fenetre)
fill_menu = Menu(menu, tearoff=0)
fill_menu.add_command(label="nouveau", command=delete_all)
fill_menu.add_command(label="quitter", command=fenetre.quit)

#2 label dans une cascade
menu.add_cascade(label="fichier", menu=fill_menu)
fenetre.config(menu=menu)

#creation du canvas et de l'image
canvas = Canvas(frame, width=300, height=300,  bg="#dee5dc", bd=0, highlightthickness=0)
image = PhotoImage(file=r"C:/Users/pcproject/image/piton.png").zoom(2)
canvas.create_image(width1, height1, image=image)#pas command

#creation d'une entrée
entree_proposition = Entry(frame, font=("Helvetica", 10), fg="black", borderwidth=2)
#entree_proposition.insert(0, "entrez votre prenon")
reponse = entree_proposition.get()
#entree_proposition.insert(0, "entre ton nom : ")
entree_proposition.pack()

#creation de label
label = Label(fenetre, text="je sais pas quoi dire", font=("Courrier", 20), bg=color)
label_score = Label(canvas, text=0, font=("Courrier", 10), bg="white")

#creation boutton image pour boutton
boutonscore = Button(frame, image=image, bg="#336BFF", bd=0, relief=SUNKEN, command=add_score)


#creation d'une boxe

def delete(): #pour les listes
    mybox.delete(ANCHOR)

#creation scrollbar
myscorllbarre = Scrollbar(frame, orient=VERTICAL)
mybox = Listbox(frame, yscrollcommand=myscorllbarre)
myscorllbarre.config(command=mybox.yview)  #pour etre vu en verticale
scale_1 = Scale(frame, from_=10, to=100)
#def select item
def select():
    labelbox.config(text=mybox.get(ANCHOR))
liste = ["Un", "Deux", "Trois", "Quatre", "Cinque", "six", "Septe", "Huigt", "Neuf", "Dix", "Onze", "Douze", "Treize", "Quatorze", "15"]
mybox.insert(END, "c'est un autre item")

for item in liste:
    mybox.insert(END, item)

my_boutton = Button(canvas, text="Supprimer", command=delete)
my_boutton2 = Button(canvas, text="Select", command=select)
labelbox = Label(canvas, text=" ")

canvas.pack()
fenetre.update()
label.pack(side=BOTTOM)
label_score.pack()
frame.pack(expand=YES)#pour rajouter la boite au milieu de la fenetre
boutonscore.pack(fill=X)
mybox.pack(padx=2, pady=2)
my_boutton.pack(pady=5, padx=5)
my_boutton2.pack(padx=5, pady=5)
labelbox.pack(pady=5)
myscorllbarre.pack(side=RIGHT, fill=Y) #apparition gauche axe horizontale

fenetre.update()
fenetre.mainloop()


#générateur password
def geenerate_password():
    password_min=6
    password_max=12
    all_characters=string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_characters) for x in range(randint(password_min, password_max)))
    entrer.delete(0, END) #turtle pogo(O,O)
    entrer.insert(0, password)


if __name__ == "__main__":
    window2 = Tk()
    window2.title("password generator")
    window2.geometry("720x480")
    window2.minsize(200, 200)
    window2.config(bakground="#4065A4")
    #creer la frame principal
    frame = Frame(window2,bg="#4065A4")
    #importer l'image
    width = 300
    height = 300
    canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
    image = PhotoImage(file="lock.png").zoom(35)
    canvas.create_image(width/2, height/2, image=image)
    canvas.grid(row=0, column=0, sticky=W)
    #creer une sous boite
    frame_right = Frame(frame, bg="#4065A4")
    #creer un titre
    titre_label = Label(frame_right, text="mot de passe" ,font=("Helvetica", 18), bg="#4065A4", fg="white")
    titre_label.pack()

    entrer = Entry(frame_right,font=("Helvetica", 18 ),bg="#4065A4", fg="white")
    entrer.pack()

    generate_button = Button(frame_right, text="generer", font=("Helvetica", 18), bg="#4065A4", fg="white", command=geenerate_password)
    generate_button.pack(fill=X)

    frame_right.grid(row=0, column=1, sticky=W) #sous boite a droite frame principal
    #afficher la frame
    frame.pack(expand=YES)
    #creer un menu
    menu_bar = Menu(window2)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="nouveau", command=geenerate_password)
    file_menu.add_command(label="quitter", command=window2.quit)
    #Pour ajouter la barre
    menu_bar.add_cascade(label="fichier", menu=file_menu)
    #pour l'afficher
    window2.config(menu=menu_bar)
    window2.mainloop()

#tp biscuit

cookie_count = 0


def add_cookie():
    global cookie_count
    cookie_count += 1
    label_counter.config(text=cookie_count)


# creer la fenetre
window = Tk()
window.title("Cookie Clicker")
window.geometry("720x480")
window.config(background='#dee5dc')

# ajout du compteur
label_counter = Label(window, text="0", font=("Courrier", 30), bg="#dee5dc")
label_counter.pack()

# creer la frame principale
frame = Frame(window, bg='#dee5dc')

# creation d'image
width = 300
height = 300
canvas = Canvas(frame, width=width, height=height,  bg="#dee5dc", bd=0, highlightthickness=0)
canvas.pack()
image = PhotoImage(file="biscuit.png").zoom(32)
canvas.create_image(width/2, height/2, image=image)

# ajout du bouton/image
button = Button(frame, image=image, bg='#dee5dc', bd=0, relief=SUNKEN, command=add_cookie)
button.pack(fill=X)

# ajout de la frame au centre
frame.pack(expand=YES)
#creer un menu qui fonctionne avec bbton
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="nouveau", command=add_cookie)
file_menu.add_command(label="quitter", command=window.quit)
#Pour ajouter la barre
menu_bar.add_cascade(label="fichier", menu=file_menu)
#pour l'afficher
window.config(menu=menu_bar)

# affichage
window.mainloop()

fenetre = Tk()
fenetre.title("Seance de Cinema - Logiciel de gestion")
fenetre.geometry("400x300")
# fonction qui va s'activer lors du clique sur le bouton reserver
def click_btn(film_id, txt):
    print("click ok sur le film n", film_id)
    # choix = int(input("Inscrivez le numero du film à voir (1, 2 ou 3)"))
    print("Vous avez choisi le film:", films[film_id-1]['titre'])

    nb_places = films[film_id-1]['places']

    # verifier si le film n'est pas complet
    if nb_places > 0:
        print("Achat effectue !")
        # retirer 1 place au nombre de places disponible
        films[film_id-1]['places'] -= 1
        txt.set(films[film_id-1]['places'])
        print("Le film possede desormais", films[film_id-1]['places'], "places !")
    else:
        print("Film complet !")
        txt.set("Film Complet !")


# afficher un message de bienvenue
print("Bienvenue au cinema, voici les films à l'affiche: ")

# cette liste de films
# films = ["Voyage au centre du HTML", "Les 9 jsons cachés", "Algobox - le film"]

# version avec le dictionnaire
films = [
    { # film 1
        "titre": "Voyage au centre du HTML",
        "seance": "18h05",
        "places": 200
    },
    { # film 2
        "titre": "Les 9 jsons cachés",
        "seance": "10h10",
        "places": 80
    },
    { # film 3
        "titre": "Algobox - le film",
        "seance": "22h15",
        "places": 1
    }
]

# afficher chaque film
for numero, film in enumerate(films, start=1):
    titre = film['titre']
    seance = film['seance']
    places = film['places']
    places_var = StringVar()
    places_var.set(places)

    titre_label = Label(fenetre, text=titre)
    titre_label.grid(row=numero, column=0)

    seance_label = Label(fenetre, text=seance)
    seance_label.grid(row=numero, column=1)

    places_label = Label(fenetre, textvariable=places_var)
    places_label.grid(row=numero, column=2)

    book_bouton = Button(fenetre, text="Reserver",
        command= lambda num = numero,
        txt = places_var: click_btn(num, txt))
    book_bouton.grid(row=numero, column=3)

fenetre.mainloop()

#niveau 2 graven tp fruitq
pygame.init()
# liste stockant le nom de chaque fruit
fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]
proba_fruits = [0.2, 0.25, 0.4, 0.1, 0.05] #probabilité d'apparition

fruits_dict = {    #les points qui rapportent
    "orange": 5,
    "cerise": 15,
    "ananas": 50,
    "pasteque": 150,
    "pomme_dore": 10000
}

# choix au hasard selon les probabilités
hasard = numpy.random.choice(fruits, 3, p=proba_fruits)

# afficher le tirage
print(hasard)

# faire la verification des lots
if hasard[0] == hasard[1] == hasard[2]: # les 3 premiers fruits sont identique
    fruit = hasard[0]
    jetons = fruits_dict[fruit]
    print(f"Une ligne de {fruit} a été completé ! + {jetons} Jetons")


# creer une classe qui va gérer la notion d'emplacement
class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('image/pomme_dore.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self, image):
        self.image = image

# definir une fonction lancement
def lancement():

    global jetons

    # choix au hasard selon les probabilités
    hasard = numpy.random.choice(fruits, 3, p=proba_fruits)
    fruit_gauche = fruits_dict[hasard[0]]
    fruit_milieu = fruits_dict[hasard[1]]
    fruit_droite = fruits_dict[hasard[2]]

    # changement des images
    emplacement_gauche.set_image(fruit_gauche)
    emplacement_milieu.set_image(fruit_milieu)
    emplacement_droite.set_image(fruit_droite)

    # faire la verification des lots
    if hasard[0] == hasard[1] == hasard[2]: # les 3 premiers fruits sont identique
        fruit = hasard[0]
        jetons_gagnes = fruits_dict_gains[fruit]
        jetons += jetons_gagnes
        print(f"Une ligne de {fruit} a été completé ! + {jetons_gagnes} Jetons")

# creation de la fenetre
largeur = 800
hauteur = 460
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Machine à sous ")
blanc = [255, 255, 255] # couleur blanche

# argent du joueur
jetons = 1000

# dictionnaire de fruits
image_test = pygame.image.load('image/orange.png')
fruits_dict = {
    "cerise": pygame.image.load('image/cerise.png'),
    "ananas": pygame.image.load('image/ananas.png'),
    "orange": pygame.image.load('image/orange.png'),
    "pasteque": pygame.image.load('image/pasteque.png'),
    "pomme_dore": pygame.image.load('image/pomme_dore.png')
}

# liste stockant le nom de chaque fruit
fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]
proba_fruits = [0.2, 0.25, 0.4, 0.1, 0.05]

fruits_dict_gains = {  #rapport pt fruitq
    "orange": 5,
    "cerise": 15,
    "ananas": 50,
    "pasteque": 150,
    "pomme_dore": 10000
}

# chargement des emplacements
hauteur_emplacement = hauteur / 2 + 30
emplacement_x_milieu = largeur / 3 + 62
emplacement_x_gauche = emplacement_x_milieu - image_test.get_width() - 22
emplacement_x_droite = emplacement_x_milieu + image_test.get_width() + 20

emplacements = pygame.sprite.Group()
emplacement_gauche = Emplacement(emplacement_x_gauche, hauteur_emplacement)
emplacement_milieu = Emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = Emplacement(emplacement_x_droite, hauteur_emplacement)

# rangement des emplacements dans le groupe
emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)

# charger l'image de l'arriere plan
fond = pygame.image.load('image/slot.png')
police = pygame.font.SysFont("comicsansms", 30)

# boucle pour maintenir la fenetre pygame en eveil
running = True

while running:

    ecran.fill(blanc)
    ecran.blit(fond, (0, 0))
    emplacements.draw(ecran)

    # afficher son nombre de jetons
    text = police.render(str(jetons) + " jetons", True, (0, 0, 0))
    ecran.blit(text, (10, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        # verifier si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            quit()
        # verifier si le joueur appuie sur une touche
        if event.type == pygame.KEYDOWN:
            # si la touche est la touche ESPACE
            if event.key == pygame.K_SPACE and jetons >= 10:
                lancement() # appeler la fonction
                jetons -= 10




#entrainement touche collision pygame
pygame.init()
pygame.display.set_caption("voiture")
ecran = pygame.display.set_mode((500, 500))
black = (0, 0, 0)
couleur  = (0, 255, 0)
rouge = (255, 255, 255)
tiles = [pygame.Rect(200, 350, 50, 50),pygame.Rect(280, 350, 50, 50)]
player = pygame.Rect(100, 100, 40, 80)
clock = pygame.time.Clock()
collisions = []

def collision_test(rect, tiles):
    for tile in tiles:
        global collisions
        if pygame.Rect.colliderect(tiles, player):
            collisions.append(tile)
    return tiles


def move(rect, movement, tiles):
    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right
    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect

right = False
left = False
up = False
down = False

run = True
while run:
    ecran.fill((0, 0, 0))
    pygame.draw.rect(ecran, rouge, player)
    movement = [0, 0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5
    if up == True:
        movement[1] -= 5
    if down == True:
        movement[1] += 5
    player = move(player, movement, tiles)

    for tile in tiles:
        pygame.draw.rect(ecran, couleur, tile)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.KEYDOWN]:
        if keys[pygame.K_RIGHT]:
            right = True
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_DOWN]:
            down = True
        if keys[pygame.K_UP]:
            up = True
    if keys[pygame.KEYUP]:
        if keys[pygame.K_RIGHT]:
            right = False
        if keys[pygame.K_LEFT]:
            left = False
        if keys[pygame.K_DOWN]:
            down = False
        if keys[pygame.K_UP]:
            up = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()




import time
import sys
pygame.init()
pygame.display.set_caption("voiture")
ecran = pygame.display.set_mode((500, 500))
black = (0, 0, 0)
player = (200, 200, 40, 50)

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    pygame.display.update()
    clock.tick(50)

pygame.quit()
sys.exit()


import random, string


# créer une fonction qui va se charger de générer cette chaine (code secret)
def generer_code_debloquage():
    # Format du code de déblocage : AAAA-2222-XX
    lettres = string.ascii_uppercase

    mot = ''.join(random.choice(lettres) for i in range(4))
    numeros = random.randint(1000, 9999)
    chars = ''.join(random.choice(lettres) for i in range(2))

    # choisir une lettre
    code = mot + "-" + str(numeros) + '-' + chars
    print("Votre code débloquage est: ", code)
    return code


# créer une fonction afficher_parking pour afficher le status de chaque emplacement
def afficher_parking():
    # boucle parcourir chaque emplacement pour afficher la disponibilité
    for num_etage, etage in enumerate(parking, start=1):
        for num_place, place in enumerate(etage, start=1):
            # nom_variable = (condition_faux, condition_vrai)[condition à verifier]
            resultat = ("Non Disponible", "Disponible")[place == 'D']
            resultat = (resultat, "Réservée")[place == 'H']

            print("Etage n° -", num_etage, " place n°", num_place, resultat)


# afficher un message de bienvenue
print("Bienvenue au niveau -1, que souhaitez-vous faire ?")

# creation de la liste
emplacements = 27
etages = 3
parking = [['D'] * emplacements] * etages

# créer une liste qui contient un dico par etage avec les codes à débloquer
code_debloquage = [
    {},
    {},
    {}
]

afficher_parking()

# je creer une boucle qui ne va jamais s'arreter
while True:

    # appeler la fonction pour afficher le parking
    # afficher_parking()

    print("Choisissez un numero d'étage")

    # proposer à notre client de choisir un étage
    choix_etage = int(input()) - 1

    if choix_etage >= 0 and choix_etage < len(parking):
        print("Vous avez choisi l'etage n°", choix_etage + 1)

        # proposer à notre client de faire une action
        print("1: Garer une voiture, 2: Récuperer une voiture")
        choix = int(input())

        # verifier le choix
        if choix == 1:
            print("Vous avez choisi de garer une voiture, à quel emplacement souhaitez vous la mettre ?")
            choix_emplacement = int(input()) - 1

            # verifier si la place est disponible
            if len(parking[choix_etage]) > choix_emplacement >= 0:
                if parking[choix_etage][choix_emplacement] == 'D':  # si c'est dispo
                    print("Vous avez prit la place n°", choix_emplacement + 1)
                    parking[choix_etage][choix_emplacement] = 'V'
                    # génerer le code secret
                    code_secret = generer_code_debloquage()
                    code_debloquage[choix_etage][choix_emplacement] = code_secret

                else:
                    print("Emplacement non disponible")

        elif choix == 2:
            print("Récuperer une voiture, mettre le numero de place: ")

            choix_emplacement = int(input()) - 1

            # verifier si la place existe
            if len(parking[choix_etage]) > choix_emplacement >= 0:
                if parking[choix_etage][choix_emplacement] == 'V':

                    print("Entrer le code secret")

                    # demander le code secret de la voiture
                    choix_code_secret = input()

                    # verifier si le code secret est bon
                    code_secret_atrouver = code_debloquage[choix_etage][choix_emplacement]

                    # comparer
                    if choix_code_secret == code_secret_atrouver:
                        print("Vehicule récupéré")
                        parking[choix_etage][choix_emplacement] = 'D'
                        print("L'emplacement n°", choix_emplacement + 1, "est désormais disponible")
                    else:
                        print("Code incorrecte ! stop !")

        else:
            print("Erreur, vous devez ecrire 1 ou 2")

        # afficher le parking
        # afficher_parking()

    else:
        print("Etage non existant !")



#tp machine à laver

import time # gerer le temps

# créer une classe qui va gerer la notion de lave linge
class LaveLinge:

    # creer le constructeur
    def __init__(self, tours_minutes=1400, contenance_kg=8):
        self.tours_minutes = tours_minutes
        self.contenance_kg = contenance_kg
        self.contenance_actuel_kg = 0
        self.temperature_actuel = 60
        self.duree_machine_defaut = 35
        self.duree_machine = 35
        print("Nouvelle machine ajoutée à la laverie")
        print("tours min: ", self.tours_minutes, "contenance:", contenance_kg)


    # methodes
    def inserer_linge(self, poids_kg):
        print("Vous ouvrez la machine et vous entrez un total de", poids_kg, "kg")

        # verification
        if poids_kg <= self.contenance_kg:
            print("Ok ! le linge est à l'interieur")
            self.contenance_actuel_kg = poids_kg
        else:
            print("Ah non ! la machine est trop petite")

    def demarrage(self):

        # verifier si la machine est vide
        if self.contenance_actuel_kg != 0:
            # creer une variable pour stocker le temps par défaut de la machine
            compteur_tours = 0

            # une boucle tant que la machine n'est pas à 0
            while self.duree_machine > 0:
                print(str(self.duree_machine) + "s")
                self.duree_machine -= 1
                compteur_tours += 1400
                time.sleep(1) # attendre 1s

            # afficher nombre de tours minutes
            print("Fin", compteur_tours, "tours minutes")
        else:
            print("Vous n'avez pas inserer de linge !")

    def stop(self):
        if self.duree_machine > 0:
            print("Arret ok !")
            self.duree_machine = 0
        else:
            print("Arret impossible, lave linge en cours d'utilisation")



# afficher un message dans la console
print("Ouverture de la machine à laver")

# appeler la fonction pour demarrer la machine à laver
machine = LaveLinge(150, 40)

# dictionnaire avec nos vetements et leurs poids
vetements = {
    "chemise rouge bleuté": 1,
    "manteau de gravounai": 6,
    "chaussettes": 4,
    "jean de yannis": 18
}

total_kg = 0.0

for poid in vetements.values():
    total_kg += poid

print("Vous avez", total_kg, "kg de vetements")

# calculer combien de machines
machines = math.ceil(total_kg / 8)
print(machines, "machines")

# calculer la consommation d'eau
consommation_eau = machines * 60
print("La consommation d'eau pour {} machines est de {}L".format(machines, consommation_eau))

# appeler la methode inserer linge
machine.inserer_linge(total_kg)

# appeler la methode demarrer la machine
machine.demarrage()
machine.stop()



def nombreOcurrent(L, a):
    i = 0
    for x in L:
        if (x == a):
            i += 1
    return i
L = [1, 5, 3, 2, 6, 4, 9, 12, 2, 19]
print(L.count(5))
print(f"le nombre d'occurence de 2 par exemple est de :{nombreOcurrent(L, 2)}")


#tkinter tp
#les variables
color = "#08DD6B"
choix = 0 #lui établir une valeur 0 pour la boucle while et apres lui mettre la valeut input() pour la reconvertir en int
tentative = 5
temps = time.time()#ou time.clock()
width = False
height = False
print("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100")
nombre_hazard = random.randint(0, 101)

while choix != nombre_hazard and tentative > 0:
    print("choissisez votre nombre")
    choix = input()
    if choix.isdigit():
        choix_nombre = int(choix)
        temps_passe = time.time() - temps
        print(f"tu as pris {temps_passe}, secondes")
        #verification tu temps
        if temps_passe >= 40:
            print("tu avais 40 secondes, temps écoulé")
            break #ou dans while mettre and temps_passe < 40:
        if choix_nombre > nombre_hazard:
            tentative -= 1
            print("C'est moin")
            print(f"fais attention, il te reste encore {tentative} tentatives sur 5")
        elif choix_nombre < nombre_hazard:
            tentative -= 1
            print("C'est plus")
            print(f"fais attention, il te reste encore {tentative} tentatives sur 5")
        elif choix_nombre == nombre_hazard:
            print("tu as gagné")
            print(tentative)
            break
        if tentative == 0:
            print(f"tu as perdu tu as utilise tes 5 tentatives, le nombre qui était à trouver était : {nombre_hazard}")
    else:
        print(f"tu dois rentrer un nombre, pas {choix}")

#avec tkinter
# on importe le module tkinter
import tkinter as tk


# afficher de message de bienvenue

def essai(event=None):
    global entree_proposition, nombre_hasard, tentatives, tentativestxtvar, infovar

    # recolter la proposition
    proposition = entree_proposition.get()

    # verification
    if proposition.isdigit():
        # transformation de proposition en entier
        # cast
        nombre_proposition = int(proposition)

        # verifier si le nombre proposition est plus petit que le nombre à trouver
        if nombre_proposition < nombre_hasard:
            infovar.set("C'est plus")
        elif nombre_proposition > nombre_hasard:
            infovar.set("C'est moins")
        else:
            infovar.set("C'est gagné")
            time.sleep(2)
            fenetre.quit()

        tentatives -= 1  # enlever 1 tentative
        tentativestxtvar.set(f"{tentatives} tentatives")

    else:
        infovar.set(f"Tu dois entrer un nombre, pas {proposition}")


# compteur tentatives
tentatives = 25

# recupere le temps actuel
temps = time.time()

color = "#08DD6B"

# choisir un nombre entre 1 et 100
nombre_hasard = random.randint(1, 100)

# on créeeeeeez la fenetre tkinter
fenetre = tk.Tk()
fenetre.geometry("600x300")
fenetre.title("Jeu du juste prix")
fenetre.resizable(width=False, height=False)
fenetre.config(bg=color)

# boite
frame = tk.Frame(fenetre)
frame.pack(expand=True)

# ajouter une entrée pour ecrire
entree_proposition = tk.Entry(frame)
entree_proposition.bind('<Return>', essai)
entree_proposition.focus()
entree_proposition.pack()

# ajouter le bouton
bouton = tk.Button(frame, text="Valider", command=essai)
bouton.pack()
#creer barre scale vs Scrollbar
scale = tk.Scale(frame, from_=10, to=100)
scale.pack(side=tk.RIGHT)
#essai avec scrollbar
my_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
my_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# ajouter un intitulé pour afficher des informations
infovar = tk.StringVar()
infovar.set("Bonne chance...")
info = tk.Label(fenetre, textvariable=infovar, bg=color)
info.place(x=250, y=220)

# ajouter une variable stockant le nombre de tentatives
tentativestxtvar = tk.StringVar()
tentativestxtvar.set("5 tentatives")

# ajouter nombre de tentatives
tentativestxt = tk.Label(fenetre, textvariable=tentativestxtvar, bg=color)
tentativestxt.place(x=500, y=20)

# ajouter temps restant
tempsvar = tk.StringVar()
tempsvar.set("60s")
tentativestxt = tk.Label(fenetre, textvariable=tempsvar, bg=color)
tentativestxt.place(x=20, y=20)

# afficher
fenetre.mainloop()

run = True
while run:
    temps_passe = time.time() - temps
    tempsvar.set(str(temps_passe) + "s")
    time.sleep(1)
    fenetre.update()

#bot facebook
from  selenium import webdriver
from pynput.mouse import Button, Controller as ct
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Listener, Controller
from selenium.webdriver.common.action_chains import ActionChains

path = "C:/Users/pcproject/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
cookie = driver.find_element_by_id("bigCookie")#cookie
cookie_count = driver.find_element_by_id("cookies")#barre compte click
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]#list for boucle sur le cliker souris
action = ActionChains(driver) #permet d'affectuer action (au lieu de mouse.Controller(), mouse.click, variable.click
action.click(cookie)
for i in range(5000):
    action.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items: #permet de généraliser les conditions (ex mouvement)
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver) #on peut repeter cette action comme driver = webdriver.Chrome(newpath)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()

import time
username = input("entre ton pseudo : ")
mdp = input("entre ton mot de passe : ")
driver = webdriver.Chrome("C:\\Users\\pcproject\\chromedriver.exe")
driver.get("https://fr-fr.facebook.com/")
username_text = driver.find_element_by_id("email")
#prendre en compte les touches
username_text.send_keys(username)
mdp_text = driver.find_element_by_id("pass")
mdp_text.send_keys(mdp)

login_button = driver.find_element_by_id("u_0_e")
login_button.click()
mouse = Controller()
#posisiton de la souris
mouse.position = (990, 245)
mouse.click(Button.left, 2)

#exemple tim
path = "C:/Users/pcproject/chromedriver.exe"
driver = webdriver.Chrome(path)

try:
    driver.get("https://www.google.fr/")
    print(driver.title) #app cache copie tt
    google_barre = driver.find_element_by_name("q")
    google_barre.send_keys("test")
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gsr"))
        )
finally:
    time.sleep(3)
    driver.quit() #ou close()

#avec wiki
path = "C://Users//pcproject//chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.wikipedia.org/")
wiki_barre = driver.find_element_by_id("searchInput")
wiki_barre.send_keys("voiture")
bouton_login = driver.find_element_by_class_name("sprite svg-search-icon")
bouton_login.click()
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.CLASS_NAME("mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Voiture rootpage-Voiture skin-vector action-view"))
    articles = main.find_element_by_class_name("mw_body")
    for article in articles:
        head_title = article.find_element_by_id("firstHeading")
        print(head_title.text)
except Exception as e:
    print("ERROR", e)
finally:
    time.sleep(5)
    driver.quit()

#keylogger
def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#insta bot
def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("C://Users//pcproject//chromedriver.exe")

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_class_name("_8-yft5").click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

if __name__ == "__main__":

    username = "gyom_._"
    password = "rawwwe2003"

    ig = InstagramBot(username, password)


    hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()



fenetre = Tk()
fenetre.geometry("300x300")
fenetre.title("tout les widgets possibles")
fenetre.geometry("600x600")
fenetre.resizable(width=False, height=False)
class main:
    def __init__(self, master):
        self.myframe = Frame(master)#master = root
        self.myframe.pack(expand=YES)
        #bouton génère un message
        self.bouttontxt = StringVar()
        self.boutton = Button(master, textvariable=self.bouttontxt, command=self.cliker)
        self.boutton.place(x=30, y=30)
        #creation d'un meno
        self.menu = Menu(master)
        self.menu_fill = Menu(self.menu, tearoff=0)
        self.menu_fill.add_command(label="reboot", command=self.reboot) #pour menu label
        self.menu_fill.add_command(label="Quitter", command=self.quitter)
        self.menu_fill.add_command(label="Nouveau", command=self.nouvelle_fenetre)
        self.menu.add_cascade(label="Le Menu", menu=self.menu_fill)
        fenetre.config(menu=self.menu)
        #creation entrée
        self.reponse = StringVar()
        self.joueur_entree = Entry(self.myframe, font=("Helvetica", 10), fg="black",  borderwidth=2)
        self.getr = self.joueur_entree.get()
        self.boutonreponse = Button(self.myframe, textvariable=self.reponse, command=self.getreponse).pack()
        self.boutonreponse_txt = StringVar()
        self.joueur_entree.pack()
        #creation listbox
        # creation scroll bar
        self.scrollbar = Scrollbar(self.myframe, orient=VERTICAL).pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.myframe, yscrollcommand=self.scrollbar)
        self.my_list = ["Un", "Deux", "Trois", "Quatre", "Cinque", "six", "Septe", "Huigt", "Neuf", "Dix", "Onze",
                        "Douze"]
        for item in self.my_list:
            self.listbox.insert(END, item)
        self.listbox.pack(pady=10)
        #création barres scale
        self.horizontal = Scale(self.myframe, from_=0, to=10, orient=HORIZONTAL).pack()
        #spinebox
        self.boutton_horizontal = Button(self.myframe, text="clique sur moi", command=self.slide)
        self.s = Spinbox(self.myframe, from_=0, to=20).pack(pady=20)
        self.l = LabelFrame(fenetre, text="titre frame", padx=20, pady=25)
        self.l.pack(fill="both", expand=YES)
        self.labelframe = Label(self.l, text="a l'interieur de la frame").pack()



    def nouvelle_fenetre(self):
        self.top = Toplevel()
        self.top.title("second fenetre")
        self.top.geometry("200x200")
        self.image = ImageTk.PhotoImage(Image.open("C:/Users/pcproject/image/ananas.png"))
        self.image2 = ImageTk.PhotoImage(Image.open("C:/Users/pcproject/image/cerise.png"))
        self.image3 = ImageTk.PhotoImage(Image.open("C:/Users/pcproject/image/enemy.png"))
        self.image4 = ImageTk.PhotoImage(Image.open("C:/Users/pcproject/image/orange.png"))
        self.image5 = ImageTk.PhotoImage(Image.open("C:/Users/pcproject/image/rocket.png"))
        self.imagelist = [self.image, self.image2, self.image3, self.image4, self.image5]
        self.labelimage = Label(self.top, image=random.choice(self.imagelist)).pack()
        #self.suivant = 2
    def quitter(self):
        if messagebox.askyesno("est tu sur de faire ca ?"):
            messagebox.showwarning("tans pis...")
            fenetre.quit()
        else:
            messagebox.showinfo("tu as peur")
            messagebox.showerror("ahahaha")
    def cliker(self):
        self.bouttontxt.set("tu as cliqué sur le bouton")#get pour les réponse input()

    def reboot(self):
        self.listbox.delete(ANCHOR)

    def getreponse(self):
        if self.getr == string.digits:
            self.reponse.set(f"tu a écrit un chiffre ou des nombre : plus précesement {self.getr}")
            self.boutonreponse = Button(self.myframe, textvariable=self.reponse, command=self.getreponse).update()
        elif self.getr == string.ascii_lowercase:
            self.reponse.set(f"tu a des lettres en minuscule, : plus précesement {self.getr}")
            self.boutonreponse = Button(self.myframe, textvariable=self.reponse, command=self.getreponse).update()
        elif self.getr == string.ascii_uppercase:
            self.reponse.set(f"tu a écrit des lettres en majuscule : plus précesement {self.getr}")
            self.boutonreponse = Button(self.myframe, textvariable=self.reponse, command=self.getreponse).update()
        elif self.getr == string.punctuation:
            self.reponse.set(f"tu a écrit de la ponctuation, : plus précesement {self.getr}")
            self.boutonreponse = Button(self.myframe, textvariable=self.reponse, command=self.getreponse).update()
        else:
            pass


    #ce qui cencerne le scale
    def slide(self):
        self.horizontal_label = Label(self.myframe, text=self.horizontal.get()).pack()
main(fenetre)

fenetre.mainloop()
#but : toplevel, label, bouton, imaage(avec canvas) frame, message, scale, listbox, menu, scrollbar, entréé en classe
#entrainement collision pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
pygame.display.set_caption("test collision rect")
ecran = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# quelque variables
vitesse_x, vitesse_y = 5, 4
block2_vx, block2_vy = 2, 3
collision_tolerance = 10

block_1 = pygame.Rect(250, 400, 45 , 50)
block_2 = pygame.Rect(200, 100, 45, 40)


def draw_b_m():
    global vitesse_x, vitesse_y, block2_vx, block2_vy, collision_tolerance
    pygame.draw.rect(ecran, (255, 255, 255), block_1)
    pygame.draw.rect(ecran, (0, 255, 0), block_2)
    block_1.x += vitesse_x
    block_1.y += vitesse_y
    block_2.x += block2_vx
    block_2.y += block2_vy
    #sur les limite de l'écran
    if block_1.right >= WIDTH or block_1.left <= 0: #comme il avance se sera le coté droit qui sera en coll en x, Width
        vitesse_x *= -1
    if block_1.bottom >= HEIGHT or block_1.top <= 0: #en y Height
        vitesse_y *= -1
    #checker les collision des rebord avec le second rect
    if block_2.right > WIDTH or block_2.left <= 0:
        block2_vx *= -1
    if block_2.bottom > WIDTH or block_2.top <= 0:
        block2_vy *= -1
    #collision entre les rect et leurs positions
    if block_1.colliderect(block_2):
        if abs(block_2.top - block_1.bottom) < collision_tolerance:
            vitesse_y *= -1
        if abs(block_2.bottom - block_1.top) < collision_tolerance:
            vitesse_y *= -1
        if abs(block_2.left - block_1.right) < collision_tolerance:
            vitesse_y *= -1
        if abs(block_2.right - block_1.left) < collision_tolerance:
            vitesse_y *= -1
    #clecker les collisions à partir du block 2
    if block_2.colliderect(block_1):
        if abs(block_1.top - block_2.bottom)  < collision_tolerance:
            block2_vy *= -1
        if abs(block_1.bottom - block_2.top) < collision_tolerance:
            block2_vy *= -1
        if abs(block_1.left - block_2.right) < collision_tolerance:
            block2_vy *= -1
        if abs(block_1.right - block_2.left) < collision_tolerance:
            block2_vy *= -1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    ecran.fill((30, 30, 30))
    draw_b_m()
    pygame.display.flip()
    clock.tick(50)

#fonctionnement os
path = "C:/Users\guillaume"
os.chdir(path)
os.makedirs('python/test') #removedirs pour supprimer doss du doc
print(os.listdir(path))

#recherche dans l'arbor"escente
for dirpath, dirname, filename in os.walk(path):
    print("liens ordi : ", dirpath)
    print("endroit dans la path", dirname)
    print("dossier : ", filename)

#recherche d'un dossier
print(os.environ.get("python"))

