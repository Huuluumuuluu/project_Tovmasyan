# Задача 2: вычисление среднего возраста
# Создаём словарь с 6 персонами (имя: возраст)
persons = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Елена": 25,
    "Ольга": 41,
    "Дмитрий": 37
}

print("Исходный словарь (имя: возраст):")
for name, age in persons.items():
    print(f"{name}: {age}")

# Вычисляем средний возраст
try:
    total_age = sum(persons.values())
    count = len(persons)
    average_age = total_age / count
    print(f"\nСумма возрастов: {total_age}")
    print(f"Количество персон: {count}")
    print(f"Средний возраст: {average_age:.2f}")
except ZeroDivisionError:
    print("Словарь пуст, невозможно вычислить среднее.")
