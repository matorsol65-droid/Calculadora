from suma import suma
from resta import resta

accion = input("Indica la operación que quieres hacer: ")
comprobante = false
res = float()

if "+" in accion:
    comprobante = True
    res = suma(accion)
elif "-" in accion:
    comprobante = True
    res = resta(accion)

if comprobante:
    print(res)
