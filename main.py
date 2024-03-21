'''Michael Jolley and Dilpreet Gill - Lab 03 - 4.4.1 and 4.4.2'''

def presentMatrixOptions():
    """
    Presents user to choose mode of operation for the matrix.

    Parameters:

    Returns:
    selection (int): User's selected choice for the mode of operation for the matrix.
    """
    # 4.4.1 Menu Creation
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Multiply matrices by a scalar")

    selection = int(input("Enter your selection: "))
    return selection

def getDimensions():
    """
    Generates dimensions for a matrix.

    Parameters:

    Returns:
    rows (int): Dimensions of the rows of the matrix.
    columns (int): Dimensions of the columns of the matrix.
    """
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    return rows, columns

def getMatrix(rows, columns):
    """
    Creates a matrix with numbers provided by the user.

    Parameters:
    rows (int): Dimensions of the rows of the matrix.
    columns (int): Dimensions of the columns of the matrix.

    Returns:
    Matrix (list): Matrix
    """
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(int(input("Enter a number: ")))
    return matrix

def validateMatrices(mat1, mat2, operation):
    """
    Determines if, given mode of operation, if it is possible between matricies.

    Parameters:
    mat1 (smth)
    mat2 (smth)
    operation (smth)

    Returns:
    bool (idk its true or false)
    """
    if operation == 'add' or operation == 'subtract':
        return len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])
    elif operation == 'multiply':
        return len(mat1[0]) == len(mat2)
    else:
        return False
