# %%
import matplotlib.pyplot as plt

from image import Img
from coordinates import Coordinates, ask_coordinate

path = r"C:\Users\Benja\Code\Python\PlotDigitizer\data\plot digitizer test.PNG"
#read_image(path)
img = Img(path=path)
img.read_data()

# %%
#plot_image()
fig, ax = plt.subplots()
ax.imshow(img.data)
#  noch ein grid mit den coordinaten machen?
# %% bei dem ganzen Abschnitt bin ich nicht sicher, ob es funktionirt, das linebr mit wikrlich plots speichern machen
#ask_coordinates()
all_coordinates = []
for _ in ("x1", "x2", "y1", "y2"):
    state = True
    while state:
        print("Please define the coordinate ", _, ":")
        coordinate = ask_coordinate()
        fig, ax = plt.subplots()
        if _ == "x1" or "x2":
            ax.vlines(coordinate["pixel"],
                        0, img.data.data.shape[0],
                        color='red')
        else:
             ax.hlines(coordinate["pixel"], 0, img.data.data.shape[1])
        ax.imshow(img.data)
        happy = input(f"Does this fit to your named value: {coordinate['value']} \n yes or no")
        if happy.lower() == "yes":
            state = False
            all_coordinates.append(coordinate)

coordinates = Coordinates(x1=all_coordinates[0], 
                          x2=all_coordinates[1],
                          y1=all_coordinates[2],
                          y2=all_coordinates[3])

# %%
#ask_roi()
#rescale()
#recognize_data()
#plot_data()
#write_data()


# %%
