import random

def rotate_string():
    string = "Zebra-493"
    len_string = len(string)
    rotation_factor = random.randint(1, 10)
    print(rotation_factor)
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters_lowercased = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    new_string = []

    for char in string:
        if char.isupper():
            index_of_character = characters.index(char)
            new_index = (index_of_character + rotation_factor) % 26
            new_string.append(characters[new_index])
        elif char.isdigit():
            index_of_digit = digits.index(char)
            new_index = (index_of_digit + rotation_factor) % 10
            new_string.append(digits[new_index])
        elif char.islower():
            index_of_lowercase_character = characters_lowercased.index(char)
            new_index = (index_of_lowercase_character + rotation_factor) % 26
            new_string.append(characters_lowercased[new_index])
        else:
            new_string.append(char)

    rotated_string = ''.join(new_string)
    return rotated_string

rotated_string = rotate_string()
print("Rotated string:", rotated_string)







