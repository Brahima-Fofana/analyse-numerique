import numpy as np
from matplotlib import pyplot as plt


def simpson(fct, a, b, m):
    if m % 2 != 0 : raise ValueError("le nombre d'intervalle doit etre un nombre pair")
    if m <= 0 : raise ValueError("le nombre d'intervalle doit etre strictement positif")
    if a >= b : raise ValueError("a doit etre inferieur a b")

    h = (b-a)/m

    somme_interieur_impaire = 0
    somme_interieur_paire = 0
    for i in range(1, m):
        x_i = a + i*h
        if i%2 == 1:
            somme_interieur_impaire += fct(x_i)
        else:
            somme_interieur_paire += fct(x_i)

    integrale = (h/3)*(fct(a) + 4*somme_interieur_impaire + 2*somme_interieur_paire + fct(b))

    return integrale

def presentation(fct, a, b, m, titre="Méthode de Simpson"):

    if m % 2 != 0:
        m = m + 1

    h = (b - a) / m

    # Points pour la courbe exacte
    x_fin = np.linspace(a, b, 1000)
    y_fin = fct(x_fin)

    # Points de Simpson
    x_simp = np.linspace(a, b, m + 1)
    y_simp = fct(x_simp)

    plt.figure(figsize=(14, 8))

    # 1. Tracer la courbe exacte
    plt.plot(x_fin, y_fin, 'b-', linewidth=2, label='f(x) exacte')

    # 2. Tracer les points d'évaluation avec des couleurs différentes
    for i, (x, y) in enumerate(zip(x_simp, y_simp)):
        if i == 0 or i == m:  # Points extrêmes (a et b)
            plt.plot(x, y, 'ro', markersize=8, label='Points extrêmes' if i == 0 else "")
        elif i % 2 == 1:  # Points impairs
            plt.plot(x, y, 'go', markersize=6, label='Points impairs' if i == 1 else "")
        else:  # Points pairs
            plt.plot(x, y, 'mo', markersize=6, label='Points pairs' if i == 2 else "")

    # 3. Dessiner les paraboles d'approximation
    for i in range(0, m, 2):  # Par pas de 2 (3 points par parabole)
        x0 = x_simp[i]
        x1 = x_simp[i + 1]  # Point milieu
        x2 = x_simp[i + 2]

        y0 = fct(x0)
        y1 = fct(x1)
        y2 = fct(x2)

        # Calcul des coefficients de la parabole passant par les 3 points
        # Parabole: P(x) = Ax² + Bx + C
        A = (y2 - 2 * y1 + y0) / (2 * h * h)
        B = (y2 - y0) / (2 * h)
        C = y1 - A * x1 * x1 - B * x1

        # Tracer la parabole d'approximation
        x_para = np.linspace(x0, x2, 50)
        y_para = A * x_para ** 2 + B * x_para + C

        plt.plot(x_para, y_para, 'r--', alpha=0.7, linewidth=2,
                 label='Parabole Simpson' if i == 0 else "")

        # Remplir l'aire sous la parabole
        plt.fill_between(x_para, y_para, alpha=0.2, color='orange',
                         label='Aire Simpson' if i == 0 else "")

        # Annoter les coefficients
        plt.annotate(f'Para {i // 2 + 1}', xy=(x1, y1), xytext=(x1, y1 + 0.5),
                     arrowprops=dict(arrowstyle='->', color='red', alpha=0.5))

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'{titre} - n = {m} intervalles (Coefficients: 1,4,2,4,...,2,4,1)')
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

resultat = simpson(fct,a,b,m)
exacte = (b**3 - a**3) / 3

print(f"Resultat methode simson : {resultat}")
print(f"Resultat methode exacte : {exacte}")
print(f"Erreur : {abs(exacte - resultat)}")
