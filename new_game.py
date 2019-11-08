# -*- coding: utf-8 -*-
from random import randint #Allows the generation of random numbers

print ("----------------------Welcome Chifoumi Game-----------------------------\n-----------------------Hello how are you--------------------------------")
print ("La régle du jeu est simple:\n- La pierre bat les ciseaux\n- La feuille bat la pierre\n- Les ciseaux battent la feuille")

choix = ["1:pierre", "2:feuille", "3:ciseaux"]

user1 = input("Veuillez entrer votre prénom ").upper() #  asks for the player's name
while len(user1) <= 1: # the loop requires to ask the name of the player
    print ("Merci d'entrer un prénom valide ")
    user1 = input("Veuillez entrer votre prénom ")
print ("Bonjour", user1, "je te souhaite bon chance")

player = input("Veuillez choisir entre pierre, feuille ou ciseaux ").lower() #player makes his choice)
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



