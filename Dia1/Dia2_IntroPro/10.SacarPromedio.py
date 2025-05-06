#Sacar el promedio de una lista de numeros
#Solicito la cantidad de numeros que habrá en la lista
CantNumeros = int(input("Ingrese la cantidad de numeros de la lista: "))

#Creamos un ciclo para ingresar la lista y calcular su promedio
Suma = 0 #Defino suma como cero para almacenar los numeros que se ingresen
for i in range(1,CantNumeros+1,1):
    Numero = int(input("Ingrese un numero a la lista: "))
    Suma = Suma + Numero

#Calculo y muestro el promedio
Promedio = Suma/CantNumeros
print(f"El promedio de los numeros enlistados es: {Promedio}")

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246

