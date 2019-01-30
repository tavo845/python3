## Gustavo Ramirez
## calcular la edad actual de una persona, prviamente ingresado el año actual
## y el año de nacimiento
print("Binvenido al prgrama".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingresar tu año de nacimiento"))
edad = FEC_ACT - fec_nac
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
#print("tu edad es{}".format(edad))
