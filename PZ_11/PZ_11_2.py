# Составить генератор (yield), который преобразует все буквенные символы
# в заглавные (остальные символы оставляет без изменения).
import unittest
from task2_solution import uppercase_generator

class TestUppercaseGenerator(unittest.TestCase):
    """Тесты для генератора, переводящего буквенные символы в верхний регистр"""
    
    def test_latin_letters(self):
        """Проверка преобразования латинских букв"""
        gen = uppercase_generator("Hello")
        result = ''.join(gen)
        self.assertEqual(result, "HELLO")
    
    def test_cyrillic_letters(self):
        """Проверка преобразования кириллических букв"""
        gen = uppercase_generator("привет")
        result = ''.join(gen)
        self.assertEqual(result, "ПРИВЕТ")
    
    def test_mixed_case(self):
        """Проверка смешанного регистра"""
        gen = uppercase_generator("PyThOn")
        result = ''.join(gen)
        self.assertEqual(result, "PYTHON")
    
    def test_non_letters_unchanged(self):
        """Проверка, что небуквенные символы не меняются"""
        gen = uppercase_generator("123 !@#")
        result = ''.join(gen)
        self.assertEqual(result, "123 !@#")
    
    def test_empty_string(self):
        """Проверка пустой строки"""
        gen = uppercase_generator("")
        result = ''.join(gen)
        self.assertEqual(result, "")
    
    def test_mixed_content(self):
        """Проверка строки с буквами, цифрами и знаками"""
        gen = uppercase_generator("a1B2c!d")
        result = ''.join(gen)
        self.assertEqual(result, "A1B2C!D")
    
    def test_generator_type(self):
        """Проверка, что функция возвращает именно генератор (итератор)"""
        result = uppercase_generator("test")
        # Проверяем наличие метода __next__ (признак итератора/генератора)
        self.assertTrue(hasattr(result, '__next__'), "Функция должна возвращать итератор")

if __name__ == "__main__":
    unittest.main()
