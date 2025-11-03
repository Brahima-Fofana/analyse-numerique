import numpy as np
from matplotlib import pyplot as plt

def derive(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def newton(fct, x0 = 0, tol=1e-6, max_iter=100):

    x = x0
    for i in range(max_iter):
        fct_x = fct(x)
        df_x = derive(fct, x)

        if abs(df_x) < 1e-15 : raise ValueError("La derivé est nulle, la methode a echouer")
        x_next = x - (fct_x/df_x)

        if abs(x_next - x)  < tol:
            return x_next, i+1
        x = x_next

    print(f"La methode de Newtion n'a pas convergé après {max_iter} iterations")
    return x, max_iter


def racine_trouve(fct, point_intials):
    if len(point_intials) < 1: raise ValueError("la taille des point initial dois depasser 1")

    racineX = list()
    racineY = list()
    iterations_list = list()

    for i in point_intials:
        try:
            resultat, iter = newton(fct, x0=i)
            racine_arrondi = round(resultat, 8)
            racineX.append(racine_arrondi)
            racineY.append(fct(racine_arrondi))
            iterations_list.append(iter)
            print(f"x = {i:6.2f} → Convergence vers x = {resultat:.10f} (en {iter} itérations)")
        except ValueError as e:
            print(f"x0 = {i:6.2f} → Échec: {e}")

    return racineX, racineY, iterations_list

def presentation(x_point, fct, racineX, racineY, iterations_list, titre):
    y_point = [fct(i) for i in x_point]

    plt.figure(figsize=(12,8))
    plt.plot(x_point, y_point, 'b-', label='Courbe f(x)', linewidth=2)
    plt.plot(racineX, racineY, 'ro', markersize=8, label="Les zeros")
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3, label='y = 0')

    for i, (x, y, iters) in enumerate(zip(racineX, racineY, iterations_list)):
        plt.annotate(f'x={x:.3f}',
                     xy=(x, y), xytext=(x + 0.1, y + 0.5),
                     arrowprops=dict(arrowstyle='->', color='red', alpha=0.7))

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title(f"Méthode de Newton - {titre}")
    plt.show()


def fct(x):
    return x**2 - 4*x + 3

resultat, iter = newton(fct)
print(f"La zero de la fonction est {resultat}, obtenue a l'iteration {iter}")

point_initials = [0, 1]
racineX, racineY, iterations_list = racine_trouve(fct, point_initials)
x_point = np.linspace(-1, 5, 200)
presentation(x_point, fct, racineX, racineY, iterations_list, "x**2 - 4*x + 3")



