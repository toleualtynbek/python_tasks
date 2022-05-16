number = float(input("Сколько километров пробежал в первый день: "))
target = float(input("Сколько должен пробежать: "))
i = 1;
while number <= target:
    print(i, "- й день: ", number)
    number = number + number*0.1;
    i = i + 1;
print("На ",i, "- й день спортсмен достиг результата: ",number, "км.")

