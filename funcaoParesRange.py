def evens(ranges):
    even = []
    for i in range(ranges):
        if i % 2 == 0:
            even.append(i)
    print(even)

evens(11)