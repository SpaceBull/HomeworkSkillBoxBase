class MyDict(dict):
    """
    Класс МойСловарь. Родитель: dict
    """
    def get(self, key, default=None):
        """
            Метод, который ищет значение от ключа (key) в словаре.
        :param key: передается ключ из словаря.
        :param default: значение, которое возвращается если нет искомого ключа в словаре.
        :return: возвращаем через родительский класс (dict) значение от ключа(key), но если его нет,
        возвращаем default которому мы присвоили значение '0'
        """
        return super(MyDict, self).get(key, 0)


b = MyDict({1: 'Gt', 2: 'rs'})
print(b.get(key=1))
print(b.get(key=3))
