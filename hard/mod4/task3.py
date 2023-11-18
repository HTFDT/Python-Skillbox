import datetime
import re
import csv

import prettytable as pt

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

currency_map = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум"
}

exp_map = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет"
}


def csv_reader(file_name):
    with open(file_name, "r", encoding="utf_8_sig") as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            return None, None
        vacancies = [x for x in reader if len(x) == len(headers) and not any([y == "" for y in x])]
    return headers, vacancies


def csv_filter(reader, list_naming):
    data = []
    for j in range(len(reader)):
        d = {}
        for i in range(len(reader[j])):
            without_tags = re.sub(r"</?\w+(\s*/?)>", "", reader[j][i])
            without_spaces = re.sub(r"[^\S\r\n]+", " ", without_tags)
            value = without_spaces.strip()
            d[list_naming[i]] = value

        data.append(d)
    return data


def print_vacancies(data_vacancies):
    t = pt.PrettyTable()
    t.align = 'l'
    t.hrules = pt.ALL
    t.vrules = pt.ALL
    t.field_names = ["№"] + list(formatter(data_vacancies[0]).keys())
    t.max_width = 20
    for i, vac in enumerate(data_vacancies, 1):
        data = formatter(vac)
        t.add_row([i] + list(data.values()))
    print(t.get_string())


def formatter(row):
    new_row = {}
    unused_fields = {"salary_from", "salary_to", "salary_currency", "salary_gross"}
    for field in row:
        key = naming_map[field]
        value = row[field]
        if field == "experience_id":
            value = exp_map[value]
        elif field == "premium":
            value = "Да" if row[field] == "True" else "Нет"
        elif field in unused_fields:
            if "Оклад" not in new_row:
                key = "Оклад"
                fr = format(float(row['salary_from']), ",.0f").replace(",", " ")
                to = format(float(row['salary_to']), ",.0f").replace(",", " ")
                value = (f"{fr} - {to} "
                         f"({currency_map[row['salary_currency']]}) "
                         f"({'Без вычета налогов' if row['salary_gross'] == 'True' else 'С вычетом налогов'})")
            else:
                continue
        elif field == "published_at":
            key = "Дата публикации вакансии"
            dt = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
            value = dt.strftime("%d.%m.%Y")
        if len(value) > 100:
            value = value[:100] + "..."
        new_row[key] = value

    return new_row


filename = input()
headers, reader = csv_reader(filename)
if headers is None:
    print("Пустой файл")
elif len(reader) == 0:
    print("Нет данных")
else:
    data = csv_filter(reader, headers)
    print_vacancies(data)
