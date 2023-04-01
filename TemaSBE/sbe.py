import publication as p
import subscription as s
  
# subscriptie = s.Subscription("Pascani", 12, 0.8, 3.5, "NE", "25.03.2023")
# print("\n", subscriptie)

# publicatie = p.Publication()
# print(publicatie)

subscription_frequency = {
    "city": {"frequency": 0.9, 'display': 0},
    "temp": {"frequency": 0.5, 'display': 0},
    "rain": {"frequency": 0.3, 'display': 0},
    "wind": {"frequency": 0.8, 'display': 0},
    "direction": {"frequency": 0, 'display': 0},
    "date": {"frequency": 0.8, 'display': 0}
}

subscriptii = s.Subscription(subscription_frequency).generate_objects(10)
for x in subscriptii:
    print(x, "\n")
