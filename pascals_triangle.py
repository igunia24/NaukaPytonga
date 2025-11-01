#!/usr/bin/env

n = int(input("What row of Pascal's Triangle do you want to see?"))
matrix = []
for i in range(n):
    matrix.append([1] * (i + 1))
    # print(f"##{i}")
    # print(matrix)
    if i >= 2:
        for j in range(1, i):
            # print(i, j)
            # print(matrix[i][j])
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

# print(matrix)
print(f"Values in the {n} row of Pascal's triangle are {matrix[n - 1]}")
