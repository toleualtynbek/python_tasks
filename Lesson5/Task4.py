
s = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_str = str()
with open('text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4_1.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            line = line.split()
            for item in s.items():
                if line[0] == item[0]:
                    line[0] = item[1]
                    my_str = " ".join(line)
                    f2.writelines(my_str + '\n')
