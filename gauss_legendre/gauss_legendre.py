import numpy as np


def gauss_legendre(f, a, b, n):
    # Obtenir les racines (x_i) et poids (w_i) du polynôme de Legendre de degré n
    x_i, w_i = np.polynomial.legendre.leggauss(n)

    # Changement de variable pour [a,b]
    t = 0.5 * (b - a) * x_i + 0.5 * (b + a)
    return 0.5 * (b - a) * np.sum(w_i * f(t))


# Exemple : intégrer f(x) = x^2 entre 0 et 1
f = lambda x: x ** 2
resultat = gauss_legendre(f, 0, 1, 3)  # n=3 points de Gauss
print(f"Résultat ≈ {resultat:.8f}")

# Comparaison avec la vraie valeur
print("Valeur exacte :", 1 / 3)
