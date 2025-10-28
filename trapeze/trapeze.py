import numpy as np


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
