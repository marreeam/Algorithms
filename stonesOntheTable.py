# There are n stones on the table in a row, each of them can be red, green or blue. 
# Count the minimum number of stones to take from the table so that any two neighboring stones had different colors.
# Stones in a row are considered neighboring if there are no other stones between them.

import random


number_of_stones = int(input())

the_color_of_the_stones = input()
the_row_of_colors = []

# Function to randomly select colors for the stones
def random_color_wheel():
    for i in range(number_of_stones):
        k = random.randint(0, 2)
        the_row_of_colors.append(the_color_of_the_stones[k])

    print(the_row_of_colors)
random_color_wheel()

# Function to count the number of consecutive stones with the same color
def have_different_color():
    index_of_the_numbers = 0
    number = 0
    for c in range(number_of_stones - 1):
        # Check if the color of the current stone is the same as the next stone
        if the_row_of_colors[index_of_the_numbers] == the_row_of_colors[index_of_the_numbers + 1]:
            # Increment the count if consecutive stones have the same color
            number = number + 1
            # Remove the next stone from the list to avoid counting it again
            the_row_of_colors.pop(index_of_the_numbers + 1)
        else:
            # Move to the next stone if the colors are different
            index_of_the_numbers = index_of_the_numbers + 1
 
    print(number)

have_different_color()



