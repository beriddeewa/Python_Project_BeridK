# Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных) букв латинского алфавита.

n = int(input("Введите число N: "))

start_code = ord('A')

for i in range(n):
    letter = chr(start_code + i)
    print(letter, end="")
