import cv2

def recognize(data):
    grey_scale = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(data, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    pixelpointsCV2 = cv2.findNonZero(thresh1)

    x = []
    y = []
    for i in pixelpointsCV2:
        x.append(i[0][0])
        y.append(-i[0][1])

    return (x, y)