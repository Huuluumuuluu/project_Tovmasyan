# Составить генератор (yield), который преобразует все буквенные символы
# в заглавные (остальные символы оставляет без изменения).

def uppercase_gen(text):
    """Генератор, возвращающий каждый символ в верхнем регистре."""
    for ch in text:
        yield ch.upper()

def convert(text):
    """Преобразует строку через генератор."""
    return ''.join(uppercase_gen(text))

def main_task2():
    sample = "Hello, World! 123 Привет, мир."
    print("Исходная строка:", sample)
    print("Результат:", convert(sample))

if __name__ == "__main__":
    main_task2()
