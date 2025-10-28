from simpson import simpson
import numpy as np

print("\nTESTS DE LA MÉTHODE DES SIMPSON")
print("=" * 50)

# Test 1: f(x) = x² sur [1, 3]
def f1(x):
    return x ** 2

a1, b1 = 1, 3
m1 = 100
resultat1 = simpson(f1, a1, b1, m1)
exacte1 = (b1 ** 3 - a1 ** 3) / 3

print(f"Test 1 - f(x) = x² sur [{a1}, {b1}]")
print(f"Résultat simpson: {resultat1:.8f}")
print(f"Valeur exacte:     {exacte1:.8f}")
print(f"Erreur:           {abs(exacte1 - resultat1):.2e}")
print()

# Test 2: f(x) = sin(x) sur [0, π]
def f2(x):
    return np.sin(x)

a2, b2 = 0, np.pi
m2 = 100
resultat2 = simpson(f2, a2, b2, m2)
exacte2 = 2.0  # ∫sin(x)dx de 0 à π = 2

print(f"Test 2 - f(x) = sin(x) sur [{a2}, {b2}]")
print(f"Résultat simpson: {resultat2:.8f}")
print(f"Valeur exacte:     {exacte2:.8f}")
print(f"Erreur:           {abs(exacte2 - resultat2):.2e}")
print()

# Test 3: f(x) = e^x sur [0, 1]
def f3(x):
    return np.exp(x)

a3, b3 = 0, 1
m3 = 100
resultat3 = simpson(f3, a3, b3, m3)
exacte3 = np.exp(1) - 1

print(f"Test 3 - f(x) = exp(x) sur [{a3}, {b3}]")
print(f"Résultat simpson: {resultat3:.8f}")
print(f"Valeur exacte:     {exacte3:.8f}")
print(f"Erreur:           {abs(exacte3 - resultat3):.2e}")