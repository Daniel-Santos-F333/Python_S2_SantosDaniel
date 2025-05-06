#Determinar numero mayor de tres numeros
#Saludamos al usuario y le solicitamos 3 numeros
print("Bienvenido al programa para hallar el mayor de tres numeros")
Numero1 = int(input("Ingrese por favor un numero: "))
Numero2 = int(input("Ingrese por favor un numero: "))
Numero3 = int(input("Ingrese por favor un numero: "))

#Comenzamos el proceso para determinar cual de los tres numeros ingresados es el mayor
if Numero1>=Numero2 and Numero1>=Numero3:
    Mayor=Numero1
else:
    if Numero2>=Numero1 and Numero2>=Numero3:
        Mayor=Numero2
    else:
        Mayor=Numero3
        
#Mostramos el resultado
print(f"El numero mayor entre {Numero1}, {Numero2} y {Numero3} es: {Mayor}")

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246

       