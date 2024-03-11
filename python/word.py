word=input()
upper_words=0
not_upper=0
for i in word:
    if i.isupper():
      
        upper_words+=1
        
    if i.islower():
      
        not_upper+=1


if upper_words>not_upper:
    word=word.upper()
if upper_words<=not_upper:
    word=word.lower()
print(word)

