import time, os, random

class Game:
    def __init__(self, high_num, myName):
        self.high_num = high_num         
        self.myName = myName              
        self.guessesTaken = 0             
        self.number = random.randint(1, self.high_num)  
        self.guess = None   

    def get_guess(self):
        print('Prend un nombre')
        try:
            self.guess = int(input())   
                                        
        except ValueError:
            print('Reponse non valide')
            return False

        return True


    def play(self):
        print('Bon {},  Je pense à un nombre entre 1 et {}.'
            .format(self.myName, self.high_num))
        while self.guessesTaken < 6:
            if not self.get_guess():
                continue
            # else: self.guess gets changed in get_guess function

            self.guessesTaken += 1

            if self.guess < self.number:
                print('Trop Bas')

            if self.guess > self.number:
                print('Ttop haut')

            if self.guess == self.number:
                break

        if self.guess == self.number:
            print('Biens joué {} Tu as trouvé le bon nombre en  {} essais !'
                .format(self.myName, self.guessesTaken))
        else:
            print('Non le nombre que je pensais était : ', self.number)


def main():
    print('Salut, ton pseudo ?')
    myName = input()
    print("Ok, {}! Il y a deux niveaux de difficulté".format(myName))

    while True:
        print('Tape 1 pour le niveau  simple, 2 pour le plus difficil et q pour quitter')
        user_choice = input()

        if user_choice.lower().startswith('q'):
            print("Aurevoire")
            break

        try:
            user_choice = int(user_choice)
            if user_choice not in [1,2]:
                continue
        except ValueError:
            continue

        if user_choice == 1:
            # make easy game
            easy_game = Game(20, myName)
            # play easy game
            easy_game.play()

        elif user_choice == 2:
            # make difficult game
            diff_game = Game(30, myName)
            # play difficult game
            diff_game.play(), 


main() 



       

