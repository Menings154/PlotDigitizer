# %%
import matplotlib.pyplot as plt

from image import Img


path = r"C:\Users\Benja\Code\Python\PlotDigitizer\data\plot digitizer test.PNG"
#read_image(path)
img = Img(path=path)
img.read_data()

# %%
fig, ax = plt.subplots()
ax.imshow(img.data)
#plot_image()
#ask_coordinates()
#ask_roi()
#rescale()
#recognize_data()
#plot_data()
#write_data()

