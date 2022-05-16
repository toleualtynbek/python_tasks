number = int(input("Введите любое целое положительное число: "))
max = 0;
while number > 0:
    digit = number % 10;
    number = number // 10;
    if digit > max:
        max = digit;

print("Самая большая цифра: ",max)