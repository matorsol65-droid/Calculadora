from suma import suma
from resta import resta

accion = input("Indica la operación que quieres hacer: ")

res = ""

if "+" in accion:
    res = suma(accion)
elif "-" in accion:
    res = resta(accion)

if res:
    print(res)
