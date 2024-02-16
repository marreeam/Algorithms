# Those days, many boys use beautiful girls' photos as avatars in forums.
# So it is pretty hard to tell the gender of a user at the first glance. 
# Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). 
# After that they talked very often and eventually they became a couple in the network.

# But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man!
# Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

# This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female.
# You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.





users_name = input("Please, input users name: ")


len_of_users_name = len(users_name)

# Initialize a list to store unique characters in the user's name
different_characters = []

# Add the first character of the user's name to the list of different characters
different_characters.append(users_name[0])

# Define a function to determine if the number of different characters is even or odd
def even_or_odd():
    if len(different_characters) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

# Define a function to determine if the user is a girl or a boy based on the uniqueness of characters
def girl_or_boy():
    k = 1
    
    # Iterate over the characters in the user's name starting from the second character
    for i in range(len_of_users_name - 1):
        # Check if the character is not already in the list of different characters
        if users_name[k] not in different_characters:
            # If the character is not in the list, add it to the list
            different_characters.append(users_name[k])
        # Increment the index to move to the next character in the user's name
        k = k + 1
    
    # Call the even_or_odd function to determine whether to chat with her or ignore him
    print(even_or_odd())


girl_or_boy()


