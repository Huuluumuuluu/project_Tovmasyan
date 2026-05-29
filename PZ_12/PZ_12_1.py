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
    print("ЗАДАНИЕ 1 (Вариант 30): элементы >10 заменить на 0")
    print("=" * 50)

    rows = input_positive_int("Введите количество строк: ")
    cols = input_positive_int("Введите количество столбцов: ")

    # Генерация матрицы случайными числами от 0 до 20
    matrix = [[random.randint(0, 20) for _ in range(cols)] for _ in range(rows)]
    print_matrix(matrix, "Исходная матрица")

    # Замена элементов >10 на 0 (списковое включение)
    result = [[0 if val > 10 else val for val in row] for row in matrix]
    print_matrix(result, "Результат (элементы >10 заменены на 0)")

if __name__ == "__main__":
    main()
