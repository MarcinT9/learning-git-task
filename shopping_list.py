print('Lista zakupów')

shopping_list = {
    'piekarnia': ['bułka', 'chleb', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'ziemniaki']
}
for shop, product in shopping_list.items():
    print(f'Idę do {shop.capitalize()} i kupuję tam {product}')


element = shopping_list['piekarnia'] + shopping_list['warzywniak']

print(f'W sumie kupuję {len(element)} produktów.')

print('Na potrzeby zadania pierwsza zmiana')

print('Na potrzeby zadania druga zmiana')

print('Na potrzeby zadania trzecia zmiana')

print('Nowy branch - Będzie Pan zadowolony')