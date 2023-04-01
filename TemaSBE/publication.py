#clasa de publicatii
class Publication:
    def __init__(self, stationid=None, city=None, temp=None, rain=None, wind=None, direction=None, date=None):
        self.stationid = stationid
        self.city = city
        self.temp = temp
        self.rain = rain
        self.wind = wind
        self.direction = direction
        self.date = date
        self.constraints = publication_structure
        
        for field, (ftype, fconstraints) in publication_structure.items():
            fvalue = getattr(self, field)
            
            # verifica tipul campului
            if not isinstance(fvalue, ftype):
                raise PublicationConstraintError(f"Invalid field {field}: expected type {ftype}, got {type(fvalue)}")
            
            # verifica valoarea campului
            if fvalue not in fconstraints:
                raise PublicationConstraintError(f"Invalid field {field}: value {fvalue} not in {fconstraints}")

        
        
    def __str__(self):
        return f"({self.stationid}, {self.city}, {self.temp}, {self.rain}, {self.wind}, {self.direction}, {self.date})"


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

#exceptia aruncata in cazul in care nu se respecta constrangerile
class PublicationConstraintError(Exception):
    pass

