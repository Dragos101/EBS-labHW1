import publication as p
import subscription as s
  
# subscriptie = s.Subscription("Pascani", 12, 0.8, 3.5, "NE", "25.03.2023")
# print("\n", subscriptie)

# publicatie = p.Publication()
# print(publicatie)

subscriptii = s.Subscription().generate_objects(10)
for x in subscriptii:
    print(x, "\n")
