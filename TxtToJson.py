import json

def txt_to_json(txt_file_path, json_file_path):
    # Чтение данных из текстового файла
    with open(txt_file_path, 'r') as txt_file:
        lines = txt_file.readlines()

    # Удаление пустых строк и лишних символов
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # Создание списка из строк файла
    data = {'name': cleaned_lines}

    # Запись данных в JSON файл
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Замените пути на пути к вашим файлам
txt_file_path = 'in.txt'
json_file_path = 'out.json'

# Вызов функции для преобразования файла
txt_to_json(txt_file_path, json_file_path)
