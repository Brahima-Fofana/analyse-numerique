import numpy as np
from matplotlib import pyplot as plt


def trapeze(fct, a, b, m):
    if m <= 0 : raise ValueError("le nombre d'intervalle doit etre strictement positif")
    if a >= b : raise ValueError("a doit etre superieur a b")

    h = (b-a)/m
    somme_interieur = 0
    for i in range(1, m):
        x_i = a + i*h
        somme_interieur += fct(x_i)

    integrale = 0.5*h*(fct(a) + 2*somme_interieur + fct(b))

    return integrale

def presentation(fct, a, b, m, titre="Méthode des Trapèzes"):

    h = (b - a) / m

    x_fin = np.linspace(a, b, 1000)
    y_fin = fct(x_fin)

    x_trap = np.linspace(a, b, m + 1)
    y_trap = fct(x_trap)

    plt.figure(figsize=(12, 8))

    plt.plot(x_fin, y_fin, 'b-', linewidth=2, label='f(x)')
    plt.plot(x_trap, y_trap, 'bo', markersize=4, label='Points d\'évaluation')

    for i in range(m):
        x_gauche = x_trap[i]
        x_droite = x_trap[i + 1]

        y_gauche = fct(x_gauche)
        y_droite = fct(x_droite)

        trap_x = [x_gauche, x_gauche, x_droite, x_droite, x_gauche]
        trap_y = [0, y_gauche, y_droite, 0, 0]

        plt.fill(trap_x, trap_y, 'g', alpha=0.3, edgecolor='darkgreen',
                 label='Trapèze' if i == 0 else "")

        plt.plot([x_gauche, x_gauche], [0, y_gauche], 'g-', alpha=0.6)
        plt.plot([x_droite, x_droite], [0, y_droite], 'g-', alpha=0.6)

        plt.plot([x_gauche, x_droite], [y_gauche, y_droite], 'r--', alpha=0.7,
                 label='Approximation linéaire' if i == 0 else "")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'{titre} - n = {m} intervalles')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    return h

# teste
def fct(x):
    return x**2

a = 1
b = 3
m = 100

resultat = trapeze(fct,a,b,m)
exacte = (b**3 - a**3) / 3

print(f"Resultat methode trapeze : {resultat}")
print(f"Resultat methode exacte : {exacte}")
print(f"Erreur : {abs(exacte - resultat)}")
