# Даны средние значения температур за каждый месяц в году.
# Найти минимальное и максимальное значения температур за год.
# Вывести значения температур по временам года.

def get_stat(temps):
    """Возвращает мин, макс и температуры по сезонам."""
    min_t = min(temps)
    max_t = max(temps)
    seasons = {
        "Зима": [temps[i] for i in (11,0,1)],
        "Весна": [temps[i] for i in (2,3,4)],
        "Лето": [temps[i] for i in (5,6,7)],
        "Осень": [temps[i] for i in (8,9,10)]
    }
    return min_t, max_t, seasons

def main_task1():
    monthly_temps = [-5, -3, 2, 10, 15, 20, 22, 21, 16, 8, 1, -2]
    print("Исходные температуры (янв-дек):", monthly_temps)
    mn, mx, seasons = get_stat(monthly_temps)
    print(f"Мин: {mn}, Макс: {mx}")
    for season, temps in seasons.items():
        print(f"{season}: {temps}")

if __name__ == "__main__":
    main_task1()
