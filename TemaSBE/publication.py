#clasa de publicatii
import random
import time
import threading

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

    def generate_publications(self, n):
        start_time = time.perf_counter()
        objects = []
        for i in range(n):
            object = {}
            for key, value in self.publication_structure.items():
                type_, choices = value
                if type_ == int:
                    object[key] = random.randint(*choices)
                elif type_ == float:
                    object[key] = round(random.uniform(*choices), 2)
                elif type_ == str:
                    object[key] = random.choice(choices)
                else:
                    raise ValueError(f"Unsupported type {type_}")
            objects.append(object)
        end_time = time.perf_counter()
        f = open("TemaSBE/time_operations.txt", "a")
        f.write(f'Time to generate {n} publications without threads :{end_time - start_time} \n')
        f.close()
        return objects
    
    def generate_publications_thread(self, n):
        start_time = time.perf_counter()
        objects = []
        threads = []

        for i in range(n):
            thread = threading.Thread(target=self.generate_publication, args=(objects,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        end_time = time.perf_counter()
        f = open("TemaSBE/time_operations.txt", "a")
        f.write(f'Time to generate {n} publications with threads :{end_time - start_time} \n')
        f.close()

        return objects

    def generate_publication(self, objects):
        object = {}
        for key, value in self.publication_structure.items():
            type_, choices = value
            if type_ == int:
                object[key] = random.randint(*choices)
            elif type_ == float:
                object[key] = round(random.uniform(*choices), 2)
            elif type_ == str:
                object[key] = random.choice(choices)
            else:
                raise ValueError(f"Unsupported type {type_}")
        objects.append(object)
  
    def __str__(self):
        return f"({self.stationid}, {self.city}, {self.temp}, {self.rain}, {self.wind}, {self.direction}, {self.date})"

