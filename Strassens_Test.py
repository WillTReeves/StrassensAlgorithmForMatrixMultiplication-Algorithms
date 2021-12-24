from Stopwatch import stopwatch
from Matrix_Class import Matrix
from Strassens_Main import strassens

# For testing indivdual matrix sizes 

'''A,B = Matrix(16,16),Matrix(16,16)
A.random_fill(0,10)
B.random_fill(0,10)
print("matrix #1")
print(A)
print("matrix #2")
print(B)
C = strassens(A,B)
print("multiplied matrix")
print(C)'''


# For time testing with growing n sizes 
'''
n_sizes = [2, 4, 8, 16, 32, 64, 128,256]

for n in n_sizes:
    A,B = Matrix(n,n),Matrix(n,n)
    A.random_fill(0,10)
    B.random_fill(0,10)
    c = stopwatch()
    c.start()
    strassens(A,B)
    j = c.stop()
    print(n)
    print(j)
'''





