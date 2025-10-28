import numpy as np
from matplotlib import pyplot as plt

from newton import  presentation, racine_trouve

# ============================================================================
# FONCTIONS TESTS VARIÉES
# ============================================================================

def test_polynome_3_racines():
    """Polynôme avec 3 racines réelles distinctes"""
    print("\n" + "=" * 60)
    print
    "POLYNÔME CUBIQUE - 3 RACINES RÉELLES"
    print("=" * 60)

    def f(x):
        return x ** 3 - 6 * x ** 2 + 11 * x - 6  # = (x-1)(x-2)(x-3)

    # Racines exactes: 1, 2, 3
    x_point = np.linspace(0, 4, 400)
    point_initials = [-1, 0.5, 1.5, 2.5, 4, 5]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = x³ - 6x² + 11x - 6")


def test_polynome_racine_double():
    """Polynôme avec racine double (convergence plus lente)"""
    print("\n" + "=" * 60)
    print("POLYNÔME AVEC RACINE DOUBLE")
    print("=" * 60)

    def f(x):
        return x ** 3 - 4 * x ** 2 + 5 * x - 2  # = (x-1)²(x-2)

    # Racines: 1 (double), 2
    x_point = np.linspace(0, 3, 400)
    point_initials = [-1, 0, 0.5, 1.2, 1.8, 3]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = x³ - 4x² + 5x - 2 (racine double en x=1)")


def test_fonction_trigonometrique():
    """Fonction trigonométrique avec plusieurs zéros"""
    print("\n" + "=" * 60)
    print("FONCTION TRIGONOMÉTRIQUE - MULTIPLES ZÉROS")
    print("=" * 60)

    def f(x):
        return np.sin(x) + 0.5 * np.cos(2 * x)

    # Plusieurs zéros dans l'intervalle
    x_point = np.linspace(-5, 5, 400)
    point_initials = [-4, -2, -1, 0, 1, 2, 3, 4]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = sin(x) + 0.5·cos(2x)")


def test_fonction_exponentielle():
    """Fonction avec composante exponentielle"""
    print("\n" + "=" * 60)
    print("FONCTION EXPONENTIELLE")
    print("=" * 60)

    def f(x):
        return np.exp(-x) * np.sin(2 * x) - 0.5

    x_point = np.linspace(-2, 5, 400)
    point_initials = [-1, 0, 1, 2, 3, 4]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = e^(-x)·sin(2x) - 0.5")


def test_fonction_rationnelle():
    """Fonction rationnelle avec asymptote"""
    print("\n" + "=" * 60)
    print("FONCTION RATIONNELLE")
    print("=" * 60)

    def f(x):
        return (x ** 2 - 1) / (x - 2)  # Asymptote en x=2

    x_point = np.linspace(-3, 4, 400)
    # Éviter x=2 (asymptote)
    point_initials = [-2, 0, 1, 2.5, 3]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = (x² - 1)/(x - 2)")


def test_fonction_complexe():
    """Fonction avec plusieurs oscillations"""
    print("\n" + "=" * 60)
    print("FONCTION COMPLEXE - MULTIPLES OSCILLATIONS")
    print("=" * 60)

    def f(x):
        return np.sin(3 * x) * np.exp(-0.1 * x) * (x - 2)

    x_point = np.linspace(-2, 10, 400)
    point_initials = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = sin(3x)·e^(-0.1x)·(x-2)")


def test_cas_difficile():
    """Cas difficile - fonction plate avec zéros très proches"""
    print("\n" + "=" * 60)
    print("CAS DIFFICILE - FONCTION PLATE")
    print("=" * 60)

    def f(x):
        return (x - 1.5) ** 3 * (x - 1.5001) ** 2

    # Zéros très proches : 1.5 et 1.5001
    x_point = np.linspace(1.4, 1.6, 400)
    point_initials = [1.45, 1.5, 1.55]

    racineX, racineY, iterations_list = racine_trouve(f, point_initials)
    presentation(x_point, f, racineX, racineY, iterations_list, "f(x) = (x-1.5)³·(x-1.5001)² (zéros très proches)")


# ============================================================================
# EXÉCUTION DE TOUS LES TESTS
# ============================================================================

if __name__ == "__main__":
    print("TESTS COMPLETS DE LA MÉTHODE DE NEWTON")
    print("Avec différentes fonctions pour visualiser les zéros")

    test_polynome_3_racines()  # 3 racines bien séparées
    test_polynome_racine_double()  # Convergence plus lente
    test_fonction_trigonometrique()  # Multiples zéros périodiques
    test_fonction_exponentielle()  # Comportement exponentiel
    test_fonction_rationnelle()  # Avec asymptote
    test_fonction_complexe()  # Multiples oscillations
    test_cas_difficile()  # Zéros très proches