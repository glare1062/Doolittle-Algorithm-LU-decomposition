import numpy as np


def Doolittle(A, n):
    # returns 0s in arrays of size for lower and upper matrices
    L = np.zeros((n, n), dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)

    for row in range(0, n):
        # to add 1 to each lower matrix
        L[row][row] = 1

        # calc value for upper matrix column vise
        for column in range(row, n):
            sum = 0
            s = 0
            while (s <= row - 1):
                sum = sum + (L[row][s] * U[s][column])
                s = s + 1
            U[row][column] = A[row][column] - sum

        # calc value for lower matrix column vise
        for column in range(row + 1, n):
            sum = 0
            s = 0
            while (s <= row - 1):
                sum = sum + (L[column][s] * U[s][row])
                s = s + 1
            if U[row][row] == 0.0:
                raise ZeroDivisionError("Zero encountered at the matrix A diagonal.")
            else:
                L[column][row] = (A[column][row] - sum) / U[row][row]
    return L, U

def calcY(L, B):
    n = len(B)
    B = B.astype(np.float64)
    Y = np.zeros((n), dtype=np.float64)
    Y[0]=B[0]
    for row in range(0, n):
        sum = 0
        column = 0
        while (column <= row - 1):
            sum = sum + (L[row][column] * Y[column])
            column = column + 1
        Y[row] = B[row] - sum

    return Y

def calcX(Y, U):
    n = len(Y)
    Y = Y.astype(np.float64)
    X = np.zeros((n), dtype=np.float64)

    # last row of x
    # makes last x a 1 to get calc
    row=n-1
    # setting last x
    X[row] = Y[n-1] / U[row][row]
    # ignore last row
    row-=1

    # runs in reverse order lol
    while(row>=0):
        sum = 0
        column = n-1
        while (column >=0):
            sum = sum + (U[row][column] * X[column])
            column = column -1
        if U[row][row] == 0.0:
            raise ZeroDivisionError("Zero encountered at the matrix A diagonal.")
        else:
            X[row] = (Y[row] -sum)/ U[row][row]
        row-=1

    return X

A = np.array([[5, 6, 2.3, 6],
              [9, 2, 3.5, 7],
              [3.5, 6, 2, 3],
              [1.5, 2, 1.5, 6]
              ])  # define B
B = np.array([4, 5, 6.7, 7.8])




if __name__ == '__main__':
    n = len(A)
    L, U = Doolittle(A,n)
    print("Matrix L: \n{} \nMatrix U: \n{}\n".format(L, U))

    Y= calcY(L,B)
    print("Matrix Y: \n{}\n".format(Y))
    X = calcX(Y,U)
    print("Matrix X: \n{}\n".format(X))


