import random



def weights():
    years=0
    bobs_weight=random.randint(1,10)
    print(bobs_weight)
    Limaks_weight=random.randint(1,bobs_weight)
    print(Limaks_weight)
    while Limaks_weight<bobs_weight:
            Limaks_weight=Limaks_weight*3
            bobs_weight=bobs_weight*2
            years=years+1

    print(years)
weights()
