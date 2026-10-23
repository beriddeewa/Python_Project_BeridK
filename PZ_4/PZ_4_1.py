# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

price = input('Введите цену за 1 кг конфет: ')

while type(price) != int:
    try:
        price = int(price)
    except ValueError:
            print('Неправильно ввели число!')
            price = input('Введите цену за 1 кг конфет: ')

for i in range(1, 11):
     m = i / 10
     cost = m * price
     
     print(f'Стоимость {m:.1f} кг конфет: {cost:.2f} руб.')