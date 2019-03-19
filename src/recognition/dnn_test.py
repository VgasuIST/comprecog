import cv2 as cv
import numpy as np

CONF_THRESH = 0.5
NMS_THRESH = 0.45

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

# read names of classes
with open('resources/synset_words.txt') as f:
    classes = [x[x.find(' ') + 1:] for x in f]
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv.dnn.readNetFromCaffe('resources/bvlc_googlenet.prototxt', 'resources/bvlc_googlenet.caffemodel');
img = cv.imread('resources/tests/test2.1.jpg')

imresized = cv.resize(img, (224, 224))
Width = imresized.shape[1]
Height = imresized.shape[0]

blob = cv.dnn.blobFromImage(imresized, 1, (224, 224), (104, 117, 123))
print("Blob:", blob.shape)

net.setInput(blob)
output = net.forward()

print(output)

cv.imshow('', img)
cv.waitKey()
cv.destroyAllWindows()
