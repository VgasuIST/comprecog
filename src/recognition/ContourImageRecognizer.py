import cv2 as cv

from recognition.ImageRecognizer import Recognizer
from recognition.DetectedObject import DetectedObject


class ContourRecognizer(Recognizer):
    """ Обнаружение обьектов при помощи контуров

           Данный класс читает изображение и находит
           в нём контуры по определённым фильтрам, пороги
           которых можно регулировать аргрументами конструктора
    """

    th1: int
    """ Порог отсечения оттенков серого. Оттенок, выше данного порога принимает значение 255 """

    th2: int
    """ Порог для закрытия контуров """

    def __init__(self, th1: int = 150, th2: int = 1):
        self.th1 = th1
        self.th2 = th2

    @staticmethod
    def contour2shape(c):
        """
            Обнаруживаем фигуру по её контуру
            :return имя фигуры
        """

        # аппроксимируем (сглаживаем) контур
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * peri, True)
        shape = "polygon"

        # если фигура имеет 3 вершины, то данная фигура - треугольник
        if len(approx) == 3:
            shape = "triangle"

            # если фигура имеет 4 вершины, то она
            # скорее всего либо квадрат, либо прямоугольник
        elif len(approx) == 4:
            # получаем ограничительную рамку фигуры для вычисления отношения сторон
            (x, y, w, h) = cv.boundingRect(approx)
            ar = w / float(h)

            # если фигура имеет равные стороны, то фигура - квадрат
            # иначе фигура - прямоугольник
            shape = "square" if 0.98 <= ar <= 1.02 else "rectangle"

            # если фигура имеет 5 вершин, то она - пятиугольник
        elif len(approx) == 5:
            shape = "pentagon"

            # иначе мы распознаём фигуру как круг
        else:
            shape = "circle"

        return shape

    def process_file(self, file_name):
        image = cv.imread(file_name)
        # если не получилось прочитать файл, выбрасываем исключение
        if image is None:
            raise IOError('imread() failed')

        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # конвертируем в чб изображение
        blurred = cv.GaussianBlur(gray, (5, 5), 0)  # размываем для устранения jpg-артефактов

        # применяем порог для отсечения ненужных оттенков (и артефактов)
        thresh = cv.threshold(blurred, self.th1, 255, cv.THRESH_BINARY)[1]

        edged = cv.Canny(thresh, 10, 250)  # применяем фильтр Cranny для обрисовки контуров

        # создаём закрытие, закрываем им "дырки" в контурах
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (self.th2, self.th2))
        closed = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel)

        contours, hierarchy = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # находим контуры

        image_w = float(image.shape[1])
        image_h = float(image.shape[0])

        detections = list()
        # цикл по контурам
        for c in contours:
            shape = self.contour2shape(c)
            x, y, w, h = cv.boundingRect(c)  # получаем ограничительную рамку

            detection = DetectedObject(shape, x/image_w, y/image_h, (x+w)/image_w, (y+h)/image_h)
            detections.append(detection)

        return image, detections
