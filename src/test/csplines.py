import numpy as np

def csplines(xP, yP):
    leng = len(xP)

    h = lambda x: xP[x+1] - xP[x]

    matrix = np.zeros((leng, leng))
    matrix[0][0] = 1
    matrix[leng-1][leng-1] = 1

    for i in range(1, leng-1):
        matrix[i][i-1] = h(i-1)
        matrix[i][i] = 2*(h(i-1)+h(i))
        matrix[i][i+1] = h(i)

    print(matrix)

    b = np.zeros((leng))
    for i in range(1, leng-1):
        b[i] = (3/h(i))*(yP[i+1]-yP[i])-(3/h(i-1))*(yP[i]-yP[i-1])

    print(b)

    invMatrix = np.linalg.inv(matrix)
    x = invMatrix.dot(b)

    print(x)
