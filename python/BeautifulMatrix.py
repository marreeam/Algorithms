# Taking input for each row and creating the matrix
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

matrix = [row1, row2, row3, row4, row5]

# Initializing variables
index = None
steps = 0

# Iterating through the matrix to find the index of 1
for i in range(len(matrix)):
    if 1 in matrix[i]:
        row_index = i
        col_index = matrix[i].index(1)
        index = (row_index, col_index)
        break  # Exit the loop after finding the index

# Calculating steps to reach the center (2, 2)
if index is not None:
    steps = abs(2 - index[0]) + abs(2 - index[1])

print(steps)

