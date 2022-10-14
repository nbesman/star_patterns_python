def square_and_diagonals(size):
    row = 0
    col = 0 
    for row in range(size): 
        for col in range(size): 
            if (row == 0) or (row == size-1) or (col == size-1) or (col == 0) or (row == col) or (row + col == size-1):
                print("*", end=" ") 
            else: 
                print(" ", end=' ')
        print("")
    

size =9
square_and_diagonals(size)