# Tendencias e Innovación en Tecnología Agricola (TEA)
def calcularSalario (horas, tarifa):
    HORAS_SEMANALES = 40
    horas_extra = 0
    if (horas > HORAS_SEMANALES): 
        horas_extra = horas - HORAS_SEMANALES
        calculo = (HORAS_SEMANALES * tarifa) + (horas_extra * (tarifa*1.5))
    else:
        calculo = (horas * tarifa) / 0
    return calculo

try:
    horas = int (input("Ingrese número de horas trabajadas: "))
    tarifa = float(input("Ingrese tarifa por horas:"))
    salario = calcularSalario (horas, tarifa)
    print("Salario: ", salario)

except:
    print("Error, ingresar un valor numérico")