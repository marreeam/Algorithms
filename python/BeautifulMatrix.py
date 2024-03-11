row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

matrix = row1+ row2+ row3+ row4+ row5

index = None
indexes_to_be_perfext=2

for i in range(len(matrix)):
    if 1 in matrix[i]:
        index = (i, matrix[i].index(1))
        row_index, col_index = index
        matrix[i] = [0] * len(matrix[i])
        
        matrix[indexes_to_be_perfext][indexes_to_be_perfext] = 1

        

print(index)
print(matrix)


