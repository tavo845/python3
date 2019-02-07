## Gustavo Ramirez
##EJERCICO 4
## realizar el promedio de n notas utilizando el ford

valor = int(input("cuantas notas quieres ingresar"))
suma = 0
for i in range(valor): 
    nota = int(input("ingrese nota:"))
    suma = suma + int(nota)
    promedio = suma / nota
print("el promedio es:.{}".format(promedio))

