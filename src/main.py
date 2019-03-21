from utils.Utils import Utils

from recognition.ContourImageRecognizer import ContourRecognizer
from utils.Visualizer import Visualizer
from utils.ObjectNameTable import ObjectNameTable

from processing.CompositionProcessor import CompositionProcessor


from ComprecogApplication import ComprecogApplication
import wx

def __main__():
    # выводим отладочную информацию в консоль
    Utils.print_startup_debug_info()

    name_table = ObjectNameTable('resources/localized_names.txt')
    vis = Visualizer(name_table)
    recognizer = ContourRecognizer()
    processor = CompositionProcessor()

    # обрабатываем файл, возвращаем блоб + детекшны
    image, detections = recognizer.process_file('resources/tests/test2_.jpg')

    # обрабатываем детекшны и возвращаем лист с ProcessingResult'ами
    results = processor.process_objects(detections)

    # показываем результат визуализером
    vis.show(image, detections, results)
    vis.exit()


__main__()
