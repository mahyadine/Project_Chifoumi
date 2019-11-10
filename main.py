# -*- coding: utf-8 -*- #display accents
from random import randint #Allows the generation of random numbers
import os #The OS module in Python provides a way of using operating system dependentfunctionality.
import sys #The sys module provides functions and variables used to manipulate different parts of the Python runtime environment

print ("----------------------Welcome Chifoumi Game-----------------------------\n-----------------------Hello how are you--------------------------------")
print ("La régle du jeu est simple:\n- La pierre bat les ciseaux\n- La feuille bat la pierre\n- Les ciseaux battent la feuille")

def shifoumi(): #creation of the function
    user1 = input("Veuillez entrer votre prénom ").upper() #  asks for the player's name
    while len(user1) <= 1: # the loop requires to ask the name of the player
        print ("Merci d'entrer un prénom valide ")
        user1 = input("Veuillez entrer votre prénom ") # the user is asked to enter his name
    print ("Bonjour {} je te souhaite bon chance".format(user1))

    score_user1 = 0 #value user
    score_computer = 0 #value computer
    while score_user1 < 3 and score_computer < 3: #I create a loop as long as it does not have 3 continuous part
        player = input("Veuillez choisir entre pierre, feuille ou ciseaux ").lower() #player makes his choice)
        while player not in ("pierre", "feuille", "ciseaux"): # obligation to enter the correct spelling
            print("Merci de noter la bonne valeur")
            player = input("Veuillez choisir entre pierre, feuille ou ciseaux ").lower()
        print(player,"VS", end=" ")
        
        chosen = randint(1,3) #The choice of pc
        if chosen == 1:
            computer = "feuille"
            print("feuille")

        elif chosen == 2:
            computer = "ciseaux"
            print("ciseaux")

        else:
            computer = "pierre"
            print("pierre")

        if player == computer:
            print("Match Nul")

        elif player == "pierre" and computer == "feuille":
            score_computer = score_computer + 1
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))

        elif player == "feuille" and computer == "pierre":
            score_user1 = score_user1 + 1
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))

        elif player == "ciseaux" and computer == "pierre":
            score_computer = score_computer + 1
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))

        elif player == "pierre" and computer == "ciseaux":
            score_user1 = score_user1 + 1 
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))

        elif player == "feuille" and computer == "ciseaux":
            score_computer = score_computer + 1
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))

        elif player == "ciseaux" and computer == "feuille":
            score_user1 = score_user1 + 1
            print("Tu as {}, et le pc a {}".format(score_user1, score_computer))
    end=True
    while end:
        test=input("Voulez vous continuer oui ou non: ")
        if test == "oui":
            if __name__ == '__main__':
                shifoumi()
                os.execv(__file__, sys.argv)
        else:
            end=False

shifoumi()

