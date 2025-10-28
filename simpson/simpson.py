import numpy as np


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
