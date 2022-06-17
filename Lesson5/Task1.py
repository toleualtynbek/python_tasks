
with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        my_text = input('Введите текст. Чтобы выйти нажмите Enter: ')
        if not my_text:
            break
        print(my_text, file=f)
