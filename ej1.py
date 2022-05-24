print("Hello world")

def sueldo(cargo):
    dinero = 0
    if "Ejecutivo" == cargo:
        dinero = 90
    if "Jefe" == cargo:
        dinero = 100
    if "Externo" == cargo:
        dinero = 50
    return dinero

print(sueldo("Jefe"))