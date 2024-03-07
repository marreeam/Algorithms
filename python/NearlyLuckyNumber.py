
def is_nearly_lucky():
    n = input()

    lucky_digits = 0
    for digit in n:
        if digit == '4' or digit == '7':
            lucky_digits += 1

    print("YES" if lucky_digits == 4 or lucky_digits == 7 else "NO")

is_nearly_lucky()

