import json

# Считывание JSON-структуры из файла broke.json
with open('broke.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Запись данных без изменений в файл good.json
with open('good.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
