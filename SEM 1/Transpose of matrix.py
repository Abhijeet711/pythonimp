q="y"
while q.lower()=="y":
    rows=int(input("Enter no. rows: "))
    cols=int(input("Enter no. columns: "))

    print("enter the element of matrix: ")
    matrix=[[int(input()) for i in range(cols)]for i in range(rows)]
    print("your matrix is:")
    for n in matrix:
        print(n)

    result=[[0 for i in range(rows)] for j in range(cols)]
    for r in range(rows):
        for c in range(cols):
            result[c][r]=matrix[r][c]

    print("Transpose matrix is: ")
    for r in result:
        print(r)
    q=input("want to continue?(y/n): ")
