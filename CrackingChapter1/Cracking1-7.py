
def rotateByNinetyCopy(matrix):
    matrixLength = len(matrix)
    w, h = matrixLength, matrixLength
    rotatedMatrix = [['' for x in range(w)] for y in range(h)]
    for row in range(matrixLength):
        for col in range(matrixLength):
            temp = matrixLength - row - 1
            rotatedMatrix[col][temp] = matrix[row][col]

    return rotatedMatrix


matrix = [['1', '2', '3'],
          ['a', 'b', 'c'],
          ['4', '5', '6']]


print("Before: " + str(matrix))
print("After: " + str(rotateByNinetyCopy(matrix)))
