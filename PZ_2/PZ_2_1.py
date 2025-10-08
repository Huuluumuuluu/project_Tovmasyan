def find_day_of_week(K):

    first_day = 4

    day_of_week = (first_day + (K - 1)) % 7

    return day_of_week


def day_name(day_number):

    days = {
        0: "Воскресенье",
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота"
    }
    return days[day_number]

try:
    K = int(input("Введите номер дня года K (1-365): "))

    if 1 <= K <= 365:
        day_number = find_day_of_week(K)
        day_week_name = day_name(day_number)

        print(f"{K}-й день года - это {day_week_name} (номер дня недели: {day_number})")
    else:
        print("Ошибка: K должен быть в диапазоне 1-365")

except ValueError:
    print("Ошибка: введите целое число")