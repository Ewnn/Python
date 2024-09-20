def somme_zero(liste):
    # Trier la liste pour faciliter la recherche de triplets
    liste.sort()
    triplets = []
    
    # Parcourir la liste
    for i in range(len(liste) - 2):
        if i > 0 and liste[i] == liste[i - 1]:
            continue
        
        # Méthode de deux pointeurs
        gauche = i + 1
        droite = len(liste) - 1
        
        while gauche < droite:
            somme = liste[i] + liste[gauche] + liste[droite]
            
            if somme == 0:
                triplets.append([liste[i], liste[gauche], liste[droite]])
                
                # Avance les deux pointeurs tout en évitant les doublons
                while gauche < droite and liste[gauche] == liste[gauche + 1]:
                    gauche += 1
                while gauche < droite and liste[droite] == liste[droite - 1]:
                    droite -= 1
                
                gauche += 1
                droite -= 1
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1
    
    return triplets

# Exemple d'utilisation
liste1 = [2, 7, 9, -9]
liste2 = [-33, -10, -8, -2, 1, 4, 9, 10]
resultat = somme_zero(liste1)
resultat2 = somme_zero(liste2)

print(resultat)
print(resultat2)