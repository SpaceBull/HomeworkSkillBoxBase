class Stack:
    """
    Класс Стэк.

    Attributes:

        __new_roster (List) - Список
    """
    def __init__(self):
        self.__new_roster = []

    def __str__(self):
        return '; '.join(self.__new_roster)
    """
        Метод __str__ возвращает (принтует в консоль) задачи через "точку с запятой" 
    """
    def push(self, elem):
        self.__new_roster.append(elem)
    """
        Метод Пуш добавляет в список new_roster входящие задачи
        
        Arg:
         elem (str) - передается номер и задача
    """
    def pop(self):
        if len(self.__new_roster) == 0:
            return None
        return self.__new_roster.pop()
    """
        Метод Pop удаляет последний элемент из списка, но если список пуст, возвращает None
    """


class TaskManager:
    """
    Класс Менеджер Задач.

    Attributes:
        roster (dict) - Словарь
    """
    def __init__(self):
        self.roster = dict()

    def __str__(self):
        display = []
        if self.roster:
            for i_number in sorted(self.roster.keys()):
                display.append(f'{str(i_number)} {self.roster[i_number]}\n')
            return ''.join(display)
        """
            Метод __str__ возвращает и принтует новый список
        """

    def new_task(self, task: str, number_task: int):
        if number_task not in self.roster:
            self.roster[number_task] = Stack()
        self.roster[number_task].push(task)
        """
            Метод new_task проверяет есть ли такой номер в реестре,
            если нет, то вызывает Класс Стэк,
            иначе добавляет через метод Пуш новую задачу
            
            arg:
                task (str) - передается задача
                number_task (int) - передается номер задачи(приоритет)
        """


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)