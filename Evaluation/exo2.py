def addition_liste(n1, n2):
    resultat = []
    retenue = 0

    # Parcours des listes
    i = len(n1) - 1
    j = len(n2) - 1

    # Parcourir les deux listes de droite à gauche
    while i >= 0 or j >= 0 or retenue > 0:
        x = n1[i] if i >= 0 else 0
        y = n2[j] if j >= 0 else 0
        s = x + y + retenue
        resultat.append(s % 10)
        retenue = s // 10
        i -= 1
        j -= 1
        
    # Inverser le résultat car il a été construit à l'envers
    return resultat[::-1]

# Exemple d'utilisation
print(addition_liste([1, 2, 3], [7]))  # Résultat attendu: [1, 3, 0]
print(addition_liste([8, 4, 0], [8, 3]))  # Résultat attendu: [9, 2, 3]
print(addition_liste([1, 8, 3], [7]))     # Résultat attendu: [1, 9, 0]

