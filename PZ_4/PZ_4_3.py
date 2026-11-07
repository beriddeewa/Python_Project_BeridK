# Ввести 4 числа
# Найти и вывести на экран сумму и количество отрицательных чисел
sum = 0
kol = 0
i = 0  

while i < 4:  
    num = float(input('Введите число: '))
    if num < 0:
        kol = kol + 1
        sum = sum + num
    
    i = i + 1  

print(f'Количество: {kol}')
print(f'Сумма: {sum}')
