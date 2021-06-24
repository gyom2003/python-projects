import time
import random, sys

class JoeurClass:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.person = None
        
        
    def beattaque(self, damage):
        self.health -= damage
        print("Tu viens de recevoire {} degats !"
        .format(damage))
        return self.health
        
    def attaque(self):
        damage = self.attack
        eref = FirstEnemy(50, 10, "zombie")
        eref.healthenemy -= damage
        return eref.healthenemy
        #return damage
        
        
    
    def fuire():
        time.sleep(1)
        sys.exit()
        
    def get_pseudo(self):
        return self.pseudo
            
        
    
class FirstEnemy:
    def __init__(self, healthenemy, attackenemy, enemypseudo):
        self.healthenemy = healthenemy, 
        self.attackenemy = attackenemy, 
        self.enemypseudo = enemypseudo, 
        
    def get_pseudo(self):
        return self.enemypseudo
    
    def enemybeattaque(self, thedamage):
        self.healthenemy -= thedamage
        print("l'enemie vient de recevoire {} degats !"
        .format(thedamage))
        return self.healthenemy
        
        
        
    


def mainFunction(): #{}
    while True:
        print("quelle est ton pseudo ?")
        myname = str(input())
        joueurreference = JoeurClass(myname, 100, 20)
        firstenemyreference = FirstEnemy(50, 10, "zombie")
        print("Bonjour {}, voici les caractéristiques de ton personnage"
        .format(myname))
        time.sleep(1)
        print("pseudo: {}, points de vies: {}, points d'attaques: {}"
        .format(joueurreference.pseudo, joueurreference.health, joueurreference.attack))
        print("Tu est en face de ton premier enemie veut tu te battre ou partir ? (b ou p)")
        combatresponse = input()
        try:
            if combatresponse.lower() not in ('b', 'p'):
                print("Choisis entre b et p")
            else: 
                time.sleep(1)
                if combatresponse == 'b':
                    print(joueurreference.get_pseudo(), "viens d'attaquer", firstenemyreference.get_pseudo(), "!")
                    firstenemyreference.enemybeattaque(20)
                    print("l'enemie à désormais {} points de vies"
                    .format(30))
                    time.sleep(1)
                    print("Maintenant", firstenemyreference.get_pseudo(), "viens d'attaquer", joueurreference.get_pseudo(), "!")
                    joueurreference.beattaque(10)
                    time.sleep(1)
                    print("tu as désormais {} points de vies"
                    .format(joueurreference.health))
                    #joueurreference.attaque(firstenemyreference, joueurreference.attack)
                    
                elif combatresponse == 'p':
                    print("Premier matche terminé")
                    joueurreference.fuire
                    
        except ValueError:
            continue
            
    
    
mainFunction()
    
