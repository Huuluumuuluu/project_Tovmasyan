# Задача 2 (Вариант 30): найти номер числа, отличного от остальных трёх равных

def find_unique_index(numbers):
    """Возвращает индекс (начиная с 1) числа, отличающегося от остальных."""
    for i in range(4):
        if numbers.count(numbers[i]) == 1:
            return i + 1
    return -1  # на случай, если условия задачи не соблюдены


def main_task2():
    print("=== Поиск числа, отличного от трёх равных ===")
    nums = []
    for i in range(1, 5):
        while True:
            try:
                value = int(input(f"Введите {i}-е целое число: "))
                nums.append(value)
                break
            except ValueError:
                print("Ошибка: введите целое число!")

    pos = find_unique_index(nums)
    if pos != -1:
        print(f"Число, отличное от остальных, находится на позиции {pos}")
    else:
        print("Ошибка: условие 'одно число отлично от трёх равных' не выполнено.")


if __name__ == "__main__":
    main_task2()
