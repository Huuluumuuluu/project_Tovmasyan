# Задача 1: изменение зарплаты сотрудника
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

print("Исходный словарь:")
print(sample_dict)

# Изменяем зарплату Brad на 8500
# Проверяем, существует ли сотрудник Brad, чтобы избежать ошибки
if 'emp3' in sample_dict and sample_dict['emp3']['name'] == 'Brad':
    sample_dict['emp3']['salary'] = 8500
    print("\nЗарплата Brad изменена на 8500.")
else:
    print("\nСотрудник Brad не найден.")

print("\nИзменённый словарь:")
print(sample_dict)
