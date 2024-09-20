class Exo:
    def puissance(self, x, n):

        # Cas de base : tout nombre élevé à la puissance 0 vaut 1
        if n == 0:
            return 1
        # Cas d'un exposant positif : on utilise la relation de récurrence x^n = x * x^(n-1)
        elif n > 0:
            return x * self.puissance(x, n - 1)
        # Cas d'un exposant négatif : on utilise la propriété x^-n = 1 / x^n
        else:
            return 1 / self.puissance(x, -n)

# Création d'une instance de la classe Exo et appel de la méthode puissance
resultat = Exo().puissance(-3, -1)
print(resultat)
