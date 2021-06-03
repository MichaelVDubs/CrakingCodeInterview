def setToZero(matrix):
    cols = []
    rows = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for a in rows:
        for col in range(len(matrix[a])):
            matrix[a][col] = 0
    for a in cols:
        for row in range(len(matrix)):
            matrix[row][a] = 0

    return matrix


matrix = [[1, 2, 3, 3, 4], [1, 0, 2, 3, 5], [0, 1, 2, 3, 4]]

print(setToZero(matrix))
