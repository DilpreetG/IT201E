'''Michael Jolley and Dilpreet Gill - Lab 03 - Functions'''

def presentMatrixOptions():
    # 4.4.1 Menu Creation
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Multiply matrices by a scalar")

    selection = int(input("Enter your selection: "))

def matrixInput():
    # 4.4.2 Matrix Input
    matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(int(input("Enter a number: ")))
