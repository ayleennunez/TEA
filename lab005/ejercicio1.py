try:
    file2read = input("ingrese nombre del archivo: ")
    fhandle = open(file2read, "r")
    for linea in fhandle:
        print(linea.upper())
except:
    print("Errir, archivo no ecnontrado.")

#print (fhandle.read().upper())