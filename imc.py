# Define una función para calcular el IMC (Índice de Masa Corporal)
def calcular_bmi(peso, altura_cm):

# Convertir la altura de centímetros a metros
    altura_m = altura_cm / 100
    
# Calcular el IMC
    bmi = peso / (altura_m ** 2)
    return bmi

# Define una función para clasificar el IMC según los estándares de la OMS
def clasificar_bmi(bmi):
    if bmi < 18.5:
        return "Bajo Peso"
    elif 18.5 <= bmi < 25:
        return "Adecuado"
    elif 25 <= bmi < 30:
        return "Sobrepeso"
    elif 30 <= bmi < 35:
        return "Obesidad Grado I"
    elif 35 <= bmi < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"
    
# Ingresar el peso y la altura
peso = float(input("Ingrese su peso en Kg: \n"))
altura_cm = float(input("Ingrese su talla (altura) en centímetros: \n"))

# Calcular el IMC
bmi = calcular_bmi(peso, altura_cm)

# Clasificar el IMC
clasificacion = clasificar_bmi(bmi)

# Imprimir los resultados
print(f"Su IMC es: {bmi:.2f}, lo que indica una clasificación de: {clasificacion}.")
