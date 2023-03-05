max=100
def printMatrix(m, rowSize, colSize):
    for i in range(rowSize):
        for j in range(colSize):
            print(m[i][j],end=' ')
        print()

def multiplyMatrix(row1, col1, A, row2, col2, B):
    C=[[0 for i in range(max)] for j in range(max)]
    if (row2 != col1):
        print("not possible")
        return

    for i in range(row1):
        for j in range(col2):
            C[i][j]=0
            for k in range(row2):
                C[i][j]+=A[i][k]*B[k][j];

    print("Resultant Matrix: ")
    printMatrix(C, row1,col2)

if __name__=="__main__":
    A=[[0 for i in range(max)] for j in range(max)]
    B=[[0 for i in range(max)] for j in range(max)]

    row1 = int(input("Enter the number of rows of First Matrix: "))
    col1 = int(input("Enter the number of columns of First Matrix: "))

    print("enter the elements of first matrix: ")
    for i in range(row1):
        for j in range(col1):
            A[i][j] = int(input("A["+str(i)+"]["+str(j)+"]: "))

    row2 = int(input("Enter the number of rows of Second Matrix: "))
    col2 = int(input("Enter the number of columns of Second Matrix: "))

    print("enter the elements of second matrix: ")
    for i in range(row2):
        for j in range(col2):
            B[i][j] = int(input("B["+str(i)+"]["+str(j)+"]: "))
    
    print("First Matrix")
    printMatrix(A,row1,col1)

    print("Second Matrix")
    printMatrix(B,row2,col2)

    multiplyMatrix(row1, col1, A, row2, col2, B)
