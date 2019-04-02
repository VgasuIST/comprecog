import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import numpy as np


class Visualizer:
    """
        Визуализирует результат на экране. Обводит рамки обнаруженных объектов
         и выводит их локализированное имя
        XXX: Для русских символов пришлось использовать библиотеку Pillow (форк PIL)
    """

    name_table = None
    """ таблица с локализированными именами объектов """

    font = None
    """ шрифт для рисования имен объектов """

    def __init__(self, name_table):
        self.name_table = name_table

        # загружаем шрифт для рисования
        font_path = 'resources/fonts/consolas.ttf'
        self.font = ImageFont.truetype(font_path, 20)

    def visualize_detections(self, img, detections):
        img = img.copy()
        for detection in detections:
            # получаем координаты ограничительной рамки
            point1, point2 = detection.denormalized_points(img)
            # рисуем ограничительную рамку
            cv.rectangle(img, point1, point2, (255, 0, 255), 4)

        img_pil = Image.fromarray(img)  # конвертируем opencv-изображение в PIL-изображение
        draw = ImageDraw.Draw(img_pil)  # создаём "рисовалку" на PIL-изображении

        for detection in detections:
            center = detection.denormalized_center(img)
            draw.text(center, self.name_table.translate(detection.name),
                      font=self.font, fill=(255, 0, 0, 255))

        return np.array(img_pil)

