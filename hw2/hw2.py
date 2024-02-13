"""This is hw2 solution.

Напишите модуль, в котором функция process_data принимает путь к json-файлу
с данными о клиентах сайта
(пример файла в data_hw2.json) и путь к json-файлу вывода.
Функция process_data записывает в этот общий json статистику:
процент распределения географии пользователей по городам,
а также процент клиентов, которые были онлайн:
менее двух дней, недели, месяца, полугода, и более полугода назад.
Вынести домашнее и его тесты в отдельную папку hw2.
Тесты используют различные json-файлы.
В workflows выделить отдельные работы для проверок линтера разных домашних,
отдельные работы для тестов разных домашних
(цель состоит в том, чтобы в actions они отображались отдельными галочками).
"""
import json
import os

import extra


def process_data(input_path: str, output_path: str) -> None:

    extra.check_paths(input_path, output_path)
    try:
        with open(input_path, 'r') as input_file:
            clients = json.load(input_file)
    except ValueError:
        raise ValueError('Input file is not readable!')

    result = {
            'regions_stats': extra.process_regions(clients),
            'last_login_stats': extra.process_last_login(clients),
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as output_file:
        json.dump(result, output_file, indent=4)
