my_list = [7, 5, 3, 3, 2]
add_num = int(input("Введите число: "))
i = 0
for k in my_list:
    if add_num <= k:
        i = i + 1
my_list.insert(i, add_num)
print(*my_list)
