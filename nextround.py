# "Contestant who earns a score equal to or greater than the k-th place finisher's 
# score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

# A total of n participants took part in the contest (n ≥ k), and you already know their scores.
# Calculate how many participants will advance to the next round.



def next_round():
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    list_of_participants_scores = input().split()
    for i in range(n):
        list_of_participants_scores[i] = int(list_of_participants_scores[i])
       
    participants_who_advanced = []
    for i in list_of_participants_scores:
        if i >= list_of_participants_scores[k - 1] and i > 0:
            participants_who_advanced.append(i)
            
    print(len(participants_who_advanced))

next_round()





