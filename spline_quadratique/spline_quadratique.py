import time

import matplotlib.pyplot as plt
import numpy as np

def coef_b(x_point, y_point, b_prev, i):
    if i == 0:
        return 0
    b = (2*(y_point[i] - y_point[i-1])/(x_point[i] - x_point[i-1])) - b_prev
    return  b


def spline_quadratique(x_point, y_point, x):
    if len(x_point) != len(y_point) : raise ("La taille des cordonnés de x et y ne sont pas conforme !")
    n = len(x_point)

    spline = np.zeros(n-1)

    intervalle = 0
    for i in range(n-1):
        if x_point[i] <= x  <= x_point[i+1]:
            intervalle = i
            break
        elif i == n-2:
            intervalle = n-2

    b_coeffs = [0]
    for i in range(1, n):
        b_i = coef_b(x_point, y_point, b_coeffs[i-1], i)
        b_coeffs.append(b_i)

    i = intervalle
    a = (b_coeffs[i+1] - b_coeffs[i]) / (2 * (x_point[i+1] - x_point[i]))
    b = b_coeffs[i]
    c = y_point[i]

    resultat = a*(x -x_point[i])**2 + b*(x - x_point[i]) + c

    return resultat


def presentation(x_point, y_point, x_vals_test, fct_test=None):
    y_vals = [spline_quadratique(x_point, y_point, x) for x in x_vals_test]

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
    plt.title("Interpolation methode Spline Quadratique")
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
print("Temps d'execution teste n° 0 ", fin0 - debut0, " avec Spline Quadratique")