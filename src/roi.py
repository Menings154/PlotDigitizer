from dataclasses import dataclass

@dataclass
class Roi:
    x: int
    y: int
    width: int
    height: int

def ask_roi():
    print("No, we define the region of interest (ROI) which will be a square")
    x = int(input("What is the x coordinate of your upper left corner of your ROI?"))
    y = int(input("What is the y coordinate of your upper left corner of your ROI?"))
    width = int(input("What is the width of your ROI?"))
    height = int(input("What is the hight of your ROI?"))
    return Roi(x=x, y=y, width=width, height=height)