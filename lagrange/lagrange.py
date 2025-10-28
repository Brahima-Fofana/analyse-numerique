import time

import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas

def lagrange(x_point, y_point, x):
    if len(x_point) != len(y_point) : raise ValueError("Les points ne sont pas complet")
    n = len(x_point)

    poly_base = []
    for i in range(n):
        base_lagrange = 1.0
        for j in range(n):
            if j != i :
                base_lagrange *= (x - x_point[j])/(x_point[i] - x_point[j])
        poly_base.append(base_lagrange)

    poly = 0
    for i in range(n):
        poly += y_point[i] * poly_base[i]

    return poly


def presentation(x_point, y_point, x_vals_test, fct_test=None):
    y_vals = [lagrange(x_point, y_point, x) for x in x_vals_test]

    plt.figure(figsize=(10,6))
    if fct_test is not None:
        y_test_vals = [fct_test(x) for x in x_vals_test]
        plt.plot(x_vals_test, y_test_vals, 'g-', linewidth=2, label="Fonction Test")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_point, y_point, 'ro', markersize=8, label="point connus")
    plt.plot(x_vals_test, y_vals, 'b-', label='Polynome Lagrange', linewidth=2)
    plt.grid(True)
    plt.legend()
    plt.title("Interpolation methode Lagrange")
    plt.show()

# teste simple
x_point = [1,2,4]
y_point = [2,5,17]
x_vals_test = np.linspace(min(x_point), max(x_point), 10)

def fct_test(x):
    return x**2 + 1


debut0 = time.time()
presentation(x_point, y_point, x_vals_test, fct_test)
fin0 = time.time()
print("Temps d'execution teste n° 0 ", fin0 - debut0, " avec Lagrange")

