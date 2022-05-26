def f_division (arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return "Деление на 0 невозможно!"
dev_number = float(input("Ведите делимое число: "))
div_number = float(input("Введите делитель: "))
print(f'Результат деление = {f_division(dev_number, div_number)}')