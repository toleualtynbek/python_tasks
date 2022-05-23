my_string = input("Введите строку из нескольких слов: ").split()
for i, j in enumerate(my_string, 1):
    print(f'{i} - {j[:10]}')
