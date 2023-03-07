import random


class Card:
    def __init__(self):
        self.name_card = [
            'Двойка', 'Тройка', 'Четвёрка', 'Пятерка', 'Шестёрка',
            'Семёрка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
            'Дама', 'Король', 'Туз'
        ]
        self.card_weight = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


class Deck:
    def __init__(self):
        self.player = Card()

    def add_a_card(self):
        index_card = random.randint(0, 12)
        return self.player.name_card[index_card], self.player.card_weight[index_card]

    def play(self, person, computer):
        while True:
            if computer <= 19:
                print('Компьютер берет 1 карту')
                new_card = self.add_a_card()
                computer += new_card[1]
                continue
            if person <= 19:
                new_card = input('\nВзять карту? (да или нет): ').lower()
                if new_card == 'да':
                    new_card = self.add_a_card()
                    person += new_card[1]
                    print(f'Выпала тебе карта {new_card[0]} и теперь стало {person}\n')
                else:
                    return person, computer
            else:
                return person, computer


class Player:
    def __init__(self, name):
        self.name = name

    def info(self):
        deck = Deck()
        second_card = deck.add_a_card()
        first_card = deck.add_a_card()
        summ_card = second_card[1] + first_card[1]
        print(f'У Игрока {self.name} две карты: {second_card[0]} и {first_card[0]}')
        print(f'В сумме {summ_card} очков\n')
        return summ_card


man = Player('Вася')
computer = Player('Компьютер')

copy_person = man.info()
copy_bot = computer.info()
card = Deck()

player = card.play(copy_person, copy_bot)
person = player[0]
bot = player[1]

while True:
    if person > 21:
        print('Ты проиграл')
    elif bot > 21:
        if person <= 21:
            print(f'У компьютера {bot} а у тебя {person} - Ты выйграл!')
    elif person > 21:
        if bot <= 21:
            print(f'У компьютера {bot} а у тебя {person} - Компьютер выйграл!')
    elif person == bot or bot and person > 21:
        print(f'У компьютера {bot} а у тебя {person} - Ничья')
    elif person == 21:
        print(f'У компьютера {bot} а у тебя {person} - Ты выйграл!')
    elif bot == 21:
        print(f'У компьютера {bot} а у тебя {person} - Компьютер выйграл!')
    break

