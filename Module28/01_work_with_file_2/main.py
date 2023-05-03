class File:
    """
    Класс "Контекст менеджер" File - Открывает файл и проверяет на наличие уже существующего.
        Attributes:
        filename - Наименование файла
        mode - Режим чтения/записи (r/w)
    """
    def __init__(self, filename: str, mode: str) -> None:
        print('Открывание файла')
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> 'File':
        """
        Метод Enter - открывая в обработке файл с заданными атрибутами, если файл уже существует,
         то откроет в режим записи.
        :return: возвращает в глобальную переменную.
        """
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод Exit - закрывает в завершение файл.
        :return: Возвращая True, подтверждая успешное завершение.
        """
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!')
