def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print("Введите положительное х и отрицательное у ")
        return
    if x <= 0 or y >= 0:
        print("Введите положительное действительное число х и отрицательное целое число у ")
        return
    else:
        return x**y


print(round(my_func(2, -2),10))