import re
# 1

searchs = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
open_files = ["1", "2", "3"]
os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
my_dict = {
    "Изготовитель системы": os_prod_list,
    "Название ОС": os_name_list,
    "Код продукта": os_code_list,
    "Тип системы": os_type_list
}

def get_data():
    for i in open_files:
        with open(f"./files/info_{i}.txt", "r", encoding="cp1251") as f:
            # Читаем построчно файл
            for line in f:
                # Ищем подходящие ключи
                for key in my_dict.keys():
                    # Если ключ найден
                    if key in line:
                        # Фильтруем поиск данных
                        line = re.split(r":", line)[1]
                        line = re.findall(r"(\w+[-]?[ ]?[\.]?)", line)
                        # Удаляем пробел в конце строки
                        if line[len(line) - 1][-1] == " ":
                            line[len(line) - 1] = line[len(line) - 1].replace(" ", "")

                        # Добавляем данные
                        my_dict.get(key).append("".join(line))
    # Создаём список ключей в словаре
    my_dict["main_data"] = list(my_dict.keys())
    csv_output = [",".join(my_dict["main_data"])]    # Вывод для csv файла
    # Записывем данные для каждого файла отдельно
    for i in open_files:
        with open(f"./files/main_data_{i}.txt", "w+") as f:
            f.write(",".join(my_dict["main_data"]) + '\n')
            print(i)
            str_file = []
            for key in my_dict["main_data"]:
                str_file.append(my_dict[key][int(i)-1])
            f.write(",".join(str_file) + '\n')
            csv_output.append(",".join(str_file))   # Дополняем вывод для csv файла
    return csv_output




def write_to_csv(way_file_csv):
    result = get_data()
    with open(way_file_csv, "w+") as f:
        for i in result:
            f.write(i + "\n")


way_file_csv = "./files/result.csv"
write_to_csv(way_file_csv)


# 2
print("json")

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open("./files/orders.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        add_data = {
            "Товар": item,
            "количество": quantity,
            "цена": price,
            "покупатель": buyer,
            "дата": date
        }

        data["orders"] += [add_data]
        with open("./files/orders.json", "w+", encoding="utf-8") as s:
            json.dump(data, s, sort_keys=True, indent=4, ensure_ascii=False)



write_order_to_json("батарейка", 10, 3, "Вася", "2022-02-10")

# 3
print("yaml")

import yaml

yaml_data = {
    "1": [],
    "2": 23,
    "3": {
        "1": ord("€"),
        "2": "€"    # Просто для сравнения
    }
}

with open("./files/data.yaml", "w") as f:
    yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)

with open("./files/data.yaml") as f:
    print(f.read())

