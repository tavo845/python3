HORAS = 3600
MINUTOS = 60
SEGUNDOS = 0.25
menu = int(input("1.tiempo en horas  2.tiempo en minutos  3.tiempo en segundos"))
if menu == 1:
    horas = int(input("Ingrese cuantas horas necesita:. "))
    tiempo = horas * HORAS
    total = tiempo * SEGUNDOS
    print("El total a pagar por el tiempo es:.{}".format(total))
elif menu == 2:
    minutos = int(input("ingrese cuantos minutos nececesita:. "))
    tiempo = minutos * MINUTOS
    total = tiempo * SEGUNDOS
    print("El total a pagar por el tiempo es{}".format(total))
if menu == 3:
    segundos = int(input("Ingrese cuanto segundos necesita:. "))
    total = segundos * SEGUNDOS
    print("El total a pagar por el tiempo es de:.{}".format(total))
                 
