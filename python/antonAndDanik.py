

def whowon():
    number_of_games= int(input())
    string_of_winners=input()
    A=[]
    D=[]
    for i in range(number_of_games):
        if string_of_winners[i]=="A":
            A.append(i)
        if string_of_winners[i]=="D":
            D.append(i)
    if len(A)>len(D):
        return "Anton"
    if len(D)>len(A):
        return "Danik"
    if len(D)==len(A):
        return "Friendship"
print(whowon())