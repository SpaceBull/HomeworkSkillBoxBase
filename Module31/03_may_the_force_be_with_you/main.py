# РЕШЕНИЕ В 2 способа, ТЗ несло мало ясности

import requests
import json

starships_attribute = ["name", "max_atmosphering_speed", "starship_class", "pilots"]# необходимые искомые атрибуты корабля
pilots_attribute = ["name", "height", "mass", "homeworld", "url"]# необходимые искомые атрибуты пилота

my_starships = requests.get('https://swapi.dev/api/starships/?search=Millennium')
# ищем корабль Millennium Falcon
roster = json.loads(my_starships.text) # десериализация JSON
my_starships = roster["results"]

data_starships = [{key: value} for attribute in my_starships for key, value in attribute.items()
                  if key in starships_attribute] # атрибуты корабля
pilot_attribute = [json.loads(requests.get(attribute).text) for attribute in data_starships[3]['pilots']]
# ccылки на пилотов проверяем на Respone 200 и загружаем в текст

data_pilot = [{key: value} for attribute in pilot_attribute for key, value in attribute.items()
              if key in pilots_attribute]# атрибуты пилотов

data_starships.extend(data_pilot)

with open('ser.json', 'w') as file:
    json.dump(data_starships, file, indent=4)
# сериализация

with open('ser.json', 'r') as file:
    data = json.load(file) # Здесь load, а НЕ loasds, потому что работаем с файлом

for param in data:
    print(param)

##########################################
#Второй способ

ship_name = "Millennium Falcon"  # название корабля, для которого получаем информацию
# делаем запрос на получение информации о корабле
ship_url = "https://swapi.dev/api/starships/?search=" + ship_name
ship_response = requests.get(ship_url)
ship_data = json.loads(ship_response.text)
# получаем ссылку на один корабль из ответа на запрос

ship_api_url = ship_data["results"][0]["url"]
ship_api_response = requests.get(ship_api_url)
ship_api_data = json.loads(ship_api_response.text)

# информация о корабле
ship_info = {
    "название": ship_api_data["name"],
    "максимальная скорость": ship_api_data["max_atmosphering_speed"],
    "класс": ship_api_data["starship_class"],
    "список пилотов": []
            }
# получаем информацию о пилотах из ссылок в ответе на запрос для корабля
for pilot_url in ship_api_data["pilots"]:
    pilot_api_response = requests.get(pilot_url)
    pilot_api_data = json.loads(pilot_api_response.text)
    # информация о каждом пилоте
    pilot_info = {
        "имя": pilot_api_data["name"],
        "рост": pilot_api_data["height"],
        "вес": pilot_api_data["mass"],
        "родная планета": pilot_api_data["homeworld"],
        "ссылка на информацию о родной планете": pilot_api_data["homeworld"]
    }
    ship_info["список пилотов"].append(pilot_info)
# вывод информации о корабле и пилотах в консоль
print(json.dumps(ship_info, indent=4, ensure_ascii=False))
# запись информации о корабле и пилотах в JSON-файл
with open("ship_info.json", "w", encoding="utf-8") as file:
    json.dump(ship_info, file, indent=4, ensure_ascii=False)
