l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
number=""
number2=""

for i in l1:
    number+=str(i)

for j in l2:
    number2+=str(j)
number_to_add=int(number[::-1])
number_to_add2=int(number2[::-1])
sum=str(number_to_add+number_to_add2)
sum2=sum[::-1]
new_list=[]
for i in range(len(sum)):
    new_list.append(int(sum2[i]))
print(new_list)

