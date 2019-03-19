
class ObjectNameTable(dict):
    names: dict = {}

    def __init__(self, fn):
        self.load_table(fn)

    def load_table(self, fn):
        self.names.clear()
        with open(fn, 'r', encoding='utf8') as fp:
            for line in fp:
                spl = line.split('=')
                key = spl[0].strip()
                val = spl[1].strip()
                self.names[key] = val

    def translate(self, string):
        return 'Неизвестно' if string not in self.names else self.names[string]
