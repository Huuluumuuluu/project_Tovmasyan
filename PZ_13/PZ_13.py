# Вариант 30. Из исходного текстового файла (radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio домен выделен полужирным).

import re

# Открываем и читаем исходный файл
with open('radio_stations.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Регулярное выражение для поиска домена в URL
# Ищем протокол http:// или https://, затем захватываем домен (буквы, цифры, точки, дефисы)
# до двоеточия (порт) или до первого слеша
pattern = r'https?://([a-zA-Z0-9.-]+)'

# Находим все совпадения
domains = re.findall(pattern, content)

# Выводим результат
print("Найденные домены:")
for domain in domains:
    print(domain)

print(f"\nВсего найдено доменов: {len(domains)}")
