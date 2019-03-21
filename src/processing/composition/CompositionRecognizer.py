

class CompositionRecognizer:
    """
    Интерфейс распознователя композиции. Каждая реализация задаёт
    свои правила распознования и имеет своё название соотвествующей композиции
    """

    def recognize_composition(self, objects):
        """
        Распознаёт композицию из объектов
        :param objects: объекты для обработки
        :return: шанс того, что объекты представляют из себя композицию
        """
        raise NotImplementedError()

    def composition_type(self):
        """
        Возвращает имя композиции
        :return:
        """
        raise NotImplementedError()
