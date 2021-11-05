import numpy as np
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

a = True
while a:
    dim = input("Введіть розмір матриці: ")
    while True:
        if dim.isdigit() == False:
            dim = input("Ви ввели не правильне значення : ")
        else:
            break
def determinant(a):
    assert len(a.shape) == 2 
    assert a.shape[0] == a.shape[1] 
    n = a.shape[0]
   
    for k in range(0, n-1):
       
        for i in range(k+1, n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                
    return np.prod(np.diag(a))

matrix = np.random.rand(50, 50)


print(determinant(matrix))
print(determinant(matrix))