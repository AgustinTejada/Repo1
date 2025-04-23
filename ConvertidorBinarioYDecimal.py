print("Conversor de Números")

print("\nMenú de opciones:")
print("1. Convertir Decimal a Binario")
print("2. Convertir Binario a Decimal")

opcion = input("Selecciona una opción (1-2): ")

if opcion == "1":
    entrada = int(input("Ingresa un número decimal: "))

    # Validación: verificar que sea un número positivo
    if entrada >= 0: 
        numero = entrada 
        if numero == 0:
            print("El número en binario es: 0")
        else:
            binario = ""
            while numero > 0:
                if numero % 2 == 0:
                    binario = "0" + binario 
                else:
                    binario = "1" + binario 
                numero = numero // 2 
            print("El número en binario es: ", binario)
    else:
        print("El número no se puede convertir")


elif opcion == "2":
    binario = input("Ingresa un número binario (solo 0 y 1): ")
    es_valido = True

    for digito in binario:
        if digito != "0" and digito != "1":
            es_valido = False
            break

    if es_valido:
        decimal = 0
        longitud = len(binario)
        for i in range(longitud):
            bit = int(binario[longitud - 1 - i])
            decimal = decimal + bit * (2 ** i)
        print("El número en decimal es:", decimal)
    else:
        print("Error: Solo se permiten dígitos 0 y 1.")
else:
    print("Opción inválida. Intenta nuevamente.")
