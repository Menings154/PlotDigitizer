from dataclasses import dataclass

@dataclass
class Roi:
    x: int
    y: int
    width: int
    hight: int

def ask_roi():
    print("No, we define the region of interest (ROI) which will be a square")
    x = input("What is the x coordinate of your upper left corner of your ROI?")
    y = input("What is the y coordinate of your upper left corner of your ROI?")
    width = input("What is the width of your ROI?")
    hight = input("What is the hight of your ROI?")
    return Roi(x=x, y=y, width=width, hight=hight)