# Дан список размера N. Найти номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

N = int(input('N = '))
lst = []

for i in range(N):
    x = int(input('Введите элимент списка: '))
    lst.append(x)

ans = 0  

if lst[0] > lst[1]:
    ans = 0

for i in range(1, N - 1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        ans = i

if lst[N - 1] > lst[N - 2]:
    ans = N - 1

print(ans)