for x in range(0,20):
    print(x**2)

list1 = [x**2 for x in range(20)]

print(list1)

list1 = [x for x in range(20) if x**2 < 201]

print(list1)