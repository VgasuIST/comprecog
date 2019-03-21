

class ProcessingResult:
    """
    Результат обработки объектов рекогнизером композиций.
    Хранит в себе данные о композиции и вероятности что объекты представляют собой данную композицию
    """

    composition_type: str
    """Имя композиции"""

    confidence: float
    """Вероятность композиции"""

    def __init__(self, composition_type, confidence):
        self.composition_type = composition_type
        self.confidence = confidence

    def get_composition_type(self):
        """
        геттер для composition_type
        :return: вероятность композиции
        """
        return self.composition_type

    def get_confidence(self):
        """
        геттер для confidence
        :return: вероятность композиции
        """
        return self.confidence
