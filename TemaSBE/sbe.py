import publication as p
import subscription as s

f = open("TemaSBE/publicatii.txt", "w")
publicatii = p.Publication().generate_publications(1000)
for x in publicatii:
    f.write(f'{x} \n')
    # print(x)
f.close()

publicatii = p.Publication().generate_publications_thread(1000)

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

# f = open("TemaSBE/subscriptii.txt", "w")
# subscriptii = s.Subscription(subscription_frequency, subscription_operator_freq).generate_objects(10)
# for x in subscriptii:
#     for value in x:
#         if x.index(value) + 1 == len(x):
#             f.write(f'{value}')
#         else:
#             f.write(f'{value};')
#         # print(value, end = ';')
#     f.write('\n')
#     # print()
# f.close()
