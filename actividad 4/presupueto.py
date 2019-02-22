URGENCIA = 0.37
PEDIATRIA = 0.42
TRAUMATOLOGIA = 0.21
print("desea calcular presupuesto")
salida = input("ingresa presupuesto 1-si \n 2-no")
while salida != 2:
    presupuesto = int(input("Ingrese cantidad:."))
    print("la cantidad em Urgencia es:.{}".format(presupuesto *URGENCIA))
    print("la cantidad en Pediatria es:.{}".format(presupuesto *PEDIATRIA))
    print("la cantidad en Traumatologia es:.{}".format(presupuesto *TRAUMATOLOGIA))
    salida = input("ingresa presupuesto 1-si \n 2-no")
print("gracias por su ayuda")
