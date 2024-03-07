# An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house
# is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward.
# Determine, what is the minimum number of steps he need to make in order to get to his friend's house.






import random
# This function calculates the minimum number of steps required to reach a friend's house.
# It simulates taking steps of 5 units towards the house until the remaining distance is less than 5.
# If there's any remaining distance, an additional step is taken to cover it.
# The total number of steps is then printed as the output.

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
        
        
            
        