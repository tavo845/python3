##Gustavo Ramirez

##EJERCICIO 1
##que seleccione una opcion op.1 solicitar dos numeros y elevar el primer numero
##al segundo numero op2. solicitar tres numeros y elevar el primero al segumdo
##y el resultado elevarlo al tercero


print("elevacon de numeros seleccione opcion 1 - opcion 2".center(50,"*"))
opcion = input(":.")
if opcion == "1":
      numero1 = input("ingresa primer valor")
      numero2 = input("ingresa segundo valor")
      elevacion = int(numero1) ** int(numero2)
      print("la elevacion es:.{}".format(elevacion))
elif opcion == "2":
     numero1 = input("ingresa primer valor")
     numero2 = input("ingresa segundo valor")
     numero3 = input("ingresa tercer valor")
     elevacion = int(numero1) ** int(numero2) ** int(numero3)
     print("la elevacion es:.{}".format(elevacion))
