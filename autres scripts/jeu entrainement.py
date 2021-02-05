#le pendue
from random import randint, shuffle,
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



