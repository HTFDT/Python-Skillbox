import re
import csv

naming_map = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    "employer_name": "Компания",
    "salary_from": "Нижняя граница вилки оклада",
    "salary_to": "Верхняя граница вилки оклада",
    "salary_gross": "Оклад указан до вычета налогов",
    "salary_currency": "Идентификатор валюты оклада",
    "area_name": "Название региона",
    "published_at": "Дата и время публикации вакансии"
}


def csv_reader(file_name):
    with open(file_name, "r", encoding="utf_8_sig") as f:
        reader = csv.reader(f)
        headers = next(reader)
        vacancies = [x for x in reader if len(x) == len(headers) and not any([y == "" for y in x])]
    return headers, vacancies


def csv_filter(reader, list_naming):
    data = []
    for j in range(len(reader)):
        d = {}
        for i in range(len(reader[j])):
            without_tags = re.sub(r"</?\w+(\s*/?)>", "", reader[j][i])
            without_spaces = re.sub(r"[^\S\r\n]+", " ", without_tags)
            if "\n" in without_spaces:
                value = [x.strip() for x in without_spaces.split("\n")]
            else:
                v = without_spaces.strip()
                value = "Да" if v == "True" else "Нет" if v == "False" else v
            d[list_naming[i]] = value

        data.append(d)
    return data


def print_vacancies(data_vacancies, dict_naming):
    for i, vac in enumerate(data_vacancies, 1):
        for field in vac:
            print(dict_naming[field], end=": ")
            if isinstance(vac[field], list):
                print(*vac[field], sep=", ")
            else:
                print(vac[field])
        if i != len(data_vacancies):
            print()


filename = input()
headers, reader = csv_reader(filename)
data = csv_filter(reader, headers)
print_vacancies(data, naming_map)
