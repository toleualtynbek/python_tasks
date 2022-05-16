revenue = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

profit = float(revenue - costs);
if profit>0:
    print("Фирма отработала с прибылью")
    k = profit/revenue;
    print("Рентабельность фирмы: ",k)
    employees = int(input("Введите количество отрудников: "))
    result = profit/employees;
    print("Прибыль фирмы в расчёте на одного сотрудника: ", result)
else:
    print("Фирма отработала с убыткой")
