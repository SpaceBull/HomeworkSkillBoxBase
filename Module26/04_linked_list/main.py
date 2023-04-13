from typing import Any, Optional


class Node:
    """
    Базовый класс "Узел"

    :arg
        value: Optional[Any] = None - "Значение" с принимаемым любым типов данных.
        next: Optional['Node'] = None - "Ссылка" на следующий узел.
    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return '{value}'.format(value=str(self.value))


class LinkedList:
    """
    Класс "Односвязный список"

    :arg
        head: Optional[Node] = None - Указатель на первый (головной) узел.
        length: длина всего списка.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList[]'

    def append(self, new_element: Any) -> None:
        """
        Метод "Добавить" новое значение в список.
        :param new_element: новое значение, которое нужно добавить в список.
        :return: self.
        """
        new_node = Node(new_element)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def get(self, index) -> int:
        """
        Метод геттер (Поиск) - найти по индексу нужное значение.
        :param index: искомый индекс
        :return: cur_node
        """
        flag = False
        cur_index = 0
        if self.length < index:
            raise IndexError
        while not flag:
            cur_node = self.head
            if index == cur_index:
                return cur_node
            else:
                cur_index += 1
                self.head = cur_node.next

    def remove(self, index) -> None:
        """
        Метод Удаления — удаляет в списке значение по заданному индексу.
        :param index: заданный индекс.
        :return: self.
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
        self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
print()
print(f'Получение третьего элемента: {my_list.get(0)}')
