print("Conversor de Números")

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