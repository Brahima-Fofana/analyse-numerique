import numpy as np
import matplotlib.pyplot as plt
from rectangle import rectangle, presentation


# ============================================================================
# TESTS
# ============================================================================

def test_methode_carree():
    """Test avec f(x) = x² - VOTRE fonction de test originale"""
    print("=" * 60)
    print("TEST MÉTHODE: f(x) = x²")
    print("=" * 60)

    def f(x):
        return x ** 2

    a, b = 1, 3
    m = 10

    resultat = rectangle(f, a, b, m)
    exacte = (b ** 3 - a ** 3) / 3

    print(f"Intervalle: [{a}, {b}]")
    print(f"Nombre d'intervalles: {m}")
    print(f"Résultat: {resultat:.6f}")
    print(f"Valeur exacte: {exacte:.6f}")
    print(f"Erreur: {abs(exacte - resultat):.6f}")

    presentation(f, a, b, m, "Méthode - f(x) = x²")


def test_methode_lineaire():
    """Test avec fonction linéaire"""
    print("\n" + "=" * 60)
    print("TEST MÉTHODE: f(x) = 3x - 2")
    print("=" * 60)

    def f(x):
        return 3 * x - 2

    a, b = 0, 4
    m = 8

    resultat = rectangle(f, a, b, m)
    exacte = (3 / 2) * b ** 2 - 2 * b - ((3 / 2) * a ** 2 - 2 * a)

    print(f"Intervalle: [{a}, {b}]")
    print(f"Nombre d'intervalles: {m}")
    print(f"Résultat: {resultat:.6f}")
    print(f"Valeur exacte: {exacte:.6f}")
    print(f"Erreur: {abs(exacte - resultat):.6f}")

    presentation(f, a, b, m, "Méthode - f(x) = 3x - 2")


def test_methode_sinus():
    """Test avec fonction sinus"""
    print("\n" + "=" * 60)
    print("TEST MÉTHODE: f(x) = sin(x)")
    print("=" * 60)

    def f(x):
        return np.sin(x)

    a, b = 0, np.pi
    m = 12

    resultat = rectangle(f, a, b, m)
    exacte = 2.0  # ∫sin(x)dx de 0 à π = 2

    print(f"Intervalle: [0, π]")
    print(f"Nombre d'intervalles: {m}")
    print(f"Résultat: {resultat:.6f}")
    print(f"Valeur exacte: {exacte:.6f}")
    print(f"Erreur: {abs(exacte - resultat):.6f}")

    presentation(f, a, b, m, "Méthode - f(x) = sin(x)")


def test_methode_exponentielle():
    """Test avec fonction exponentielle"""
    print("\n" + "=" * 60)
    print("TEST MÉTHODE: f(x) = exp(x)")
    print("=" * 60)

    def f(x):
        return np.exp(x)

    a, b = 0, 2
    m = 10

    resultat = rectangle(f, a, b, m)
    exacte = np.exp(b) - np.exp(a)

    print(f"Intervalle: [{a}, {b}]")
    print(f"Nombre d'intervalles: {m}")
    print(f"Résultat: {resultat:.6f}")
    print(f"Valeur exacte: {exacte:.6f}")
    print(f"Erreur: {abs(exacte - resultat):.6f}")

    presentation(f, a, b, m, "Méthode - f(x) = exp(x)")


def test_methode_complexe():
    """Test avec fonction plus complexe"""
    print("\n" + "=" * 60)
    print("TEST MÉTHODE: f(x) = x² + cos(x)")
    print("=" * 60)

    def f(x):
        return x ** 2 + np.cos(x)

    a, b = 0, 2
    m = 15

    resultat = rectangle(f, a, b, m)
    # Calcul de la valeur exacte
    exacte = (b ** 3 / 3 + np.sin(b)) - (a ** 3 / 3 + np.sin(a))

    print(f"Intervalle: [{a}, {b}]")
    print(f"Nombre d'intervalles: {m}")
    print(f"Résultat: {resultat:.6f}")
    print(f"Valeur exacte: {exacte:.6f}")
    print(f"Erreur: {abs(exacte - resultat):.6f}")

    presentation(f, a, b, m, "méthode - f(x) = x² + cos(x)")


def test_simple():
    """Votre test original avec visualisation"""
    print("\n" + "=" * 60)
    print("VOTRE TEST ORIGINAL AVEC VISUALISATION")
    print("=" * 60)

    def fct(x):
        return x ** 2

    a = 1
    b = 3
    m = 10  # Réduit pour mieux visualiser

    resultat = rectangle(fct, a, b, m)
    exacte = (b ** 3 - a ** 3) / 3

    print(f"Resultat methode rectangle : {resultat}")
    print(f"Resultat methode exacte : {exacte}")
    print(f"Erreur : {abs(exacte - resultat)}")

    presentation(fct, a, b, m, "Test original - f(x) = x²")


# ============================================================================
# EXÉCUTION UNIQUEMENT DE VOS TESTS
# ============================================================================

if __name__ == "__main__":
    print("TESTS")
    print("=" * 70)

    # Votre test original avec visualisation
    test_simple()

    # Tests spécifiques de votre méthode
    test_methode_carree()
    test_methode_lineaire()
    test_methode_sinus()
    test_methode_exponentielle()
    test_methode_complexe()
