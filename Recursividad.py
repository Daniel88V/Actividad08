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
            return 0
        else:
            return num + naturales(num-1)
    num = int(input("Ingrese numero: "))
    print(naturales(num))
elif opcion == "3":
    print("Código en proceso...")
elif opcion == "4":
    def conteo(letra, palabra):
        if not palabra:
            return 0
        if palabra[0].lower() == letra.lower():
            return 1 + conteo(letra, palabra[1:])
        else:
            return conteo(letra, palabra[1:])
    palabra = input("Ingrese palabra: ")
    while True:
        letra = input("Ingrese letra: ")
        if len(letra) == 1:
            break
        else:
            print("Error, por favor ingresa una sola letra")
    cantidad = conteo(letra, palabra)
    print(f"La cantidad de veces que la letra {letra} aparece en la palabra {palabra} es: {cantidad}")
elif opcion == "5":
    def invertida(inversion):
        if len(inversion) <= 1:
            return inversion
        else:
            return inversion[-1] + invertida(inversion[:-1])
    inversion = input("Ingrese la palabra que desea invertir: ")
    palabra_invertida = invertida(inversion)
    print(f"La palabra {inversion} de forma invertida es: {palabra_invertida}")
elif opcion == "6":
    def potencia(base, exponente):
        if exponente == 0:
            return 1
        else:
            return base * potencia(base, exponente - 1)
    base = int(input("Ingrese base: "))
    exponente = int(input("Ingrese exponente: "))
    print(potencia(base, exponente))
elif opcion == "7":
    print("Saliendo del menú...")
    exit()