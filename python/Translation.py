# The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: 
# a berlandish word differs from a birlandish word with the same meaning a little: it is spelled (and pronounced) reversely.
#  For example, a Berlandish word code corresponds to a Birlandish word edoc. However, it's easy to make a mistake during the «translation».
# Vasya translated word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

first_word= input()
second_word=input()
def if_translate_correctly():
    reversed=first_word[::-1]
    if second_word==reversed:
        return "YES"
    else:
        return "NO"
print(if_translate_correctly())

