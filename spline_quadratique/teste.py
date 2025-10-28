import time

import numpy as np
from spline_quadratique import presentation

methode = "Spline Quadratique"

# teste complique
x_point = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2]
y_point = [np.sin(x) + np.cos(2*x) for x in x_point]

def fct_complexe1(x):
    return np.sin(x) + np.cos(2*x)

x_vals_test = np.linspace(0, 2*np.pi, 200)

debut1 = time.time()
presentation(x_point, y_point, x_vals_test, fct_complexe1)
fin1 = time.time()
print("Temps d'execution teste n° 1 ", fin1 - debut1, " avec ", methode)


# teste 2
x_point = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y_point = [np.exp(-x/2) * np.sin(3*x) for x in x_point]

def fct_complexe2(x):
    return np.exp(-x/2) * np.sin(3*x)

x_vals_test = np.linspace(0, 4, 300)

debut2 = time.time()
presentation(x_point, y_point, x_vals_test, fct_complexe2)
fin2 = time.time()
print("Temps d'execution teste n° 2 ", fin2 - debut2, " avec ", methode)


# teste 3
x_point = [-3, -2, -1, 0.5, 1, 2, 3, 4]
y_point = [1/(1 + x**2) * np.sin(2*x) for x in x_point]

def fct_complexe3(x):
    return 1/(1 + x**2) * np.sin(2*x)

x_vals_test = np.linspace(-3, 4, 300)
debut3 = time.time()
presentation(x_point, y_point, x_vals_test, fct_complexe3)
fin3 = time.time()
print("Temps d'execution teste n° 3 ", fin3 - debut3, " avec ", methode)


# test 4
x_point = np.linspace(-5, 5, 15)  # 15 points
y_point = [np.exp(-x**2/8) * np.cos(2*x) for x in x_point]

def fct_complexe4(x):
    return np.exp(-x**2/8) * np.cos(2*x)

x_vals_test = np.linspace(-5, 5, 400)
debut4 = time.time()
presentation(x_point, y_point, x_vals_test, fct_complexe4)
fin4 = time.time()
print("Temps d'execution teste n° 4 ", fin4 - debut4, " avec ", methode)

# Fonction très oscillante
x_point = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
y_point = [np.sin(10*x) * np.exp(-x) for x in x_point]

def fct_oscillante(x):
    return np.sin(10*x) * np.exp(-x)

x_vals_test = np.linspace(0, 2, 500)
debut5 = time.time()
presentation(x_point, y_point, x_vals_test, fct_oscillante)
fin5 = time.time()
print("Temps d'execution teste n° 5", fin5 - debut5, " avec ", methode)


# Fonction à croissance exponentielle
x_point = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
y_point = [np.exp(x) * np.log(1 + x) for x in x_point]

def fct_croissance(x):
    return np.exp(x) * np.log(1 + x)

x_vals_test = np.linspace(0, 2.5, 200)
debut6 = time.time()
presentation(x_point, y_point, x_vals_test, fct_croissance)
fin6 = time.time()
print("Temps d'execution teste n° 6 ", fin6 - debut6, " avec ", methode)