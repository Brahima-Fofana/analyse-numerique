import numpy as np

def jacoby(A, b, x0=None, tol=1e-10, max_iter=1000):
    A = np.array(A)
    if A.shape[0] != A.shape[1] : raise ValueError("La matrice n'est pas carré !")
    n = len(b)
    if A.shape[0] != n : raise ValueError("Le produit matriciel n'est pas possible")

    if x0 is None:
        x = np.zeros(n)
    else :
        x = x0.copy()

    x_new = np.zeros(n)

    for iter in range(max_iter):
        for i in range(n):
            somme = 0
            for j in range(n):
                if j != i:
                    somme = somme + A[i,j]*x[j]
            x_new[i] = (b[i] - somme)/A[i,i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new, iter+1

        x = x_new.copy()

    print("Convergence non attend apres ", max_iter, " iterations")
    return x, max_iter


A = [[4,2,1], [3,5,1], [4,3,8]]
b = [2,4,3]

x, iter = jacoby(A,b)
print("solution de l'equation : ", x, " avec ", iter, " iteration")
print("solution numpy : ", np.linalg.solve(A,b))