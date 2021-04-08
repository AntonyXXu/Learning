def rotateMatrix1(matrix):
    N = len(matrix)
    for i in range(N//2+N%2):
        for j in range(N//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N-1-j][i]
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
            matrix[j][N-1-i] = temp
            print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix1(matrix)
print(matrix)

# matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
# def transpose(matrix):
#     N = len(matrix)
#     for i in range(N):
#         for j in range(i,N):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
            
# def reflect(matrix):
#     N = len(matrix)
#     for i in range(N):
#         for j in range(N//2):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[i][N-1-j]
#             matrix[i][N-1-j] = temp

# transpose(matrix2)
# reflect(matrix2)
# print(matrix2)