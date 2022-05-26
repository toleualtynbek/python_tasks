def summ_numbers():
    s = 0
    my_list = input("введите числа: ").split()
    for i in my_list:
        if i == 'Q':
            return s, True
        try:
            s += int(i)
        except ValueError:
            pass
    return s, False


result = 0
while True:
    a, b = summ_numbers()
    result += a
    print(result)
    if b:
        break