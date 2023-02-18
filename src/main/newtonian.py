import numpy as np

def ddt(xP, yP):
    leng = len(xP)
    matrix = np.zeros((leng, leng))

    for i in range(leng):
        matrix[i][0] = yP[i]

    for i in range(1, leng):
        for j in range(1, i+1):
            matrix[i][j] = (matrix[i][j-1]-matrix[i-1][j-1])/(xP[i]-xP[i-j])

    return matrix

def newtonian(matrix, xP, x, order):
    xS = 1
    result = matrix[0][0]
    for i in range(1, order+1):
        xS *= x - xP[i-1]
        result += matrix[i][i]*xS

    return result
