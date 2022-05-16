
number = float(input("Введите время в секундах: "))

if number<60:
        print("вы ввели :", number," секунд")

elif number>=60 and number<360:
        m = number // 60;
        s = number % 60;
        print("вы ввели :", m, " минут")
        print("вы ввели :", s, " секунд")

else:
        h = number // 360;
        k = number % 360;
        m = k // 60;
        s = k % 60;
        print("вы ввели :", h, " часа")
        print("вы ввели :", m, " минут")
        print("вы ввели :", s, " секунд")

