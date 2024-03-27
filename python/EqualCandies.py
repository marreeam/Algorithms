def equal_candies():
    t = int(input())

    for _ in range(t):
        number_of_boxes = int(input())
        quantities_of_candies = list(map(int, input().split()))

        smallest_number = min(quantities_of_candies)
        candies_to_eat = sum(c - smallest_number for c in quantities_of_candies)

        print(candies_to_eat)
equal_candies()
