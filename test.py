from vecteur import V2,V3


# Test
v2_1 = V2(1, 2)
v2_2 = V2(6, 7)

print("Les objets de V2 :\n")
v2_1.out()
v2_2.out()

print("La norme de V2:", v2_1.Norme())
print("Count:", V2._count)

v3_1 = V3(1, 2, 3)
v3_2 = V3(5, 6, 7)

print("\nLes objets de V3 :\n")
v3_1.out()
v3_2.out()

print("La norme de V3 : ", v3_1.Norme())
print("Count = ", V3._count)
