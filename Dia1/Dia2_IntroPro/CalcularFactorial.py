#saludamos al usuario y le solicitamos ingresar el numero del que desea conocer su factorial
print("Bienvenido, al programa CalcularFactorial")
NumFactorial= int(input("Por favor ingrese un numero del que desee saber cual es su factorial: "))
Factorial = 1
#Usamos un Ciclo for para calcular el factorial
for i in range(1,NumFactorial+1,1):
    Factorial=Factorial*i

#Imprimimos el resultado
print(f"El factorial de {NumFactorial} es: {Factorial}")

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246
