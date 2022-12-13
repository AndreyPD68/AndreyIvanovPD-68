print ('Задача 1')
cook_book = {}
with open('recipes.txt', 'tr', encoding='utf-8') as f:
    for line in f:
        dish_name = (line.strip('\n'))
        ing_number = int(f.readline())
        ingredients = []
        for i in range(ing_number):
            ingr = f.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure
                                })

        f.readline()
        cook_book.update({dish_name: ingredients})

print(cook_book)
print()

dishes = []
for k in cook_book:
    dishes.append(k)
print()
print ('Задача 2')
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        ingr = cook_book.get(i)
        for item in ingr:
            shop_list.update({item.get('ingredient_name'): {'measure': item.get('measure'),
                                                            'quantity': int(item.get('quantity')) * person_count
                                                            }})
    return (shop_list)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 100))
print()
print('Задача 3')

import os

files_res = []
for file_line in ['1.txt', '2.txt', '3.txt']:
    with open(os.path.join(os.getcwd(), file_line), 'rt', encoding='utf-8') as file:
        data = file.readlines()
        files_res .append([file_line + '\n', str(len(data)) + '\n', data])

files_res .sort(key=lambda i: i[1])

with open(os.path.join(os.getcwd(), 'result.txt'), 'wt', encoding='utf-8') as file:
    for file_line in files_res:
        file.writelines([file_line[0], file_line[1]])
        file.writelines(file_line[2])
        file.write('\n')
    print('Файл успешно создан')






