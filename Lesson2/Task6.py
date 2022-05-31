goods_number = int(input("Введите количество видов товара: "))
goods = []
for i in range(goods_number):
    goods_name = input(f"Введите название товара №{i+1}: ")
    goods_price = int(input("Введите цену товара: "))
    goods_quantity = int(input("Введите количество товара: "))
    goods_unit = input("Введите единицу измерения: ")
    goods.append((i+1, {"Название": goods_name, "Цена": goods_price, "Количество": goods_quantity, "Единица измерение": goods_unit}))
print(goods)
goods_dict = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерение': []}
for good in goods:
    goods_dict['Название'].append(good[1]['Название'])
    goods_dict['Цена'].append(good[1]['Цена'])
    goods_dict['Количество'].append(good[1]['Количество'])
    goods_dict['Единица измерение'].append(good[1]['Единица измерение'])
print('*********')
print(goods_dict)