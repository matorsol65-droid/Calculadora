from suma import suma
from resta import resta

accion = input("Indica la operación que quieres hacer: ")
comprobante = false
res = float()

if "+" in accion and "-" not in accion:
    comprobante = True
    res = suma(accion)
elif "-" in accion and "+" not in accion:
    comprobante = True
    res = resta(accion)
elif:

if comprobante:
    print(res)
