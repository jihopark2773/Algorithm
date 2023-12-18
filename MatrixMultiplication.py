def matrixmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

## Test Case 1
A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
result = matrixmul(A, B)
print(result)
