"""
def potencia (base, exponente):
    if exponente == 0:
        return 1
    else:
        return base *potencia(base, exponente-1)
base = int(input("Ingrese base: "))
exponente = int(input("Ingrese exponente: "))
print(potencia(base, exponente))
"""

print("======BIENVENIDO AL MENÚ======")
print("1. Calcular factorial")
print("2. Suma números naturales")
print("3. Calcular Fibonacci")
print("4. Calcular cantidad de letras")
print("5. Invertir cadena de texto")
print("6. Calcular potencia")
print("7. Salir")
print("Seleccione una opción")
opcion = input()
if opcion == "1":
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    n = int(input("Ingrese número: "))
    print(factorial(n))
elif opcion == "2":
    def naturales(num):
        if num == 0:
            return 1
        else:
            return num + naturales(num-1)
    num = int(input("Ingrese numero: "))
    print(naturales(num))