moneda1 = 0
moneda2 = 0
moneda3 = 0
moneda4 = 0
moneda5 = 0
moneda6 = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total = 0

moneda1 =int(input("ingrese monedas de 5:. "))
total1 = moneda1 * 0.05
moneda2 =int(input("ingrese monedas de 10:. "))
total2 = moneda2 * 0.10
moneda3 =int(input("ingrese monedas de 12,5:. "))
total3 = moneda3 * 0.125
moneda4 =int(input("ingrese monedas de 25:. "))
total4 = moneda4 * 0.25
moneda5 =int(input("ingrese monedas de 50:. "))
total5 = moneda5 * 0.50
moneda6 =int(input("ingrese monedas de 1 Bolivar:. "))
total6 = moneda6 * 1

total = total1 + total2 + total3 + total4 + total5 + total6
print("La cantidad total de dinero que se tiene es de:.",total)
