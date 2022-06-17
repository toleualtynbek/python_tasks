import json

result = dict()
average_prof = 0
num = 0

with open('text_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        firm_name, firm_type, income, cost = line.split()
        firm_prof = int(income) - int(cost)
        if firm_prof >= 0:
            average_prof += firm_prof
            num += 1
        result[firm_name] = firm_prof

average_prof /= num
with open('json7.json', 'w', encoding='utf-8') as f:
    json.dump([result, {"average_profit": average_prof}], f, ensure_ascii=False)