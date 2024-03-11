number, k = input().split()  
number = list(map(int, number))  
k = int(k)

for i in range(k):
    if number[-1] == 0:
       
        number.pop() 
    else:
       
        number[-1] -= 1
result = int(''.join(map(str, number)))
print(result)



