# A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 
# 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

# He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?






import random
number_of_bananas_he_wants=random.randint(1,10)
print(f"number of bananas he want: {number_of_bananas_he_wants} ")

money_he_has=random.randint(1,30)
print(f"he have: {money_he_has} dolars")
banana_cost=random.randint(1,5)
print(f"banana cost: {banana_cost} dolars")

full_cost1=0

# Function to calculate the total cost of buying all the bananas.

def total_cost_of_bananas():
    full_cost=0
    
    for i in range(1,number_of_bananas_he_wants+1):
        full_cost+=i*banana_cost
        full_cost1=full_cost
        
       
    print(f"full cost : {full_cost1}")
    return full_cost1

total_cost = total_cost_of_bananas()


# Function to calculate the amount of money the person needs to borrow.
def money_he_needs_to_borrow():
    
    money_he_needs=total_cost- money_he_has
    
    if money_he_needs<=0:
        print("he does not need money")
    else:
        print(f"he needs to borrow: {money_he_needs} dolars ")

    
money_he_needs_to_borrow()


