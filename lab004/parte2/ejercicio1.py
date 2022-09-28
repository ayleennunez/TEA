# Tendencias e Innovación en Tecnología Agricola (TEA)
contador = 0
suma = 0
maximo = 0
minimo = 0
primerNumero = True 
while True:
    try:
        numero = input("Ingrese un número: ")
        if (numero == "salir"):
            break
        else:
            contador = contador + 1
            suma = suma + int(numero)
            
            if (primerNumero):
                minimo= int(numero)
                maximo= int(numero) 
                primerNumero = False
            else:
                if(int(numero) > maximo): maximo = int(numero) 
                if(int(numero) < minimo): minimo = int(numero)
    except:
        print("Error, debe ingresar un número")
        contador = contador - 1
        continue
print("Contador:", contador)
print("Sumatoria: ", suma)
print("maximo: ", maximo)
print("minimo: ", minimo)