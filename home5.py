import random

def reach_house_minimum_steps():
    coordianions_of_friends_house=random.randint(1,10)
    print(coordianions_of_friends_house)
    number_of_steps=0
    
    while coordianions_of_friends_house>=5:
        coordianions_of_friends_house+=-5
        number_of_steps+=1
    if coordianions_of_friends_house==0:
        pass

    if coordianions_of_friends_house<5 and coordianions_of_friends_house>0:
        number_of_steps+=1
    print(number_of_steps)
reach_house_minimum_steps()
        
        
            
        