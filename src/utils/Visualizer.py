import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import numpy as np


class Visualizer:
    """
        Визуализирует результат на экране. Обводит рамки обнаруженных объектов
         и выводит их локализированное имя
        XXX: Для русских символов пришлось использовать библиотеку Pillow (форк PIL)
    """

    font = None
    name_table = None

    def __init__(self, name_table):
        font_path = 'resources/fonts/consolas.ttf'
        self.font = ImageFont.truetype(font_path, 20)
        self.name_table = name_table

    def show(self, img, detections):
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

        img = np.array(img_pil)

        cv.imshow('', img)
        cv.waitKey()

    def exit(self):
        cv.waitKey()
