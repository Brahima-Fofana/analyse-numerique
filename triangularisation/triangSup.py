import numpy as np
import time

def triangSup(A, b):
    A = np.array(A, dtype=float)
    n,m = A.shape
    if n!=m: return None
    b = np.array(b, dtype=float)
    x = np.zeros(n)

    for i in range(n-1,-1,-1) :
        somme = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - somme)/A[i,i]

    return x

A = [[9,2,3], [0,1,2], [0,0,1]]
b = [2,1,1]

print(triangSup(A,b))
print(np.linalg.solve(A,b))

 # COMPARAISON EN FONCTION DU TEMPS
t1 = time.time()
triangSup(A,b)
t2 = time.time()

t3 = time.time()
np.linalg.solve(A,b)
t4 = time.time()

print("temps triangInf :", t2-t1)
print("temps solver :", t4-t3)



