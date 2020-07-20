#-----------------------------Time complexity: O(9^(n*n))------------------------------------#
def find_empty_slot(arr,pos):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                pos[0] = i
                pos[1] = j
                return True
    return False

def isSafe(arr,row,col,num):
    return not rowCheck(arr,row,num) and not colCheck(arr,col,num) and not boxCheck(arr,row-row%3,col-col%3,num)

def rowCheck(arr,row,num):
    for i in range(9):
        if arr[row][i]==num:
            return True
    return False

def colCheck(arr,col,num):
    for i in range(9):
        if arr[i][col]==num:
            return True
    return False

def boxCheck(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col]==num:
                return True
    return False

def solve_sudoku(arr):
    pos = [0,0]
    if not find_empty_slot(arr,pos):
        return True
    row,col = pos[0],pos[1]
    for num in range(1,10):
        if isSafe(arr,row,col,num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0
    return False
    
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
    print()
