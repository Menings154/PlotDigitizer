from dataclasses import dataclass

@dataclass
class Coordinates:
    x1: dict
    x2: dict
    y1: dict
    y2: dict


def ask_coordinate():
    pixel = input("Please write a pixel number") # das müsste man viel sicherer machen
    value = input("Please give the corresponding value")
    return {"pixel": pixel,
            "value": value}