my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = 0
result = []
for i, j in enumerate(my_list):
    if i != 0 and j > my_list[i-1]:
        result.append(j)
    i += i

print(result)
