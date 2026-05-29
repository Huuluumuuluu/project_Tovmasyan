
#вариант 30, (номер 6) задание 1 
N = int(input("Введите размер списка N: "))
lst = []

for i in range(N):
    num = int(input(f"Введите элемент {i+1}: "))
    lst.append(num)

print("Исходный список:", lst)

first_even = None
for num in lst:
    if num % 2 == 0:
        first_even = num
        break

if first_even is not None:
    for i in range(N):
        if lst[i] % 2 == 0:
            lst[i] += first_even

print("Результат:", lst)
