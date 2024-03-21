'''Michael Jolley and Dilpreet Gill - Lab 03 - 4.4.1 and 4.4.2'''

def presentMatrixOptions():
    # 4.4.1 Menu Creation
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Multiply matrices by a scalar")

    selection = int(input("Enter your selection: "))

def getDimensions():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    return rows, columns

def getMatrix(dimensions):
    rows, columns = dimensions
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(int(input("Enter a number: ")))
    return matrix

def validateMatrices(mat1, mat2, operation):
    if operation == 'add' or operation == 'subtract':
        return len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])
    elif operation == 'multiply':
        return len(mat1[0]) == len(mat2)
    else:
        return False
