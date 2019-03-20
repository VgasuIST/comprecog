
class DetectedObject:
    """
        DetectedObject - универсальный результат обнаружения объекта с изображения
    """

    name: str
    """ Имя обнаруженного объекта """

    x1: float
    """ Нормализированная X-координата (0-1) левого верхнего угла на изображении """

    y1: float
    """ Нормализированная Y-координата (0-1) левого верхнего угла на изображении """

    x2: float
    """ Нормализированная X-координата (0-1) правого нижнего угла на изображении """

    y2: float
    """ Нормализированная Y-координата (0-1) правого нижнего угла на изображении """

    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def denormalized_points(self, image):
        """
            Возвращает денормализованные координаты ограничительной рамки на изображении
            :param image: изображение
            :return: координаты двух точек (x,y)
        """

        image_w = image.shape[1]
        image_h = image.shape[0]
        p1 = int(self.x1*image_w), int(self.y1*image_h)
        p2 = int(self.x2*image_w), int(self.y2*image_h)
        return p1, p2

    def denormalized_center(self, image):
        """
            Возвращает денормализованные координаты центра ограничительной рамки на изображении
            :param image: изображение
            :return: координаты (x,y)
        """

        image_w = image.shape[1]
        image_h = image.shape[0]
        return int((self.x1+self.x2)*0.5*image_w), int((self.y1+self.y2)*0.5*image_h)

    def __str__(self):
        """
            Вспомогательный метод для вывода объекта в консоль
            :return: строковое представление объекта
        """
        return '{0}({1:.2f} {2:.2f} -> {3:.2f} {4:.2f})'\
            .format(self.name, self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        """
           Вспомогательный метод для вывода объекта в консоль
           :return: строковое представление объекта
        """
        return self.__str__()
