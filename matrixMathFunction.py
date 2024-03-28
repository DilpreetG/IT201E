
import numpy as np

'''Michael Jolley and Dilpreet Gill - Lab 03 - 4.4.3 4.4.4 4.4.5 and 4.4.6 - Math Functions'''

def matrixAddition(matrix1, matrix2):
    '''4.4.3 Adds two matrices together'''
    matrix1, matrix2 = np.array(matrix1), np.array(matrix2)
    if matrix1.shape != matrix2.shape:
        return("Matrices must be the same size to add them together")

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result

def matrixSubtraction(matrix1, matrix2):
    '''4.4.4 Subtracts two matrices'''
    matrix1, matrix2 = np.array(matrix1), np.array(matrix2)
    if matrix1.shape != matrix2.shape:
        return("Matrices must be the same size to subtract them together")

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] - matrix2[i][j])
    return result

def matrixMultiplication(matrix1, matrix2):
    '''4.4.5 Multiplies two matrices together'''
    if len(matrix1[0]) != len(matrix2):
        return("The number of columns in the first matrix must match the number of rows in the second matrix")

    result = []
    result = np.dot(matrix1, matrix2)
    return result # can also use tolist() to convert to a list if needed

def scalarMultiplication(matrix, scalar):
    '''4.4.6 Multiplies a matrix by a scalar'''
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[0])):
            result[i].append(matrix[i][j] * scalar)
    return result
