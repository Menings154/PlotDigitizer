import cv2
import matplotlib.pyplot as plt

path = r"C:\Users\Benja\Code\Python\PlotDigitizer\data\plot digitizer test.PNG"

img = cv2.imread(path)

fig, ax = plt.subplots()
ax.imshow(img)
ax.plot(200, 200, color='red', marker='v')
ax.vlines(200, 0, 575)
fig.savefig(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\check\temp.png")