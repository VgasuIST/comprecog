
class ObjectNameTable:
    """
    Загружает и хранит локализированные имена известных
    объектов для удобного и универсального вывода в графическом интерфейсе
    """

    names: dict = {}
    """
    Словарь с локализированными именами. Ключ - нелокализированное
    нормализованное имя, Значение - переведённое имя
    """

    def __init__(self, fn):
        self.load_table(fn)

    def load_table(self, fn):
        """
        Загружает локализации из файла
        :param fn: имя файла с локализациями
        """
        self.names.clear()
        with open(fn, 'r', encoding='utf8') as fp:
            for line in fp:
                spl = line.split('=')
                key = spl[0].strip()
                val = spl[1].strip()
                self.names[key] = val

    def translate(self, string):
        """
        Переводит нормализованное нелокализированное имя в локализированное
        :param string: имя
        :return: перевод
        """
        return 'Неизвестно' if string not in self.names else self.names[string]
