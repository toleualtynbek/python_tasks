from itertools import count, cycle

for el in count(int(input("Введите стартовое число меньше 10:"))):
    print(el)
    if el > 10:
        break

j = 1
for i in cycle(input("Введите число: ")):
    print(i)
    j += 1
    if j > 10:
        break