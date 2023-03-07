class Cell:
    grid_cells = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }

    def __init__(self, number_cell):
        self.number_cell = number_cell

    def checks_the_cell(self, cell_symbol):
        for key, value in Cell.grid_cells.items():
            if key == self.number_cell:
                if value == ' ':
                    Cell.grid_cells[self.number_cell] = cell_symbol
                    example_board = Board(cell_symbol)
                    example_board.info_result()
                else:
                    print('Клетка занята')


class Board:
    flag = False
    count = 0

    def __init__(self, cell_symbol):
        self.symbol = [cell_symbol for _ in range(3)]

    def info_result(self):
        Board.count += 1
        copy_cell = list(Cell.grid_cells.values())
        line_1 = copy_cell[:3]
        line_2 = copy_cell[3:6]
        line_3 = copy_cell[6:9]
        line_4 = copy_cell[0::4]
        line_5 = copy_cell[2:7:2]
        line_6 = copy_cell[2::3]
        line_7 = copy_cell[0::3]
        line_8 = copy_cell[1::3]
        print('\n', line_1, '\n', line_2, '\n', line_3)
        if line_1 == self.symbol or line_2 == self.symbol or line_3 == self.symbol or line_4 == self.symbol or \
                line_5 == self.symbol or line_6 == self.symbol or line_7 == self.symbol or line_8 == self.symbol:
            print('Победа!\n')
            Board.flag = True
        elif Board.count == 9:
            print('Ничья!\n')
            Board.flag = True


class Player:
    def __init__(self, name, cell_symbol):
        self.name = name
        self.cell_symbol = cell_symbol

    def cell_number(self, cell_number):
        print(f'{self.name} ходит на {cell_number} клетку')
        temp = Cell(cell_number)
        temp.checks_the_cell(self.cell_symbol)


print('Номера ячеек:')
print('[1 2 3]\n[4 5 6]\n[7 8 9]')
player_1 = Player('Алекс', 'X')
player_2 = Player('Ника', 'O')
while not Board.flag:
    choice = int(input('Введите номер ячейки: '))
    player_2.cell_number(choice)
    choice = int(input(f'Введите номер ячейки: '))
    player_1.cell_number(choice)
