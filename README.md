# Résumé des principales méthodes d’analyse numérique

## 1. Méthode de Jacobi
**Idée générale :**  
Méthode itérative pour résoudre un système linéaire Ax = b en isolant chaque variable.  

**Formule :**  
x_i^(k+1) = (1 / a_ii) * (b_i - Σ_{j ≠ i} a_ij * x_j^(k))

---

## 2. Méthode de relaxation (Gauss-Seidel ou SOR)
**Idée générale :**  
Amélioration de Jacobi : les nouvelles valeurs calculées sont immédiatement réutilisées.  
La méthode SOR ajoute un facteur de relaxation ω pour accélérer la convergence.  

**Formule (Gauss-Seidel) :**  
x_i^(k+1) = (1 / a_ii) * (b_i - Σ_{j < i} a_ij * x_j^(k+1) - Σ_{j > i} a_ij * x_j^(k))

**Formule (SOR) :**  
x_i^(k+1) = (1 - ω) * x_i^(k) + (ω / a_ii) * (b_i - Σ_{j < i} a_ij * x_j^(k+1) - Σ_{j > i} a_ij * x_j^(k))

---

## 3. Interpolation de Lagrange
**Idée générale :**  
Construit un polynôme P(x) qui passe exactement par les points donnés (x_i, y_i).  

**Formule :**  
P(x) = Σ_{i=0}^{n} [ y_i * Π_{j=0, j ≠ i}^{n} (x - x_j) / (x_i - x_j) ]

---

## 4. Spline quadratique
**Idée générale :**  
Approxime une fonction par morceaux de polynômes du second degré assurant la continuité.  

**Formule sur [x_i, x_{i+1}] :**  
S_i(x) = a_i + b_i * (x - x_i) + c_i * (x - x_i)²

---

## 5. Méthode des rectangles
**Idée générale :**  
Approxime une intégrale par la somme des aires de rectangles.  

**Formule :**  
∫ₐᵇ f(x) dx ≈ h * Σ_{i=0}^{n-1} f(x_i)  
où h = (b - a) / n

---

## 6. Méthode des trapèzes
**Idée générale :**  
Approxime une intégrale par la somme des aires de trapèzes entre les points.  

**Formule :**  
∫ₐᵇ f(x) dx ≈ (h / 2) * [ f(x₀) + 2Σ_{i=1}^{n-1} f(x_i) + f(x_n) ]

---

## 7. Méthode de Simpson
**Idée générale :**  
Approxime une intégrale en utilisant des paraboles sur chaque sous-intervalle.  

**Formule (Simpson 1/3) :**  
∫ₐᵇ f(x) dx ≈ (h / 3) * [ f(x₀) + 4Σ_{i impair} f(x_i) + 2Σ_{i pair} f(x_i) + f(x_n) ]

---

## 8. Méthode de Newton (Newton-Raphson)
**Idée générale :**  
Méthode itérative pour trouver les racines de f(x) = 0 à l’aide des tangentes.  

**Formule :**  
x_(n+1) = x_n - f(x_n) / f'(x_n)
