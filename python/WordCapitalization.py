# Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

# Note, that during capitalization all the letters except the first one remains unchanged.

def word_capitalization():    
    word = input()
    if word[0].islower():
        word = word[0].upper() + word[1:]  
        print(word)
    else:
        print(word)
word_capitalization()
 