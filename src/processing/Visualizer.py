import cv2 as cv


class Visualizer:
    def show(self, img, detections):
        for detection in detections:
            point1, point2 = detection.denormalized_points(img)
            center = detection.denormalized_center(img)
            cv.rectangle(img, point1, point2, (255, 0, 255), 4)
            cv.putText(img, detection.name, center, cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv.imshow('contours', img)
        cv.waitKey()

    def exit(self):
        cv.waitKey()
