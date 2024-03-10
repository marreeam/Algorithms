sum_to_count = input()
numbers = []

for char in sum_to_count:
    if char != "+":
        numbers.append(int(char))  # Convert the character to an integer
        numbers = sorted(numbers)
        sum_to_count = '+'.join(map(str, numbers))  # Convert the sorted list to a string
    else:
        continue

print(sum_to_count)

