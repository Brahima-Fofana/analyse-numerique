import numpy as np


def gauss_chebyshev(f, n):
    # Points de Gauss-Chebyshev (abscisses)
    x_i = np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))

    # Poids (tous égaux)
    w_i = np.pi / n

    # Approximation de l'intégrale
    return w_i * np.sum(f(x_i))


# Exemple : intégrer f(x) = x^2 / sqrt(1 - x^2) sur [-1, 1]
# (f(x) doit être multiplié par le poids implicite 1/sqrt(1-x^2))
f = lambda x: x ** 2
n = 5
resultat = gauss_chebyshev(f, n)

print(f"Résultat ≈ {resultat:.8f}")
print("Valeur exacte = π/2 ≈", np.pi / 2)
