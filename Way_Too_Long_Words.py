# Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

# Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special 
# abbreviation.

# This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of 
# letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

# Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

# You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be
#  replaced by the abbreviation and the words that are not too long should not undergo any changes.






def Way_Too_Long_Words():
    your_word = input("Input your word here: ")
    
    # Initialize an empty string to store the modified word
    new_word = ""
    
    # Check if the length of the input word is greater than 10
    if len(your_word) > 10:
        # If the word is too long, modify it
        # Take the first character of the word
        # Append the length of the word minus 2 (excluding first and last characters)
        # Take the last character of the word
        new_word = your_word[0] + str(len(your_word) - 2) + your_word[-1]
        

        print(new_word)
    else:
        # If the word is not too long, keep it unchanged
        new_word = your_word
        
        # Print the original word
        print(new_word)

# Call the function to execute it
Way_Too_Long_Words()

