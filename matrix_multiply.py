def multiply(matrix1, matrix2):
    matrix = []    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        matrix.append(row)
    return matrix
matrix1 = [
[1,2,3],
[3,2,1]
]
matrix2 = [
[1,2],
[2,1],
[3,3]
]
print(multiply(matrix1, matrix2))