#clasa pentru subscriptii
class Subscription:
    def __init__(self, city=None, temp=None, rain=None, wind=None, direction=None, date=None):
        self.city = city
        self.temp = temp
        self.rain = rain
        self.wind = wind
        self.direction = direction
        self.date = date
        
    def __str__(self):
        return f"{{(city,=,{self.city});(temp,>=,{self.temp});(rain,{self.rain});(wind,<,{self.wind});(direction,{self.direction})}}"

#constrangerile pentru subscriptii
subscription_structure = {
    "city": {"frequency": 0.9, "type": str},
    "temp": {"frequency": 0.8, "type": int},
    "rain": {"frequency": 0.7, "type": float},
    "wind": {"frequency": 0.8, "type": int},
    "direction": {"type": str},
    "date": {"type": str}
}

