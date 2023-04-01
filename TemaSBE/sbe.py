import publication as p
import subscription as s

publicatii = p.Publication().generate_publications(200)
for x in publicatii:
    print(x, "\n")

subscription_frequency = {
    "city": {"frequency": 0.9, 'display': 0},
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

subscriptii = s.Subscription(subscription_frequency, subscription_operator_freq).generate_objects(200)
for x in subscriptii:
    for value in x:
        print(value, end = ';')
    print()
