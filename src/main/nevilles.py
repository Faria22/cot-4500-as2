import numpy as np

def nevilles(xP, yP, x):
    leng = len(xP)
    matrix = np.zeros((leng, leng))
    for i, row in enumerate(matrix):
        row[0] = yP[i]

    for i in range(1, leng):
        for j in range(1, i+1):
            firstM = (x-xP[i-j])*matrix[i][j-1]
            secondM = (x-xP[i])*matrix[i-1][j-1]

            den = xP[i] - xP[i-j]

            matrix[i][j] = (firstM-secondM)/den

    return matrix[leng-1][leng-1]
