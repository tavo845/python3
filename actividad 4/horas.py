va = 0
h = 0
h_e = 0
valor_horas = int(input("Valor de las horas"))
hora = int(input("Horas trabajadas"))
hora_extra = int(input("Horas extras laboradas"))
va = int(valor_horas) * int(hora)
h = int(valor_horas) * int(hora_extra) *int(2)
h_e = int(valor_horas) + int(valor_horas) * int(hora_extra) * int(2)
print("Su sueldo normal es:.{}".format(va))
print("Su sueldo extra es:.{}".format(h))
print("el total es:.{}".format(h_e))
