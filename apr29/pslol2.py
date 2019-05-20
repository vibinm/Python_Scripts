mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for index in range(len(mat)):
    mat[index] = mat[index][1:]

print(mat)
