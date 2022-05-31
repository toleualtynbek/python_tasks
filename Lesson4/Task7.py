def my_factorial(number):
    result_num = 1
    if result_num == 0:
        yield 0
    for i in range(1, number + 1):
        result_num *= i
        yield f'{i}! =  {result_num}'

for el in my_factorial(int(input('Введите число: '))):
    print(el)