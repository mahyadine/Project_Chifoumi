# -*- coding: utf-8 -*-
from random import randint #Allows the generation of random numbers

print ("----------------------Welcome Chifoumi Game-----------------------------\n-----------------------Hello how are you--------------------------------")
print ("La régle du jeu est simple:\n- La pierre bat les ciseaux\n- La feuille bat la pierre\n- Les ciseaux battent la feuille")

user1 = input("Veuillez entrer votre prénom ").upper() #  asks for the player's name
while len(user1) <= 1: # the loop requires to ask the name of the player
    print ("Merci d'entrer un prénom valide ")
    user1 = input("Veuillez entrer votre prénom ")
print ("Bonjour {} je te souhaite bon chance".format(user1))

score_user1 = 0
score_computer = 0
while score_user1 < 3 and score_computer < 3:
    player = input("Veuillez choisir entre pierre, feuille ou ciseaux ").lower() #player makes his choice)
    while player not in ("pierre", "feuille", "ciseaux"):
        print("Merci de noter la bonne valeur")
        player = input("Veuillez choisir entre pierre, feuille ou ciseaux ").lower()
    print(player,"VS", end=" ")
    chosen = randint(1,3)

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









