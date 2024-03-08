# Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

# Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.

# Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.

# After how many full years will Limak become strictly larger (strictly heavier) than Bob?




import random

# The while loop continues iterating as long as Limak's weight is less than Bob's weight.
# Limak's weight and Bob's weight are compared in each iteration to check if Limak has surpassed Bob.
# In each iteration, Limak's weight is tripled while Bob's weight is doubled.
# The loop counts the number of years it takes for Limak to become equal to or heavier than Bob.

def weights():
    Limaks_weight,bobs_weight=int(input()).split()
    years=0
   
   
    
    while Limaks_weight<bobs_weight:
            Limaks_weight=Limaks_weight*3
            bobs_weight=bobs_weight*2
            years=years+1

    print(years)
weights()
