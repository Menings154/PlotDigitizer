from src import *

path = r"C:\Users\Benja\Code\Python\PlotDigitizer\data\plot digitizer test.PNG"
#read_image(path)
img = image.Img(path=path)
img.read_data()