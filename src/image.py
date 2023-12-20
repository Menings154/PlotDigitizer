from dataclasses import dataclass
import cv2

@dataclass
class Img:
    "Class to store all data related to an image."
    path: str

    def read_data(self):
        self.data = cv2.imread(self.path)