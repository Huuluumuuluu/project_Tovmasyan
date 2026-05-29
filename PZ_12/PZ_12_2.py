import random

def print_matrix(matrix, title="Матрица"):
    """Выводит матрицу в консоль."""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))

def input_positive_int(prompt):
    """Ввод положительного целого числа с обработкой ошибок."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Ошибка: введите число больше 0.")
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    print("=" * 50)
    print("ЗАДАНИЕ 2 (Вариант 30): увеличить элементы вне главной диагонали в 2 раза")
    print("=" * 50)

    n = input_positive_int("Введите размер квадратной матрицы (n x n): ")

    # Генерация квадратной матрицы случайными числами от 0 до 20
    matrix = [[random.randint(0, 20) for _ in range(n)] for _ in range(n)]
    print_matrix(matrix, "Исходная квадратная матрица")

    # Элементы не на главной диагонали умножаем на 2
    result = [
        [matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(n)]
        for i in range(n)
    ]
    print_matrix(result, "Результат (вне главной диагонали ×2)")

if __name__ == "__main__":
    main()
