#Generar la serie de fibonacci
#Solicitamos al usuario cuantos numeros de la serie fibonacci desea ver
Num = int(input("¿Cuantos numeros de la serie fibonacci deseas ver?: "))

#Establezco los dos primeros terminos de la serie
a = 0
b = 1

#Verifico si el numero ingresado es correcto y empiezo la serie
if Num <= 0:
    print("El numero ingresado no sirve para generar la serie")
else:
    print("Serie de Fibonacci: ")
    for i in range(Num):
        print (a)
        a, b = b, a + b 

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246




        