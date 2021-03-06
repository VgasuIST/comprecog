

class ImageRecognizer:
    """
        Интерфейс распознователя изображений.
        Реализации принимают имя изображения, загружают,
        а затем возращают детекшны и само изображение.
    """

    def process_image(self, image):
        """
            Обрабатывает изображение конкретным способом
            в зависимости от реализации и составляет свои детекшны,
            которые затем возвращаются после выполнения функции
        :param file_name: имя изображения
        :return: detections
        """
        raise NotImplementedError()


