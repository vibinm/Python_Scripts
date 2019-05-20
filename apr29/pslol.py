mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat[1][1] = 'x'  # update an element
print(mat)
print()

mat[2].append(10)   # append an item to row
print(mat)
print()

mat.insert(1, [11, 12, 13])   # insert a row into the mat
print(mat)
print()

mat[0].pop(0)
print(mat)
print()

for row in mat:
    for col in row:
        print(col, end='\t')
    print()
