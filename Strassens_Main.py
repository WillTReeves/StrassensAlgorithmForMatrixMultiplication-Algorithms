from Matrix_Class import Matrix

def strassens(A,B):
    if A.rownum <= 2:
        return matrixmultiply(A,B)
    a,b,c,d= A.split()
    e,f,g,h= B.split()
    a1 = strassens(a,e)
    a2 = strassens(a,f)
    b1 = strassens(b,g)
    b2 = strassens(b,h)
    c1 = strassens(c,e)
    c2 = strassens(c,f)
    d1 = strassens(d,g)
    d2 = strassens(d,h)
    tot1 = sum_matrix(a1, b1)
    tot2 = sum_matrix(a2, b2)
    tot3 = sum_matrix(c1,c2)
    tot4 = sum_matrix(d1, d2)
    complete = join_matrix(tot1,tot2,tot3,tot4)
    return complete

def join_matrix(a,b,c,d):
    n = a.rownum
    n2 = a.rownum + b.rownum
    A = Matrix(n2,n2)
    for y in range(n):
        for x in range(n):
            A.insert(y,x,a.matrix[y][x])
            A.insert(y,n + x,b.matrix[y][x])
            A.insert(n + y,x,c.matrix[y][x])
            A.insert(n +y,n + x,d.matrix[y][x])
    return A

def matrixmultiply(a, b):
    n = a.rownum
    A = Matrix(n,n)
    matrix = [
        [a.matrix[0][0] * b.matrix[0][0] + a.matrix[0][1] * b.matrix[1][0],
         a.matrix[0][0] * b.matrix[0][1] + a.matrix[0][1] * b.matrix[1][1]],
        [a.matrix[1][0] * b.matrix[0][0] + a.matrix[1][1] * b.matrix[1][0],
         a.matrix[1][0] * b.matrix[0][1] + a.matrix[1][1] * b.matrix[1][1]],
    ]
    for y in range(n):
        for x in range(n):
            A.insert(y,x,matrix[y][x])
    return A

def sum_matrix(A,B):
    n = A.rownum
    C = Matrix(n,n)
    for y in range(n):
        for x in range(n):
            c = A.matrix[y][x] + B.matrix[y][x]
            C.insert(y,x,c)
    return C