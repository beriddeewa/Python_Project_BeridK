# Ввести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
n = input('Введите число: ')

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Неправильно ввели число!')
        n = input('Введите число: ')

if n % 2 == 0:
    n = int(n / 4)
elif n % 2 != 0:
    n = n * 5

print(n)
