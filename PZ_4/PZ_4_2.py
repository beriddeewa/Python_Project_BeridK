# Дано целое число N (> 0). 
# Используя операции деления нацело и взятия остатка от деления, 
# найти число, полученное при прочтении числа N справа налево.

N = input('Введите число N > 0: ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
            print('Неправильно ввели число!')
            N = input('Введите число N > 0: ')

perevern_num = 0

while N > 0:
     last_num = N % 10 
     perevern_num = perevern_num*10 + last_num

     N = N // 10
 
print(f'Число справа налево: {perevern_num}')