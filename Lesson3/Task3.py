def my_func(arg_1, arg_2, arg_3):
        a = max(arg_1, arg_2)
        b = min(arg_1, arg_2)
        c = max(b, arg_3)
        return a + c
print(my_func(5,7,4))