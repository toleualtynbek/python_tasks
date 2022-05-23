my_list = input("Введите числа: ").split()
i = 0
if len(my_list) % 2 == 0:
    while i < len(my_list):
        num = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = num
        i = i + 2
else:
    i = 0
    while i < len(my_list)-1:
        num = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = num
        i = i + 2
print(my_list)