# Résumé des principales méthodes d’analyse numérique

## 1. Méthode de Jacobi
**Idée générale :**  
Méthode itérative pour résoudre un système linéaire \( A x = b \) en isolant chaque variable.  

**Formule :**  
\[
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
\]

---

## 2. Méthode de relaxation (Gauss-Seidel ou SOR)
**Idée générale :**  
Amélioration de Jacobi : les valeurs déjà calculées sont immédiatement réutilisées.  
(SOR ajoute un facteur de relaxation \( \omega \) pour accélérer la convergence.)

**Formule (Gauss-Seidel) :**  
\[
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
\]

**Formule (SOR) :**  
\[
x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
\]

---

## 3. Interpolation de Lagrange
**Idée générale :**  
Construit un polynôme \( P(x) \) passant exactement par les points donnés \((x_i, y_i)\).

**Formule :**  
\[
P(x) = \sum_{i=0}^{n} y_i \prod_{j=0, j \ne i}^{n} \frac{x - x_j}{x_i - x_j}
\]

---

## 4. Spline quadratique
**Idée générale :**  
Approxime une fonction par morceaux de **polynômes du second degré** assurant la continuité des dérivées.

**Forme générale sur chaque intervalle \([x_i, x_{i+1}]\) :**  
\[
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2
\]

Les coefficients \(a_i, b_i, c_i\) sont déterminés pour assurer la continuité de \(S\) et de \(S'\).

---

## 5. Méthode des rectangles
**Idée générale :**  
Approxime l’intégrale d’une fonction par la somme des aires de rectangles.

**Formule :**  
\[
\int_a^b f(x) \, dx \approx h \sum_{i=0}^{n-1} f(x_i)
\]
avec \(h = \frac{b - a}{n}\)

---

## 6. Méthode des trapèzes
**Idée générale :**  
Approxime l’intégrale par la somme des aires de trapèzes entre les points.  

**Formule :**  
\[
\int_a^b f(x) \, dx \approx \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]
\]

---

## 7. Méthode de Simpson
**Idée générale :**  
Utilise des **paraboles** pour mieux approximer l’intégrale sur chaque sous-intervalle.  

**Formule (Simpson 1/3) :**  
\[
\int_a^b f(x) \, dx \approx \frac{h}{3} \left[ f(x_0) + 4\sum_{i=1,\,\text{impair}}^{n-1} f(x_i) + 2\sum_{i=2,\,\text{pair}}^{n-2} f(x_i) + f(x_n) \right]
\]

---

## 8. Méthode de Newton (Newton-Raphson)
**Idée générale :**  
Méthode itérative pour trouver les racines de \( f(x) = 0 \) en utilisant la tangente.  

**Formule :**  
\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]
