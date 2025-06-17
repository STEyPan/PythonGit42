# Сериализация и Десериализация данных

# Виды сериализаций:
# 1. Бинарная сериализация данных - данные собираются в некую последовательность
# структуру состоящую из чистой байтовой последовательности
# 2. Текстовая сериализация данных - XML -> JSON

import json


with open("example.json", "r", encoding="utf-8") as file:
    json_obj = json.load(file)
    print(json_obj["total"]["key_array"][0]["string"])
    json_obj["total"]["key_array"][0]["string"] = "string"

with open("example_after.json", "w", encoding="utf-8") as file:
    json.dump(json_obj, file, ensure_ascii=False, indent=4)
    print(json_obj["total"]["key_array"][0]["string"])
