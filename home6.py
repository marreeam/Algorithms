import random
number_of_bananas_he_wants=random.randint(1,10)
print(f"number of bananas he want: {number_of_bananas_he_wants} ")

money_he_has=random.randint(1,30)
print(f"he have: {money_he_has} dolars")
banana_cost=random.randint(1,5)
print(f"banana cost: {banana_cost} dolars")

full_cost1=0

def total_cost_of_bananas():
    full_cost=0
    
    for i in range(1,number_of_bananas_he_wants+1):
        full_cost+=i*banana_cost
        full_cost1=full_cost
        
       
    print(f"full cost : {full_cost1}")
    return full_cost1
total_cost = total_cost_of_bananas()


def money_he_needs_to_borrow():
    
    money_he_needs=total_cost- money_he_has
    
    if money_he_needs<=0:
        print("he does not need money")
    else:
        print(f"he needs to borrow: {money_he_needs} dolars ")

    
money_he_needs_to_borrow()


