# taking first matrix
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# taking second matrix
Y = [[10, 11, 12],
      [13, 14, 15],
      [16, 17, 18]]
# taking a blank result matrix
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterating through rows
for i in range(len(X)):
    # iterating through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]


# printing result matrix
for r in result:
    print(r)
