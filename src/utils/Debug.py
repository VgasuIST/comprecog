import cv2 as cv
import PIL as PILLOW

PROGRAM_TITLE = 'Composition Recognizer'
PROGRAM_VERSION = '0.1'


class Debug:
    @staticmethod
    def print_startup_debug_info():
        """
            Выводит инофрмацию о библиотеках и дебаг информацию в консоль
        """
        print('{0} v{1}'.format(PROGRAM_TITLE, PROGRAM_VERSION))
        print('OpenCV:', cv.__version__)
        print('PIL (Pillow):', PILLOW.__version__)
        print('')
