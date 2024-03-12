row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

matrix = row1+ row2+ row3+ row4+ row5


index = None
steps=0

for i in range(len(matrix)):
     if matrix[i]==1:
        index = matrix.index(1)
       
       
        
        if index-12==10:
            steps=2
        if 12-index==5:
            steps=2
       
        else:
            steps=12-index
            if steps<0:
                steps=index-12
        

        
        




print(steps)


