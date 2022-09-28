# Tendencias e Innovación en Tecnología Agricola (TEA)
contador = 0
suma = 0
media = 0
primerNumero = True 
while True:
    try:
        numero = input("Ingrese un número: ")
        if (numero == "salir"):
            break
        else:
            contador = contador + 1
            suma = suma + int(numero)
            media = suma / contador

    except:
        print("Error, debe ingresar un número")
        contador = contador - 1
        continue
print("Contador:", contador)
print("Sumatoria: ", suma)
print("media: ", media)
