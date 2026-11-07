# Найти и вывести на экран сумму S = 1! + 2! + 3! + 4! + ... + (n > 1).

n = int(input('Введите число n > 1: '))

sum = 0
factorial = 1

i = 1

while i <= n:  # #1, 2, 3,
    factorial = factorial * i
    sum = sum + factorial
    i = i + 1

print(f'Сумма факториалов равна: {sum}')
