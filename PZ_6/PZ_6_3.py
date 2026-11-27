# Дан список размера N. 
# Переставить в обратном порядке элементы списка,
# расположенные между его минимальным и максимальным элементами, включая минимальный и максимальный элементы.

import random   
n = int(input())

l = []

for i in range(n):
    l.append(random.randint(1, 100))
print(l)

idx1 = l.index(min(l))
idx2 = l.index(max(l))

minn = min(idx1, idx2)
maxx = max(idx1, idx2)

l[minn + 1 : maxx] = l[minn + 1 : maxx][::-1]
print(l)
