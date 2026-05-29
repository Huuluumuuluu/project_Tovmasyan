#Из предложенного текстового файла (text18-30.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив после последней строки автора и название
#произведения.

#Выводим содержимое файла на экран
print("Содержимое файла text18-30.txt\n")

f = open('text18-30.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

print(content)

#Подсчитываю колво знаков препинания
#Задаю множество знаков препинания
punct_marks = ('.', ',', '!', '?', ';', ':', '-', '—', '(', ')', 
                     '"', "'", '«', '»', '…')

punct_count = 0
for char in content:
    if char in punct_marks:
        punct_count = punct_count + 1

print()
print("Количество знаков препинания в файле:", punct_count)
print()

# формирую новый файл с автором и названием
# Читаю файл построчно
f = open('text18-30.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

# Создаём новый файл
new_file = open('new_file.txt', 'w', encoding='utf-8')

# Записываем все строки исходного файла
for line in lines:
    new_file.write(line)

# Добавляем автора и название после последней строки
new_file.write("\n")
new_file.write("\n")
new_file.write("М.Ю. Лермонтов\n")
new_file.write("Бородино\n")

new_file.close()

print("Новый файл new_file.txt создан")
print()
print("содержимоe new_file.txt ")

f = open('new_file.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
