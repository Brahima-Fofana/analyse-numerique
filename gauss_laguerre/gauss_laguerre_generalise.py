import numpy as np
from scipy.special import roots_genlaguerre


def gauss_laguerre_generalise(f, n, alpha):
    # Récupérer les racines (x_i) et poids (w_i) du Laguerre généralisé
    x_i, w_i = roots_genlaguerre(n, alpha)

    # Approximation de l'intégrale
    return np.sum(w_i * f(x_i))


# Exemple : intégrer f(x) = x^2 sur [0, +∞)
# ∫₀^∞ x^α e^{-x} x² dx = Γ(α + 3)
from math import gamma

alpha = 2
f = lambda x: x ** 2
n = 5
resultat = gauss_laguerre_generalise(f, n, alpha)

print(f"Résultat ≈ {resultat:.8f}")
print("Valeur exacte =", gamma(alpha + 3))
