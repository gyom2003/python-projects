import random, time, sys

pierre = 1
papier = 2
ciseaux = 3

nomsobj = {pierre: "Pierre", papier: "Papier", ciseaux: "Ciseaux"} 
regles  = {pierre: ciseaux, papier: pierre, ciseaux: papier} 

player_score = 0
ordi_score = 0

def mainFunction():
	print("Jeu pierre feuille sciseaux")
	while regroupement():
		pass
	scores()

def regroupement():
	player_Reference = actions()
	ordi_Reference = random.randint(1, 3)
	resultat(player_Reference, ordi_Reference)
	return relancer_partie()



def actions():
	while True:
		player = input("Pierre = 1\n Papier = 2 \n ciseaux = 3\n à tois de choisir")
		try:
			if int(player) in (1, 2, 3):
				return int(player)
		except ValueError:
			continue
		print("il y a une erreure")

def resultat(player, ordi):
	#{}
	print("l'ordinateur à choisis: {}"
	.format(nomsobj[ordi]))
	#pour décoder ne nombre choisis + recup
	global player_score, ordi_score

	if player == ordi: 
		print("vous avez choisis le meme null")
	else: 
		#le résultat est le perdant
		if regles[player] == ordi: 
			print("tu as gagne !")
			player_score += 1, 
		else: 
			print("tu as perdus")
			ordi_score += 1

def relancer_partie():
	again_answer = input("Veut tu encores jouer ou non ? o/n")
	if again_answer in ("o", "n", "oui", "non"):
		pass
	else:
		print("ok à plus dans le bus")
		sys.exit()
		#break

def scores():
	#recupere var ninitées
	global player_score, ordi_score 
	print("Les scores des deux joueurs")
	print("Player: {}".format(player_score))
	print("Ordinateur: {}".format(ordi_score))

mainFunction()

