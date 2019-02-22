INCREMENTO = 0.8
DESCUENTO = 0.25
aumento = 0
suma = 0
descuento = 0
total = 0
sueldo = int(input("ingrese su sueldo actual:."))
aumento = sueldo * INCREMENTO
suma = aumento + sueldo
descuento = suma + DESCUENTO
totl = suma - descuento
print("Su sueldo nuevo es de:.{}".format(aumento))
