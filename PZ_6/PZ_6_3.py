#(номер 6) задание 3
N = int(input("\nВведите размер списка N: "))
A = []

for i in range(N):
    num = int(input(f"Введите элемент A[{i+1}]: "))
    A.append(num)

print("Исходный список A:", A)

K = int(input(f"Введите K (1 < K < {N}): "))
while K <= 1 or K >= N:
    print(f"K должно быть между 1 и {N}")
    K = int(input(f"Введите K снова: "))

for i in range(N-1, K-1, -1):
    A[i] = A[i-K]

for i in range(K):
    A[i] = 0

print(f"Список после сдвига на {K} позиций вправо:", A)
