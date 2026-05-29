# Даны средние значения температур за каждый месяц в году.
# Найти минимальное и максимальное значения температур за год.
# Вывести значения температур по временам года.
import unittest
from task1_solution import get_min_max_temps, get_season_temperatures

class TestTemperatureAnalysis(unittest.TestCase):
    """Тесты для первой задачи (анализ среднемесячных температур)"""
    
    def setUp(self):
        # Исходные данные (среднемесячные температуры)
        self.monthly_temps = [-5, -3, 2, 10, 15, 20, 22, 21, 16, 8, 1, -2]
    
    def test_min_temperature(self):
        """Проверка нахождения минимальной температуры"""
        min_temp, _ = get_min_max_temps(self.monthly_temps)
        self.assertEqual(min_temp, -5, "Минимальная температура должна быть -5°C")
    
    def test_max_temperature(self):
        """Проверка нахождения максимальной температуры"""
        _, max_temp = get_min_max_temps(self.monthly_temps)
        self.assertEqual(max_temp, 22, "Максимальная температура должна быть 22°C")
    
    def test_seasons_correctness(self):
        """Проверка распределения температур по временам года"""
        season_temps = get_season_temperatures(self.monthly_temps)
        
        # Ожидаемые результаты
        expected = {
            "Зима": [-2, -5, -3],   # декабрь, январь, февраль
            "Весна": [2, 10, 15],
            "Лето": [20, 22, 21],
            "Осень": [16, 8, 1]
        }
        
        for season in expected:
            with self.subTest(season=season):
                self.assertEqual(season_temps[season], expected[season],
                                 f"Неверные температуры для сезона {season}")
    
    def test_empty_list(self):
        """Проверка поведения при пустом списке (должен быть None или исключение)"""
        with self.assertRaises(ValueError):
            get_min_max_temps([])
    
    def test_season_indices(self):
        """Проверка, что в каждом сезоне ровно 3 месяца"""
        season_temps = get_season_temperatures(self.monthly_temps)
        for season, temps in season_temps.items():
            self.assertEqual(len(temps), 3, f"В сезоне {season} должно быть 3 значения")

if __name__ == "__main__":
    unittest.main()
