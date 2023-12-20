from dataclasses import dataclass

@dataclass
class Coordinates:
    x1: int
    x2: int
    y1: int
    y2: int


def ask_coordinate():
    pixel = input("Please write a pixel number") # das müsste man viel sicherer machen
    