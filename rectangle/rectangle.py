import numpy as np
from matplotlib import pyplot as plt


def rectangle(fct, a, b, m):
    if m <= 0 : raise ValueError("le nombre d'intervalle doit etre strictement positif")
    if a >= b : raise ValueError("a doit etre inferieur a b")

    h = (b-a)/m
    somme = 0
    for i in range(m):
        x_i = a + i*h
        somme += fct(x_i)

    integrale = h*(somme)

    return integrale


def presentation(fct, a, b, m, titre="Méthode des Rectangles"):
    h = (b - a) / m
    x_fin = np.linspace(a, b, 1000)
    y_fin = fct(x_fin)
    x_rect = np.linspace(a, b, m + 1)

    plt.figure(figsize=(12, 8))
    plt.plot(x_fin, y_fin, 'b-', linewidth=2, label='f(x)')

    for i in range(m):
        x_gauche = x_rect[i]
        x_droite = x_rect[i + 1]
        y_hauteur = fct(x_gauche)

        rect_x = [x_gauche, x_gauche, x_droite, x_droite, x_gauche]
        rect_y = [0, y_hauteur, y_hauteur, 0, 0]

        plt.fill(rect_x, rect_y, 'r', alpha=0.3, edgecolor='red', label='Rectangle gauche' if i == 0 else "")
        plt.plot([x_gauche, x_gauche], [0, y_hauteur], 'r-', alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'{titre} - n = {m} intervalles')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


# teste
def fct(x):
    return x**2

a = 1
b = 3
m = 100

resultat = rectangle(fct,a,b,m)
exacte = (b**3 - a**3) / 3

print(f"Resultat methode rectangle : {resultat}")
print(f"Resultat methode exacte : {exacte}")
print(f"Erreur : {abs(exacte - resultat)}")
