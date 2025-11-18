
def doble_factorial(n):
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 2
    return resultado

try:
    numero=int(input("Ingresa un número:"))

    if numero < 0:
        raise Exception("El número no puede ser negativo")

    res = doble_factorial(numero)
    print("El doble factorial es:", res)

except ValueError:
    print(" Error: No ingresaste un número válido ")

except Exception as e:
    print("Ocurrió un error:", e)
