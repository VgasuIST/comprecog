import cv2 as cv


class Visualizer:
    def show(self, img, detections):

        img_h, img_w = img.shape[:2]
        for detection in detections:
            point1 = int(detection.x1*img_w), int(detection.y1*img_h)
            point2 = int(detection.x2*img_w), int(detection.y2*img_h)
            center = int((point1[0] + point2[0])/2), int((point1[1] + point2[1])/2)
            cv.rectangle(img, point1, point2, (255, 0, 255), 4)
            cv.putText(img, detection.name, center, cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv.imshow('contours', img)
        cv.waitKey()

    def exit(self):
        cv.waitKey()
