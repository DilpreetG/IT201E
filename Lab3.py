'''Michael Jolley and Dilpreet Gill - Lab 03 - Main Program'''

import numpy as np
from matrixMathFunction import matrixAddition, matrixSubtraction, matrixMultiplication, scalarMultiplication
from main import presentMatrixOptions, getDimensions, getMatrix, validateMatrices

# Present the user with the menu of options
while True:
    selection = presentMatrixOptions()

    if selection == 1:
        # Get the dimensions of the first matrix
        print("First enter the dimensions of the first matrix\n")
        rows, columns = getDimensions()

        print()

        print("Enter the values of the first matrix\n")
        # Get the first matrix
        matrix1 = getMatrix((rows, columns))

        print()

        print("Now enter the dimensions of the second matrix\n")
        # Get the dimensions of the second matrix
        rows2, columns2 = getDimensions()

        print()

        print("Enter the values of the second matrix\n")
        # Get the second matrix
        matrix2 = getMatrix((rows2, columns2))

        print()

        # Validate the matrices
        if validateMatrices == False:
            print("The matrices are not the same size. Please try again.")
            continue

        # Add the matrices
        result = matrixAddition(matrix1, matrix2)
        print("Matrix 1 = ", matrix1, "\nMatrix 2 = ", matrix2)
        print("Matrix 1 + Matrix 2 = ", result)

    elif selection == 2:
        # Get the dimensions of the first matrix
        print("First enter the dimensions of the first matrix\n")
        rows, columns = getDimensions()

        print()

        print("Enter the values of the first matrix\n")
        # Get the first matrix
        matrix1 = getMatrix((rows, columns))

        print()

        print("Now enter the dimensions of the second matrix\n")
        # Get the dimensions of the second matrix
        rows2, columns2 = getDimensions()

        print()

        print("Enter the values of the second matrix\n")
        # Get the second matrix
        matrix2 = getMatrix((rows2, columns2))

        print()

        # Validate the matrices
        if validateMatrices == False:
            print("The matrices are not the same size. Please try again.")
            continue

        # Add the matrices
        result = matrixSubtraction(matrix1, matrix2)
        print("Matrix 1 = ", matrix1, "\nMatrix 2 = ", matrix2)
        print("Matrix 1 - Matrix 2 = ", result)

    elif selection == 3:
        # Get the dimensions of the first matrix
        print("First enter the dimensions of the first matrix\n")
        rows, columns = getDimensions()

        print()

        print("Enter the values of the first matrix\n")
        # Get the first matrix
        matrix1 = getMatrix((rows, columns))

        print()

        print("Now enter the dimensions of the second matrix\n")
        # Get the dimensions of the second matrix
        rows2, columns2 = getDimensions()

        print()

        print("Enter the values of the second matrix\n")
        # Get the second matrix
        matrix2 = getMatrix((rows2, columns2))

        print()

        # Validate the matrices
        if validateMatrices == False:
            print("The matrices are not the same size. Please try again.")
            continue

        # Add the matrices
        result = matrixMultiplication(matrix1, matrix2)
        print("Matrix 1 = ", matrix1, "\nMatrix 2 = ", matrix2)
        print("Matrix 1 * Matrix 2 = ", result)

    elif selection == 4:
        # Get the dimensions of the matrix
        print("First enter the dimensions of the matrix\n")
        rows, columns = getDimensions()

        print()

        print("Enter the values of the matrix\n")
        # Get the first matrix
        matrix1 = getMatrix((rows, columns))

        print()

        # Get the scalar
        scalar = int(input("Enter the scalar: "))

        # Multiply the matrix by the scalar
        result = scalarMultiplication(matrix1, scalar)
        print(result)
