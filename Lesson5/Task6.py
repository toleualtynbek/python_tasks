
my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lesson_count = []
        lessons = ([i for i in line.split(" ")])
        for i in lessons:
            lesson_count.append("".join(i for i in list(i) if i.isdigit()))
            my_dict[line.split(":")[0]] = sum([int(i) for i in lesson_count if i.isdigit()])
print(my_dict)