import random
import time
import threading

class Subscription: 
    subscription_structure = {
        "city": {"type": str, 'values': ["Pascani", "Brasov", "Cluj"]},
        "temp": {"type": int, 'values': (-10, 40)},
        "rain": {"type": float, 'values': (0.0, 1.0)},
        "wind": {"type": int, 'values': (0, 30)},
        "direction": {"type": str, 'values': ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]},
        "date": {"type": str, 'values': ["1.01.2023", "2.01.2023", "3.01.2023", "4.01.2023"]}
    }

    operators_struct = {
        'numbers': {'variables': ['temp', 'rain', 'wine', 'date'], 'operators': ['=', '<', '>', '>=', '<=']},
        'not_numbers': {'variables': ['city', 'directions'], 'operators': ['=', '!=']},
    }

    def __init__(self, subscription_freq, subscription_operator_freq):
        self.subscription_frequency = subscription_freq
        self.subscription_operator_freq = subscription_operator_freq

    def generate_objects(self, n):
        start_time = time.perf_counter()
        objects = []
        for i in range(n):
            x = []
            for key, value in self.subscription_structure.items():
                obj = []
                if key in self.subscription_frequency and self.subscription_frequency[key]['display'] >= self.subscription_frequency[key]['frequency'] * n:
                    continue
                obj.append(key)

                # se aloca random operatorul
                if self.subscription_operator_freq[key]['frequency'] != 0 and self.subscription_operator_freq[key]['display'] < self.subscription_operator_freq[key]['frequency'] * n:
                    obj.append('=')
                    self.subscription_operator_freq[key]['display'] = self.subscription_operator_freq[key]['display'] + 1
                elif self.subscription_operator_freq[key]['frequency'] == 0 or self.subscription_operator_freq[key]['frequency'] != 0 and self.subscription_operator_freq[key]['display'] >= self.subscription_operator_freq[key]['frequency'] * n:
                    if key in self.operators_struct['numbers']['variables']:
                        obj.append(random.choice(self.operators_struct['numbers']['operators']))
                    else: 
                        obj.append(random.choice(self.operators_struct['not_numbers']['operators']))

                self.subscription_frequency[key]['display'] = self.subscription_frequency[key]['display'] + 1
                # se aloca random valoarea pentru cheie
                if value['type'] == str:
                    obj.append(random.choice(value['values'])) 
                elif value['type'] == int:
                    obj.append(random.randint(value['values'][0], value['values'][1])) 
                elif value['type'] == float:
                    obj.append(round(random.uniform(value['values'][0], value['values'][1]), 2))

                x.append({f'{obj[0]}, {obj[1]}, {obj[2]}'})
            objects.append(x)

        end_time = time.perf_counter()
        f = open("TemaSBE/time_operations.txt", "a")
        f.write(f'Time to generate {n} subscriptions without threads :{end_time - start_time} \n')
        f.close()

        return objects
    
    def generate_objects_threads(self, n):

        subscription_frequency = {
            "city": {"frequency": 1, 'display': 0},
            "temp": {"frequency": 0.5, 'display': 0},
            "rain": {"frequency": 0.8, 'display': 0},
            "wind": {"frequency": 0.8, 'display': 0},
            "direction": {"frequency": 0, 'display': 0},
            "date": {"frequency": 0.8, 'display': 0}
        }

        subscription_operator_freq = {
            "city": {"frequency": 0, 'display': 0},
            "temp": {"frequency": 0, 'display': 0},
            "rain": {"frequency": 0.7, 'display': 0},
            "wind": {"frequency": 0, 'display': 0},
            "direction": {"frequency": 0, 'display': 0},
            "date": {"frequency": 0, 'display': 0}
        }

        start_time = time.perf_counter()
        objects = []
        threads = []
        lock = threading.Lock()
        

        def generate_object():
            x = []
            for key, value in self.subscription_structure.items():
                obj = []
                with lock:
                    if key in subscription_frequency and subscription_frequency[key]['display'] >= subscription_frequency[key]['frequency'] * n:
                        continue
                    obj.append(key)

                    # se aloca random operatorul
                    if subscription_operator_freq[key]['frequency'] != 0 and subscription_operator_freq[key]['display'] < subscription_operator_freq[key]['frequency'] * n:
                        obj.append('=')
                        subscription_operator_freq[key]['display'] = subscription_operator_freq[key]['display'] + 1
                    elif subscription_operator_freq[key]['frequency'] == 0 or subscription_operator_freq[key]['frequency'] != 0 and subscription_operator_freq[key]['display'] >= self.subscription_operator_freq[key]['frequency'] * n:
                        if key in self.operators_struct['numbers']['variables']:
                            obj.append(random.choice(self.operators_struct['numbers']['operators']))
                        else: 
                            obj.append(random.choice(self.operators_struct['not_numbers']['operators']))

                    subscription_frequency[key]['display'] = subscription_frequency[key]['display'] + 1
                    # se aloca random valoarea pentru cheie
                    if value['type'] == str:
                        obj.append(random.choice(value['values'])) 
                    elif value['type'] == int:
                        obj.append(random.randint(value['values'][0], value['values'][1])) 
                    elif value['type'] == float:
                        obj.append(round(random.uniform(value['values'][0], value['values'][1]), 2))

                    x.append({f'{obj[0]}, {obj[1]}, {obj[2]}'})
            objects.append(x)

        for i in range(n):
            t = threading.Thread(target=generate_object)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        end_time = time.perf_counter()
        f = open("TemaSBE/time_operations.txt", "a")
        f.write(f'Time to generate {n} subscriptions with threads :{end_time - start_time} \n')
        f.close()

        return objects
