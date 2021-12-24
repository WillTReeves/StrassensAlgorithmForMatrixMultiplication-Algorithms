import random

class Matrix:
    def __init__(self,rows,cols):
        self.rownum = rows
        self.colnum = cols
        self.matrix = [None] * rows
        for x in range(rows):
            self.matrix[x] = [None] * cols   
        
    def __str__(self):
        printy = ""
        index = 0
        for row in self.matrix:
            index += 1
            printy += str(row)
            if index != self.rownum:
                 printy += "\n"
        return(printy)
    
    def index(self,row,col):
        return self.matrix[row][col]
    
    def insert(self,row,col,value):
        self.matrix[row][col] = value

    def listinsert(self,listy):
        index = 0
        for y in range(self.rownum):
            for j in range(self.colnum): 
                if index == len(listy):
                    pass
                else:
                    self.insert(y,j,listy[index])
                    index += 1

    def insertrow(self,colnum,value):
        for y in range(len(self.matrix[colnum])):
            self.insert(colnum,y,value[y])
    
    def get_row(self,rowind):
        return self.matrix[rowind]

    def get_col(self,colnum):
        col = []
        for x in self.matrix:
            col.append(x[colnum])
        return col

    def random_fill(self,start,stop):
        for y in range(self.rownum):
            for x in range(self.colnum):
                num = random.randint(start,stop)
                self.insert(y,x,num)

    def split(self):
        n = len(self.matrix)
        mata = self.matrix[:n//2]
        matb = self.matrix[n//2:]
        mat1, mat2, mat3, mat4 = Matrix(n//2,n//2),Matrix(n//2,n//2),Matrix(n//2,n//2),Matrix(n//2,n//2)
        n1 = len(mata)
        n2 = len(mata[0])
        for x in range(n1):
            mat1.insertrow(x,mata[x][n//2:])
            mat2.insertrow(x,mata[x][:n//2])
            mat3.insertrow(x,matb[x][n//2:])
            mat4.insertrow(x,matb[x][:n//2])
        return mat2,mat1,mat4,mat3




                

    
    



