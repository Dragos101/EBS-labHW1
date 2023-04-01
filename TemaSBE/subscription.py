import random

class Subscription: 
    subscription_frequency = {
        "city": {"frequency": 0.9},
        "temp": {"frequency": 0.8},
        "rain": {"frequency": 0.7},
        "wind": {"frequency": 0.8},
        "direction": {"frequency": 0.8},
        "date": {"frequency": 0.8}
    }

    subscription_structure = {
        "city": {"type": str, 'values': ["Pascani", "Brasov", "Cluj"]},
        "temp": {"type": int, 'values': (-10, 40)},
        "rain": {"type": float, 'values': (0.0, 1.0)},
        "wind": {"type": int, 'values': (0, 30)},
        "direction": {"type": str, 'values': ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]},
        "date": {"type": str, 'values': ["1.01.2023", "2.01.2023", "3.01.2023", "4.01.2023"]}
    }

    def generate_objects(self, n):
        objects = []
        for i in range(n):
            obj = {}
            for key, value in self.subscription_structure.items():
                if key in self.subscription_frequency and random.random() > self.subscription_frequency[key]['frequency']:
                    continue
                if value['type'] == str:
                    obj[key] = random.choice(value['values'])
                elif value['type'] == int:
                    obj[key] = random.randint(value['values'][0], value['values'][1])
                elif value['type'] == float:
                    obj[key] = round(random.uniform(value['values'][0], value['values'][1]), 2)
            objects.append(obj)
        return objects