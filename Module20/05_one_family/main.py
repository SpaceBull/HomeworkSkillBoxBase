family = {
    ("Быков", "Павел"): 50,
    ("Быкова", "Ирина"): 38,
    ("Быков", "Игорь"): 71,
    ("Фролова", "Оксана"): 48,
    ("Иванова", "Наталья"): 84
}

surname = input('Введите фамилию: ').title()
for human, age in family.items():
    surname = surname + 'а'
    if surname.startswith(human):
        print(f'{human[0]} {human[1]} {age}')
