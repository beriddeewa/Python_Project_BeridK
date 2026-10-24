# Ввести двухзначное число. 
# Если сумма цифр числа четная, то увеличить число на 2, в противном случае уменьшить на 2

while True:
    n = input('Введите двухзначное число: ')
    try:
        chislo = int(n)
        
        if 10 <= chislo <= 99:
            break
        else:
            print('Число должно быть строго двухзначным!')
            
    except ValueError:
        print('Неправильно ввели число! Пожалуйста, используйте цифры.')
        
sum = (chislo // 10) + (chislo % 10)

if sum % 2 == 0:
    chislo = chislo + 2
else:
    chislo = chislo - 2
    
print(chislo)


