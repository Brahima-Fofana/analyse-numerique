import numpy as np


def gauss_laguerre(f, n):
    # Obtenir les racines (x_i) et poids (w_i) du polynôme de Laguerre d'ordre n
    x_i, w_i = np.polynomial.laguerre.laggauss(n)

    # Approximation de l'intégrale
    return np.sum(w_i * f(x_i))


# Exemple : intégrer f(x) = x^2 sur [0, +∞)
# I = ∫₀^∞ e^{-x} x² dx = 2
f = lambda x: x ** 2
n = 5  # nombre de points
resultat = gauss_laguerre(f, n)

print(f"Résultat ≈ {resultat:.8f}")
print("Valeur exacte = 2")
