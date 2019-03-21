from processing.ProcessingResult import ProcessingResult


class CompositionProcessor:
    """
        Главный класс по обработке обнаруженных объектов.
        Здесь регистрируются рекогнизеры композиций,
        которыми затем обрабатываются передающиеся объекты
    """

    recognizers: list = []
    """Список зарегистрированных рекогнизеров композиций """

    def __init__(self):
        #add_recognizer(ProgressiveComposition())
        pass

    def add_recognizer(self, recognizer):
        """
            Регистрирует рекогнизер композиции,
            который будет использоваться при обработке объектов
        :param recognizer: экземпляр рекогнизера композиции
        """
        self.recognizers.append(recognizer)

    def process_objects(self, objects):
        """
            Пробегается по рекогнизером, обрабатывает каждым рекогнизером переданные объекты.
            Результаты обработки добавляем к финальному результату
        :param objects: объекты для обработки
        :return: результаты обработки каждым рекогнизером
        """

        # создаём список с результатами
        results = []
        for recognizer in self.recognizers:
            # обрабатываем рекогнизером объекты, получаем вероятность композиции
            confidence = recognizer.recognize_composition(objects)
            composition_type = recognizer.composition_type()  # получаем тип композиции
            result = ProcessingResult(composition_type, confidence)  # создаём результат обработки
            results.append(result)  # добавляем созданный результат обработки
        return results  # возвращаем результаты
