def remove():
    test_cases=int(input())
    
    for i  in range(test_cases):
        length_of_sequence=int(input())
        given_elements = list(map(int, input().split()))
 
        count = 0
        for element in range(1, length_of_sequence):
            if given_elements[element] == given_elements[0]:
                index_of_repeated_element=given_elements.index(given_elements[element])
                given_elements=given_elements[index_of_repeated_element:]
                count += index_of_repeated_element+1
            else:
                continue
 
        
 
        return count
 
print(remove())