import os
def task1():
    """Создание двух файлов с числами, обработка и запись результата."""
    # 1.1 Формируем два исходных файла с последовательностями чисел
    numbers1 = [-5, 12, -3, 8, -1, 7, -10, 4]
    numbers2 = [6, -2, 9, -4, 3, -8, 11, -6, 5]

    with open('numbers1.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, numbers1)))
    with open('numbers2.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, numbers2)))

    # 1.2 Чтение чисел из файлов
    try:
        with open('numbers1.txt', 'r', encoding='utf-8') as f:
            list1 = list(map(int, f.read().split()))
        with open('numbers2.txt', 'r', encoding='utf-8') as f:
            list2 = list(map(int, f.read().split()))
    except FileNotFoundError:
        print("Ошибка: файл с числами не найден.")
        return

    # 1.3 Вычисления
    # Элементы файлов
    elements1 = ' '.join(map(str, list1))
    elements2 = ' '.join(map(str, list2))

    # Количество элементов
    count1 = len(list1)
    count2 = len(list2)

    # Индекс первого минимального элемента первого файла
    if list1:
        min_val1 = min(list1)
        idx_first_min = list1.index(min_val1)
    else:
        idx_first_min = None

    # Индекс последнего максимального элемента второго файла
    if list2:
        max_val2 = max(list2)
        # Ищем последнее вхождение максимального элемента
        idx_last_max = len(list2) - 1 - list2[::-1].index(max_val2)
    else:
        idx_last_max = None

    # Элементы, кратные 4
    multiples4_1 = [x for x in list1 if x % 4 == 0]
    multiples4_2 = [x for x in list2 if x % 4 == 0]

    # 1.4 Запись результатов в новый файл
    with open('result_numbers.txt', 'w', encoding='utf-8') as out:
        out.write("Элементы первого и второго файлов:\n")
        out.write(f"Файл 1: {elements1}\n")
        out.write(f"Файл 2: {elements2}\n\n")

        out.write(f"Количество элементов первого файла: {count1}\n")
        out.write(f"Количество элементов второго файла: {count2}\n\n")

        out.write(f"Индекс первого минимального элемента первого файла: {idx_first_min}\n")
        out.write(f"Индекс последнего максимального элемента второго файла: {idx_last_max}\n\n")

        out.write("Элементы кратные 4:\n")
        out.write(f"Из первого файла: {multiples4_1}\n")
        out.write(f"Из второго файла: {multiples4_2}\n")

    print("Задача 1 выполнена. Результат в файле 'result_numbers.txt'.\n")

def task2():
    """Обработка стихотворного файла: вывод, подсчёт знаков препинания, добавление автора."""
    input_filename = "text18-30.txt"
    output_filename = "text18-30_out.txt"

    # 2.1 Проверка существования файла
    if not os.path.exists(input_filename):
        print(f"Ошибка: файл '{input_filename}' не найден.")
        return

    # 2.2 Чтение и вывод содержимого на экран
    print("Содержимое файла text18-30.txt:")
    print("-" * 40)
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
    print("\n" + "-" * 40)

    # 2.3 Подсчёт знаков препинания
    punctuation = set(".,!?;:—-\"\'()[]{}«»…")
    total_punct = 0
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()
        for ch in text:
            if ch in punctuation:
                total_punct += 1

    print(f"Количество знаков препинания в тексте: {total_punct}\n")

    # 2.4 Формирование нового файла с добавлением автора после последней строки
    author_title = "\nМихаил Лермонтов «Бородино»"
    with open(output_filename, 'w', encoding='utf-8') as out:
        out.writelines(lines)
        out.write(author_title)

    print(f"Задача 2 выполнена. Результат в файле '{output_filename}'.")

if __name__ == "__main__":
    task1()
    print("\n" + "=" * 50 + "\n")
    task2()
