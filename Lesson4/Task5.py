from random import randint
from functools import reduce

def my_func(number1, number2):
    return number1 * number2

my_numbers = [el for el in range(100, 1001, 2)]
print(reduce(my_func, my_numbers))
