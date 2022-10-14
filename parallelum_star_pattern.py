

def parallelum(row_size,col_size,half_size):
    row = 0
    while row < row_size:
        col = 0
        while col < col_size:
            if (col == row) or (col - row == half_size)or (1 <= col-row <= half_size-1) :# (row == row_size-1):  
                print('*', end='') 
            else:
                print(' ', end='') 
            col +=1
        print('')
        row += 1

def main():             
    row_size = 7
    col_size = row_size * 2 
    half_size = col_size //2 
    parallelum(row_size,col_size,half_size)

if __name__ == "__main__": 
    main()