# Ejercicio Calculo de IMC

#En busca de mejorar la salud nutricional de los pacientes, se le solicita a 
# usted como programador el hecho de diseñar una herramienta que permita 
# determinar el estado nutricional de una persona

# W : corresponde al peso de la persona en Kg.
# H: corresponde a la altura en metros.
# IMC: EL valor del IMC, en [Kg/m2]


W = float(input("Digite su peso en kilogramos: "))
H_cm = float(input("Informe su altura en centímetros: "))

H = H_cm / 100
imc = W / (H * H)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("La clasificacion de la OMS es 'Bajo Peso'")
elif 18.5 <= imc < 25:
    print("La clasificacion de la OMS es 'Adecuado'")
elif 25 <= imc < 30:
    print("La clasificacion de la OMS es 'Sobrepeso'")
elif 30 <= imc < 35:
    print("La clasificacion de la OMS es 'Obesidad Grado I'")
elif 35 <= imc < 40:
    print("La clasificacion de la OMS es 'Obesidad Grado II'")
else:
    print("La clasificacion de la OMS es 'Obesidad Grado III'")