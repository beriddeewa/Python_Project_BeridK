# Дан список размера N. Найти номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random   
n = int(input())

l = []

for i in range(n):
    l.append(random.randint(1, 50))
print(l)

for i in range(len(l) - 2, 0, -1):
    if l[i -1] < l[i] > l[i + 1]:
        print(i + 1)
        break

