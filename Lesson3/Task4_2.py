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
        i = 0
        result = 1
        for i in range(abs(y)):
            result /= x
        return result

print(my_func(5, -4))