
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
