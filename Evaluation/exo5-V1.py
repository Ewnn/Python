import random

def jeu_plus_petit_plus_grand():
    low = 1
    maxi = 100
    coups = 0

    print("Mémorisez un nombre entier entre 1 et 100, le script va essayer de le retrouver, ne trichez pas : \n")

    while True:
        coups += 1
        tentative = random.randint(low, maxi)
        print(f"Script propose : {tentative}... +, - ou G ?")
            
        reponse = input().strip().upper()

        if reponse == 'G':
            print(f"Script a trouvé {tentative} en {coups} coups !!!")
            break
        elif reponse == "+":
            low = tentative + 1
        elif reponse == "-":
            maxi = tentative - 1
        else:
            print("Réponse invalide, merci de répondre par '+' / '-' ou 'G' !")
        
        # Vérification de triche
        if low > maxi:
            print("Tricheur !!!")
            print(f"J'ai gagné par forfait en {coups} coups !!!")
            break

# Appel de la fonction
jeu_plus_petit_plus_grand()
