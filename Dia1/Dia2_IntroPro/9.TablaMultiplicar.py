#Tabla de Multiplicar
#Solicitamos el numero para generar su tabla de multiplicar
Numerito = int(input("Ingrese un numero: "))

#Empezamos el ciclo de multiplicacion
for i in range(1,10+1,1):
    Resultado = Numerito * i
    print(f"{Numerito} x {i} = {Resultado}") #Imprimo el resultado de manera bonita

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246
