import time

from simpson import simpson
from trapeze.trapeze import trapeze
from rectangle.rectangle import rectangle

def f(x):
    return x**2

a, b = 1, 3
m = 100
exacte = (b**3 - a**3) / 3

# Test des différentes méthodes
debut1 = time.time()
rectangle(f, a, b, m)
fin1 = time.time()

debut2 = time.time()
trapeze(f, a, b, m)
fin2 = time.time()

debut3 = time.time()
simpson(f, a, b, m)
fin3 = time.time()

print("=" * 50)
print("COMPARAISON DES MÉTHODES (n=100)")
print("=" * 50)
print(f"Valeur exacte: {exacte:.10f}")
print(f"Rectangle : {rectangle(f, a, b, m):.10f} (erreur: {abs(exacte - rectangle(f, a, b, m)):.2e}) (temps : {fin1 - debut1})")
print(f"Trapèzes:        {trapeze(f, a, b, m):.10f} (erreur: {abs(exacte - trapeze(f, a, b, m)):.2e}) (temps : {fin2 - debut2})")
print(f"Simpson:         {simpson(f, a, b, m):.10f} (erreur: {abs(exacte - simpson(f, a, b, m)):.2e}) (temps : {fin3 - debut3})")