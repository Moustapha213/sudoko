k = input(" Enter Num sudoko : ")
grid =[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],]
grid = eval(k)
def checking(x , y , n):
        for i in range(9):
        	if grid[x][i] == n :
        		return False

    # Check column
        for i in range(9):
            if grid[i][y] == n :
            	return False

    # Check box
        box_x = y// 3
        box_y = x // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if grid[i][j] == n :
                    return False
        return True
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
def solve(grid):
    find = find_empty(grid)
    if not find :
    	return True
    else :
    	row , col = find    
    for i in range(1,10):
        if checking(row, col,i):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
    
def show(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
	
solve(grid)
for i in range(4):
	print()
show(grid)

