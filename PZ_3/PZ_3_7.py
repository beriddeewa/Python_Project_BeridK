# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
a = input('Введите число А: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели число!')
        a = input('Введите число А: ')

b = input('Введите число В: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели число!')
        b = input('Введите число В: ')

x = a + b

if x % 5 == 0:
    n = x + 1
elif x % 5 != 0:
    n = x - 2

print(n)
