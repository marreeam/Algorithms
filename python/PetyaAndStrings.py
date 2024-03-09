def lexicographic():
    first_string=input()
    second_string=input()
    first_string=first_string.lower()
    second_string=second_string.lower()
    if first_string>second_string:
        return "1"
    if first_string<second_string:
        return "-1"
    if first_string==second_string:
        return "0"
print(lexicographic())

