
import matplotlib.pyplot as plt
import matplotlib.patches as pt

from image import Img
from coordinates import Coordinates, ask_coordinate
from roi import Roi, ask_roi
from recognize import recognize
from rescale import crop, rescale_final_data
from output import output

#path = r"C:\Users\Benja\Code\Python\PlotDigitizer\data\plot digitizer test.PNG"
#read_image(path)
def digitize_plot(path):
    """Function which does everything"""
    img = Img(path=path)
    img.read_data()


    #plot_image()
    fig, ax = plt.subplots()
    ax.imshow(img.data)
    ax.grid()
    fig.savefig(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\check\temp.png")

    #ask_coordinates()
    all_coordinates = []
    for _ in ("x1", "x2", "y1", "y2"):
        state = True
        while state:
            print("Please define the coordinate ", _, ":")
            coordinate = ask_coordinate()
            fig, ax = plt.subplots()
            if _=="x1" or _=="x2":
                ax.vlines(coordinate["pixel"],
                            0, img.data.data.shape[0],
                            color='red')
            else:
                ax.hlines(coordinate["pixel"],
                            0, img.data.data.shape[1],
                            color='red')
            ax.imshow(img.data)
            fig.savefig(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\check\temp.png")
            happy = input(f"Does this fit to your named value: {coordinate['value']} \n yes or no")
            if happy.lower() == "yes":
                state = False
                all_coordinates.append(coordinate)

    coordinates = Coordinates(x1=all_coordinates[0], 
                            x2=all_coordinates[1],
                            y1=all_coordinates[2],
                            y2=all_coordinates[3])


    #ask_roi()
    state = True
    while state:
        roi = ask_roi()
        rectangle = pt.Rectangle((roi.x,roi.y), roi.width, roi.height, facecolor='None', edgecolor='red')
        fig, ax = plt.subplots()
        ax.add_patch(rectangle)
        ax.imshow(img.data)
        fig.savefig(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\check\temp.png")
        happy = input("Is this correct? \n yes ro no")
        if happy.lower() == "yes":
            state = False


    #crop()
    crop(img, roi)


    #recognize_data()
    final_data = recognize(img.croped_data)

    # bis hier hin klappt es wohl
    final_data = rescale_final_data(final_data, coordinates, roi)


    output(final_data)


