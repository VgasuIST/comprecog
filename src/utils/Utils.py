import cv2 as cv
import PIL as PILLOW


class Utils:
    """
    Утилиты для работы с программой. Хранит и выводит полезные данные для отладки и не только
    """

    PROGRAM_TITLE = 'Composition Recognizer'
    """Константа с именем программы"""

    PROGRAM_VERSION = '0.1'
    """Константа с версией программы"""

    @staticmethod
    def print_startup_debug_info():
        """ Выводит инофрмацию о библиотеках и отладочную информацию в консоль """
        print('{0} v{1}'.format(Utils.PROGRAM_TITLE, Utils.PROGRAM_VERSION))
        print('OpenCV:', cv.__version__)
        print('PIL (Pillow):', PILLOW.__version__)
        print('')
