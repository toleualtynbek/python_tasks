
with open('text_3.txt', 'r', encoding='utf=8') as f:
    names = []
    res_income = 0
    my_num = 0
    for line in f:
        user_name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(user_name)
            res_income += income
            my_num += 1
    res_income /= my_num
print(*names)
print(my_num)