## Gustavo Ramirez
##EJRCICIO 3
##realizar el promedo de 5 notas utilizando el ciclo for

print("Bienvenido al promediador 3000 XD".center(50,"*"))
promedio = 0
for i in range (5):
    nota = int (input("ingrese nota"))
    promedio = promedio + nota
    division = promedio / 5
print("el promedio es:.{}".format(division))
