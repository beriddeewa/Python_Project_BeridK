# Дан список размера N. 
# Переставить в обратном порядке элементы списка,
# расположенные между его минимальным и максимальным элементами, включая минимальный и максимальный элементы.

N = int(input('N = '))
lst = []

for i in range(N):
    x = int(input('Введите элимент списка: '))
    lst.append(x)

i_min = lst.index(min(lst))
i_max = lst.index(max(lst))

left = min(i_min, i_max)
right = max(i_min, i_max)

lst[left : right + 1] = lst[left : right + 1][::-1]

print(lst)
