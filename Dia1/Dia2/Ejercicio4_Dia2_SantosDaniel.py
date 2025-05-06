# ##########################
# #### Clase Dia 2 ######
# ##########################

#Saber si un numero es primo
#Solicitamos un numero al usuario

Numero = int(input("Ingrese un numero: "))
Primo = False
#Verifico si el numero ingresado es primo
if Numero <= 1:
    Primo = False
else:
    Primo = True 

    #Verifico si no tiene divisores
    for i in range(2,Numero):
        if Numero % i == 0:
            Primo = False

#Mostramos el resultado
if Primo:
    print("El numero es primo")
else:
    print("El numero no es primo")

#Desarrollado por: Daniel Santos Fajardo - C.C. 1.005.331.246
