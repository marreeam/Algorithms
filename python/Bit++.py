def bit():
    number_of_statements=int(input())
    count=0
    for i in range(number_of_statements):
    
        string=str(input())
        
        if "++" in string:
            count+=1
        if "--" in string:
            count+=-1
    return count
print(bit())



    
