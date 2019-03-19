from recognition.ContourRecognizer import ContourRecognizer
from utils.Visualizer import Visualizer
from utils.ObjectNameTable import ObjectNameTable


def __main__():
    name_table = ObjectNameTable('resources/localized_names.txt')
    vis = Visualizer(name_table)
    recognizer = ContourRecognizer()

    # обрабатываем файл, возвращаем блоб + детекшны
    image, detections = recognizer.process_file('resources/tests/test2_.jpg')

    # показываем результат визуализером
    vis.show(image, detections)


__main__()
