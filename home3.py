import random

number_of_stones=random.randint(1,10)
the_color_of_the_stones= ["R","G","B"]
the_row_of_colors=[]

def random_color_wheel():

    for i in range(number_of_stones):
        k=random.randint(0,2)
        the_row_of_colors.append(the_color_of_the_stones[k])
    print(the_row_of_colors)
random_color_wheel()

def have_different_color():
    index_of_the_numbers=0
    number=0
    for c in range(number_of_stones-1):
        if the_row_of_colors[index_of_the_numbers]==the_row_of_colors[index_of_the_numbers+1]:
            number=number+1
            the_row_of_colors.pop(index_of_the_numbers+1)
            
        else:
            index_of_the_numbers=index_of_the_numbers+1
    print(number)
have_different_color()


