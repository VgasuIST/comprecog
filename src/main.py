from recognition.ContourRecognizer import ContourRecognizer
from processing.Visualizer import Visualizer


def __main__():
    vis = Visualizer()
    recognizer = ContourRecognizer()

    # обрабатываем файл, возвращаем блоб + детекшны
    image, detections = recognizer.process_file('resources/tests/test2.1.jpg')

    # показываем результат визуализером
    vis.show(image, detections)


__main__()
