# Задача 1 (Вариант 30): проверка, является ли треугольник равносторонним

def is_equilateral_triangle(a, b, c):
    """Проверяет, может ли существовать треугольник и является ли он равносторонним."""
    # Проверка существования треугольника
    if a + b > c and a + c > b and b + c > a:
        return a == b == c
    return False


def main_task1():
    print("=== Проверка равностороннего треугольника ===")
    sides = []
    names = ["первую", "вторую", "третью"]
    for i in range(3):
        while True:
            try:
                value = int(input(f"Введите {names[i]} сторону треугольника (целое число): "))
                sides.append(value)
                break
            except ValueError:
                print("Ошибка: нужно ввести целое число!")

    a, b, c = sides
    if is_equilateral_triangle(a, b, c):
        print(f"Треугольник со сторонами {a}, {b}, {c} является равносторонним.")
    else:
        print(f"Треугольник со сторонами {a}, {b}, {c} НЕ является равносторонним.")


if __name__ == "__main__":
    main_task1()
