import numpy as np

def relaxation(A, b, w=1.0, x0=None, tol=1e-10, max_iter=1000):
    A = np.array(A)
    if A.shape[0] != A.shape[1]: raise ValueError("la matrice n'est pas carré")
    n = len(b)
    if A.shape[0] != n : raise ValueError("Le produit matricielle n'est pas possible")

    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()

    if w <= 0 or w >= 2 : raise ValueError("Omega doit etre compris entre 0 et 1")

    x_new = np.zeros(n)
    for iter in range(max_iter):
        for i in range(n):
            somme_1 = np.dot(A[i, :i], x_new[:i])
            somme_2 = np.dot(A[i, i+1:], x[i+1:])

            x_new[i] = (1-w)*x[i] + (w/A[i,i])*(b[i] - somme_1 - somme_2)

        if np.linalg.norm(x_new - x) < tol:
            return x_new, iter+1

        x = x_new.copy()

    print("La convergence non atteint a l'iteration : ", iter)
    return x, max_iter

A = [[4,2,1], [3,5,1], [4,3,8]]
b = [2,4,3]

x, iter = relaxation(A,b)
print("solution de l'equation : ", x, " avec ", iter, " iteration")
print("solution numpy : ", np.linalg.solve(A,b))
