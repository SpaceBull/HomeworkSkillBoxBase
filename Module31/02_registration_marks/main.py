import re

text = """ А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"""

private_auto = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}\w+', text)
print(f'Список номеров частных автомобилей: {private_auto}')

taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d+', text)
print(f'Список номеров такси: {taxi}')
