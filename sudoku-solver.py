#Uses pandas dataframe for neatness and ease of checking validity
import pandas as pd
#Time - record time it takes to find the solution
import time


#Returns true if the placement is valid, meaning
#	there are no similar values in row, col and grid.
#	If a similar value is already in place, return false
def check_valid(df,row,col,i):
	#Check row
	if((df.loc[row] == i).any()):
		#print('row')
		return False
	if((df[col] == i).any()):
		#print('col')
		return False
	grid_col = int(col/3) * 3
	grid_row = int(row/3) * 3
	if((df.loc[grid_row:grid_row+2,grid_col:grid_col+2] == i).any().any()):
		#print('grid')
		return False
	return True

#Returns the next empty grid in the puzzle
#	If there are no empty grid, return [-1,-1]
def search_empty(df):
	for row in range(0,df.shape[0]):
		for col in range(0,df.shape[0]):
			if(df.loc[row,col] == 0):
				return [row,col]
	return [-1,-1]

#Backtracking using recursion
#	A valid value is assigned on an empty grid
#	If no valid value can be assigned, return false
# 	to trigger backtracking.
def solve(df):
	#Look for the first empty grid, starting from the 
	#top left.
	empty_grid = search_empty(df)
	
	#If no empty grid was found, return True to continue
	if(empty_grid == [-1,-1]):
		return True

	#Solve the empty grid found
	row = empty_grid[0]
	col = empty_grid[1]

	#Check for a valid value for the empty grid
	for i in range(1,df.shape[0] + 1):
		#Check the row, column and box rule
		if(check_valid(df,row,col,i)):
			#If the assignment is valid, place the value
			df.loc[row,col] = i
			#Move on to the next empty grid
			if(solve(df)):
				return True
			#If a dead end was reach, meaning no possible values
			#can be placed, return to the inital empty grid and 
			#increment the assigned value
			df.loc[row,col] = 0

	return False

#---------------------------------------------------------------#
#Puzzle to be solved
puzzle = [[0, 0, 6, 0, 0, 0, 5, 0, 8],
		  [1, 0, 2, 3, 8, 0, 0, 0, 4],
		  [0, 0, 0, 2, 0, 0, 1, 9, 0],
		  [0, 0, 0, 0, 6, 3, 0, 4, 5],
		  [0, 6, 3, 4, 0, 5, 8, 7, 0],
		  [5, 4, 0, 9, 2, 0, 0, 0, 0],
		  [0, 8, 7, 0, 0, 4, 0, 0, 0],
		  [2, 0, 0, 0, 9, 8, 4, 0, 7],
		  [4, 0, 9, 0, 0, 0, 3, 0, 0]]

#Convert array to dataframe
df = pd.DataFrame(puzzle)

start = time.clock()
if(solve(df)):
	print(df)
else:
	print("No solution")
end = time.clock()
print(end - start)

