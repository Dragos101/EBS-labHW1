#clasa de publicatii
import random

class Publication:
    #constrangerile pentru obiectele de tip publicatie
    publication_structure = {
        "stationid": (int, (0, 100)),
        "city": (str, ["Pascani", "Brasov", "Cluj"]),
        "temp": (int, (-10, 40)),
        "rain": (float, (0.0, 1.0)),
        "wind": (int, (0, 30)),
        "direction": (str, ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]),
        "date": (str, ["1.01.2023", "2.01.2023", "3.01.2023", "4.01.2023"])
    }

    def __init__(self):
        args = {}
        for key, value in self.publication_structure.items():
            type_, choices = value
            if type_ == int:
                args[key] = random.randint(*choices)
            elif type_ == float:
                args[key] = round(random.uniform(*choices), 2)
            elif type_ == str:
                args[key] = random.choice(choices)
            else:
                raise ValueError(f"Unsupported type {type_}")
        self.__dict__ = args
  
    def __str__(self):
        return f"({self.stationid}, {self.city}, {self.temp}, {self.rain}, {self.wind}, {self.direction}, {self.date})"

