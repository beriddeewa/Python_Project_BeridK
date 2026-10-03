# Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км.
# Определить расстояние между ними через T часов, если автомобили удаляются друг от друга.
# Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями; общий путь = время * суммарная скорость.


while True:
    try:
        v1  = float(input('V1='))
        break
    except ValueError:
        print('Неправильно ввели! Нужно число.')

while True:
    try:
        v2  = float(input('V2='))
        break
    except ValueError:
        print('Неправильно ввели! Нужно число.')

while True:
    try:
        s1 = float(input('S начальное='))
        break
    except ValueError:
        print('Неправильно ввели! Нужно число.')

while True:
    try:
        t = float(input('T='))
        break
    except ValueError:
        print('Неправильно ввели! Нужно число.')


print(f'Расстояние между автобилями за {t} часа: {s1 + (t * (v1+v2))}')