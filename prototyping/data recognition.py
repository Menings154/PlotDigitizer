import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path = r"C:\Users\Benja\Code\Python\PlotDigitizer\Plots\plot digitizer test.PNG"#r"Plots\plot digitizer test.PNG"
img = cv2.imread(img_path, 0)
cv2.imshow("grayscale image", img)
#cv2.waitKey(0)
ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imshow("threshhold", thresh1)
#cv2.waitKey(0)
pixelpointsCV2 = cv2.findNonZero(thresh1)

#print(pixelpointsCV2[0])
x = []
y = []

for i in pixelpointsCV2:
    x.append(i[0][0])
    y.append(-i[0][1])

plt.figure()
plt.scatter(x, y)
plt.show()