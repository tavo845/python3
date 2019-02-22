METRO2 = 0.5

lar = float(input("ingrese el largo de la pared en metros cuadrados:. "))
ancho = float(input("ingrese el ancho de la puerta necesarios:. "))

tot1 = (lar * ancho)
tot2 = (tot1 * METRO2)
print("la cantidad de arena en metros cubicos es de:. {}".format(tot2))
