def calificacionNotas(grade):
    if (grade >= 0.9 and grade <=1.0):
        return  "Sobresaliente"
    elif (grade >=0.8 and grade <0.9):
        return  "Notable"
    elif (grade >=0.7 and grade <0.8):
        return  "Buena"
    elif (grade >=0.7 and grade <0.6):
        return  "Suficiente"
    elif (grade <=0.6):
        return  "Insuficiente"
    else:
        grade < 0.0 and grade >1.0
        print("Error, introduce un número válido entre 0.0 y 1.0.")

calificacionNotas: float(input("Ingrese su nota: "))
print("Su calificacion es: ", grade ) 