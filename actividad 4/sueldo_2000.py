print("Su sueldo al mes es de:. 2500".center(50,"*"))
sueldo = 2500
comicion = 0.10
ventas = 3
precio_de_ventas = int(input("ingrese precio de venta:."))
total_de_comision = (ventas * precio_de_ventas) * comicion
total = sueldo + total_de_comision
print("El total de comision es:.{}".format(total_de_comision))
print("El total del mes es:.{}".format(total))
