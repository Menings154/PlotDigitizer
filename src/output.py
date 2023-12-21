import matplotlib.pyplot as plt
import numpy as np

def output(final_data):
    fig, ax = plt.subplots()
    ax.scatter(final_data[0], final_data[1])
    fig.savefig(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\output\final_plot.png")
    np.savetxt(r"C:\Users\Benja\Code\Python\PlotDigitizer\data\output\final_data.csv", final_data)