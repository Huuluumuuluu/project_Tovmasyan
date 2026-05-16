#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Индекс первого минимально элемента первого файла:
#Индекс последнего максимального элемента второго файла:
#Элементы кратные 4 первого и второго файлов:

# Данные для первого файла
file1_data = [15, -3, 8, -12, 4, -7, 20, -5, 16, -1]

#данные для второго файла
file2_data = [-9, 6, -14, 10, 4, -8, 12, -2, 24, -11, 18, -6]

#Создаём и заполняем первый файл
f1 = open('file1.txt', 'w', encoding='utf-8')
for num in file1_data:
    f1.write(str(num) + ' ')
f1.close()

# Создаём и заполняем второй файл
f2 = open('file2.txt', 'w', encoding='utf-8')
for num in file2_data:
    f2.write(str(num) + ' ')
f2.close()

print("Файлы file1.txt и file2.txt созданы")
print()

# Читаю числа из первого файла
f1 = open('file1.txt', 'r', encoding='utf-8')
content1 = f1.read()
f1.close()
nums1 = []
for x in content1.split():
    if x:
        nums1.append(int(x))

# Читаю числа из второго файла
f2 = open('file2.txt', 'r', encoding='utf-8')
content2 = f2.read()
f2.close()
nums2 = []
for x in content2.split():
    if x:
        nums2.append(int(x))

#Колво элементов
count1 = len(nums1)
count2 = len(nums2)

# индекс первого минимального элемента первого файла
min1 = nums1[0]
index_min1 = 0
for i in range(len(nums1)):
    if nums1[i] < min1:
        min1 = nums1[i]
        index_min1 = i

# Индекс последнего максимального элемента второго файла
max2 = nums2[0]
for i in range(len(nums2)):
    if nums2[i] > max2:
        max2 = nums2[i]

index_max2 = 0
for i in range(len(nums2) - 1, -1, -1):
    if nums2[i] == max2:
        index_max2 = i
        break

# Элементы кратные 4 первого файла
multiples4_1 = []
for x in nums1:
    if x % 4 == 0:
        multiples4_1.append(x)

# Элементы кратные 4 второго файла
multiples4_2 = []
for x in nums2:
    if x % 4 == 0:
        multiples4_2.append(x)

# Формируем результирующий файл result.txt
result = open('result.txt', 'w', encoding='utf-8')

result.write("Элементы первого и второго файлов:\n")
result.write("первый файл: " + str(nums1) + "\n")
result.write("второй файл: " + str(nums2) + "\n\n")

result.write("Колво элементов первого и второго файлов:\n")
result.write("Колво элементов в первом файле: " + str(count1) + "\n")
result.write("Колво элементов во втором файле: " + str(count2) + "\n\n")

result.write("Индекс первого минимального элемента первого файла:\n")
result.write(str(index_min1) + " (значение: " + str(min1) + ")\n\n")

result.write("Индекс последнего максимального элемента второго файла:\n")
result.write(str(index_max2) + " (значение: " + str(max2) + ")\n\n")

result.write("Элементы кратные 4 первого и второго файлов:\n")
result.write("Первый файл: " + str(multiples4_1) + "\n")
result.write("Второй файл: " + str(multiples4_2) + "\n")

result.close()

print("Результирующий файл result.txt создан")
print("Содержимое result.txt")
f = open('result.txt', 'r', encoding='utf-8')
print(f.read())
f.close()