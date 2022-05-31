import random
#my_list =[1, 2, 3, 4, 4, 5, 6, 7, 7, 9]
my_list = [random.randint(-10, 10) for _ in range(20)]
unique_number = set()
repeat_number = set()
for number in my_list:
    if number in repeat_number:
        continue
    if number in unique_number:
        repeat_number.add(number)
        unique_number.discard(number)
        continue
    unique_number.add(number)
print(unique_number)