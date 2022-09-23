import numpy as np

n=input("Ingrese un numero: ")
n=int (n)
m=np.array([[1,1],[1,0]])
for i in range(n):
    texto=np.linalg.matrix_power(m,n-i)
    
    print(texto[1,1])

