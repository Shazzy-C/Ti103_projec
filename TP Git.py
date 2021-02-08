"""
Le but du TP d’aujourd’hui est d’écrire un script dans lequel :
1. Vous choisissez un nombre de 1 à 1000 et vous l’assignez à une variable
2. Puis, tant qu’un utilisateur ne frappe pas la touche ‘q’, vous lui demandez de choisir un nombre
entre 1 et 1000.
3. Si le nombre est inférieur à la variable assignée vous lui dites “Plus grand”
4. Si le nombre est supérieur à la variable assignée, vous lui dites “Plus petit”
5. L’utilisateur gagne s’il trouve la bonne valeur.
6. Vous devez tester que le nombre entré est correct. Par exemple, retournez une erreur si ce
qu’entre l’utilisateur n’est pas un nombre, ou n’est pas compris entre 1 et 1000.
"""
import random           #nombre aleatoire

import TP_import

chiffre = random.randint(1, 1000)
print(TP_import.naruto(TP_import.ma_variable))
while True:

    entree = input("Entrez un nombre entre 1 et 1000 puis entrée, faites 'q' puis entrée pour quitter: ")

    if entree == 'q':
        break

    elif not entree.isnumeric():   #Mettre les exclusions en premier.
        print("Vous devez entrer un nombre entier. ")
        continue

    elif int(entree) <= 0:
        print("Entrez un nombre plus grand ou egal a 1. ")
        continue

    elif int(entree) > 1000:
        print("Entrez un nombre plus petit ou egal a 1000. ")
        continue

    elif int(entree) < chiffre:
        print("Plus grand.")
        continue

    elif int(entree) > chiffre:
        print("Plus petit.")
        continue

    elif int(entree) == chiffre:
        print("Vous avez gagné !!! ")
        break

