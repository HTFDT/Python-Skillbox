import datetime
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
                value = without_spaces.strip()
            d[list_naming[i]] = value

        data.append(d)
    return data


def print_vacancies(data_vacancies):
    for i, vac in enumerate(data_vacancies, 1):
        data = formatter(vac)
        for field in data:
            print(field, end=": ")
            if isinstance(data[field], list):
                print(*data[field], sep=", ")
            else:
                print(data[field])
        if i != len(data_vacancies):
            print()


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
        new_row[key] = value

    return new_row


filename = input()
headers, reader = csv_reader(filename)
data = csv_filter(reader, headers)
print_vacancies(data)
