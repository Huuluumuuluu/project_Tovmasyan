#(номер 6) задание 2
N = int(input("\nВведите размер списка N: "))
A = []

for i in range(N):
    num = int(input(f"Введите элемент A[{i+1}]: "))
    A.append(num)

print("Список A:", A)

B = []
current_sum = 0
for i in range(N):
    current_sum += A[i]
    B.append(current_sum)

print("Список B (накопленные суммы):", B)
