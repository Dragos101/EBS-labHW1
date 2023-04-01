import publication as p
import subscription as s
  
publicatie = p.Publication(2,"Pascani", 12, 0.8, 3.5, "NE", "25.03.2023")
subscriptie = s.Subscription("Pascani", 12, 0.8, 3.5, "NE", "25.03.2023")
print(publicatie)
print("\n", subscriptie)

#exemplu pentru nerespectarea constrangerilor
#p = s.Publication(101, "Iasi", -5, 0.5, 40, "N", "5.01.2023")