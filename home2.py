users_name = input("Please,input users name: ")
len_of_users_name=len(users_name)
different_characters=[]
different_characters.append(users_name[0])
def even_or_odd():
    if len(different_characters)%2==0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

def girl_or_boy():
    k=1
    
    for i in range(len_of_users_name-1):
        if users_name[k] not in different_characters:
            different_characters.append(users_name[k])
            k=k+1
    print(even_or_odd())
    
girl_or_boy()

