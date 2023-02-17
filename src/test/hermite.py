import numpy as np

np.set_printoptions(linewidth=100)
def hermite(xP, yP, s):
    leng = len(xP)
    matrix = np.zeros((2*leng, 2*leng-1))
    for i in range(leng):
        ind = 2*i
        matrix[ind][0] = xP[i]
        matrix[ind+1][0] = xP[i]

        matrix[ind][1] = yP[i]
        matrix[ind+1][1] = yP[i]

        matrix[ind+1][2] = s[i]

    leng *= 2
    for i in range(2, leng):
        for j in range(2, i+2):
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            den = matrix[i][0]-matrix[i-2][0]
            if den == 0:
                continue

            matrix[i][j] = (matrix[i][j-1]-matrix[i-1][j-1])/den

    print(matrix)
    #for row in matrix:
    #    print(row)
