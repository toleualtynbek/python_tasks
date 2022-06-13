def my_word(text):
    return text[0].upper() + text[1:].lower()

my_text = input("Введите тексты: ").split()
for i, text in enumerate(my_text):
    if not text.isascii() or not text.isalpha() or not text.islower():
        print("Ошибка ввода")
    else:
        my_text[i] = my_word(text)
print(my_text)