# Square

my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# list sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_list = sorted(a, key=lambda x: x[1])

print(sorted_list)
