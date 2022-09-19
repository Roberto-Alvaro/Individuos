from logging.handlers import BaseRotatingHandler
from os import remove
import random 
import math
from unicodedata import decimal
from xml.etree.ElementTree import C14NWriterTarget
import numpy as np
import matplotlib.pyplot as plt

def mostrador (binarioListaOrdenada):
    
    lista_mas_mejores = []
    print ("1. Cruce de un punto")
    print ("2. Cruce de dos puntos")
    print ("3. Cruce uniforme")
    print ("4. Salir")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        #Cruce de un punto
        contador2 = 1
        while(contador2 <= 200): # iteracciones con el codigo 
            contador2 = contador2 + 1
            
            binarioListaCruce = cruceIndividuos(binarioListaOrdenada)
            print("Lista nueva, por cruce de un punto: ", binarioListaCruce)

            binario_mutacion = mutacion(binarioListaCruce)
            print("Lista mutacion: ", binario_mutacion)

            binario_generacion = ordenamientoRuleta(binario_mutacion)
            print("Lista generacion de salida: ", binario_generacion)
            print("---------------------GENERACION",contador2-1,"---------------------")
            binarioListaOrdenada = binario_generacion

            for k in binarioListaOrdenada:
                numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
                for posicion, digito_string in enumerate(k[::-1]):
                    numero_decimal += int(digito_string) * 2 ** posicion
                    DR = convDR(numero_decimal,ristra,rangomin, rangomax)
                    RA = convRA(DR)
                print("Indivduo: ", "-------->", " Binario: ", k, " Decimal: ", numero_decimal, " Real: ", DR, " Adaptado: ", RA)
                if(funcion_max <= RA): #Valor de 584.6241
                    #Se agrega los mas mejores a la lista nueva, de los mas mejores
                    #se remueve el valor explorado que es el mas mejor con el remove
                    #se genera el numero binario nuevo, aleatorio
                    #se extiende la lista original, con el numero aleatorio
                    lista_mas_mejores.append(k)
                    binarioListaOrdenada.remove(k)#se remueve el valor igual
                    n = random.randint(0, 5000000)
                    binario = bin(n)[2:]
                    if len(str(binario)) == ristra: #Condiciona a la longitud del numero binario
                        binarioListaOrdenada.extend(binario)
            print("Lista, final de ordenamiento sin, el mas mejor: ", ordenamientoRuleta(binarioListaOrdenada))
        print("Lista de los mejores individuos", lista_mas_mejores)
    
    elif opcion == 2:
        #Cruce 2 puntos
        contador2 = 1
        while(contador2 <= 200): # iteracciones con el codigo 
            contador2 = contador2 + 1
            
            binarioListaCruce = cruceDosPuntos(binarioListaOrdenada)
            print("Lista nueva, por cruce de un punto: ", binarioListaCruce)

            binario_mutacion = mutacion(binarioListaCruce)
            print("Lista mutacion: ", binario_mutacion)

            binario_generacion = ordenamientoRuleta(binario_mutacion)
            print("Lista generacion de salida: ", binario_generacion)
            print("---------------------GENERACION",contador2-1,"---------------------")
            binarioListaOrdenada = binario_generacion

            for k in binarioListaOrdenada:
                numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
                for posicion, digito_string in enumerate(k[::-1]):
                    numero_decimal += int(digito_string) * 2 ** posicion
                    DR = convDR(numero_decimal,ristra,rangomin, rangomax)
                    RA = convRA(DR)
                print("Indivduo: ", "-------->", " Binario: ", k, " Decimal: ", numero_decimal, " Real: ", DR, " Adaptado: ", RA)
                if(funcion_max <= RA): #Valor de 584.6241
                    #Se agrega los mas mejores a la lista nueva, de los mas mejores
                    #se remueve el valor explorado que es el mas mejor con el remove
                    #se genera el numero binario nuevo, aleatorio
                    #se extiende la lista original, con el numero aleatorio
                    lista_mas_mejores.append(k)
                    binarioListaOrdenada.remove(k)#se remueve el valor igual
                    n = random.randint(0, 5000000)
                    binario = bin(n)[2:]
                    if len(str(binario)) == ristra: #Condiciona a la longitud del numero binario
                        binarioListaOrdenada.extend(binario)
            print("Lista, final de ordenamiento sin, el mas mejor: ", ordenamientoRuleta(binarioListaOrdenada))
        print("Lista de los mejores individuos", lista_mas_mejores)
    
    elif opcion == 3:
        print("Cruce uniforme")

    elif opcion == 4:
        print("Salio :v")

    else:
        print ("Introduce un numero entre 1 y 3")
    print ("Fin")

"""    #Cruce de dos puntos
    binarioListaCruce = cruceDosPuntos(binarioListaOrdenada)
    print("Lista nueva, por cruce de dos punto: ", binarioListaCruce)"""

def convBD(binaryLista):
    for i in binaryLista:
        numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
        for posicion, digito_string in enumerate(i[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        #print(f'El número decimal que buscamos es {numero_decimal}')
        return numero_decimal

    """lista_numeros = []
    for i in binaryLista:
        numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
        for posicion, digito_string in enumerate(i[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        #print(f'El número decimal que buscamos es')
        lista_numeros.append(numero_decimal)
    return lista_numeros"""
    
def convDR (numero, ristra, rangomin, rangomax):
    funcion = (rangomin+(numero*((rangomax-rangomin) / (2**ristra-1))))
    return funcion

def convRA(numero_real):
    funcion = ((5 * math.cos (numero_real)) + (2*(numero_real**2)) + (8))
    return funcion

def ordenamientoRuleta(binarioLista):
    #individuosAdaptados = np.array(individuosAdaptados)
    #npy = sorted(individuosAdaptados, reverse = True)
    #print("El ordenamiento es: ", npy)
    #numeros_ordenados = sorted([77, 22, 9, -6, 4000], reverse=True)
    #binarioLista = np.array(binarioLista)
    lista_orenada = sorted(binarioLista, reverse = True)
    #print("El ordenamiento es: ", npy2)

    return lista_orenada
    
def cruceIndividuos(binarioListaOrdenada):
    contador = 1
    punto = 4

    binarioListaOrdenada2 = []

    #binario = np.random.choice(cadenaBinaros, 2, False)
    print("----------------Cruce un punto-----------------")
    #cruces_num = input("introduce el numero de cruces")
    while (contador <= 5): #5 cruces por defecto
        print("cruce no.", "------>",  contador)
        padre1 = []
        padre2 = []
        padre1_nuevo = []
        padre2_nuevo = []
        hijo1 = []
        hijo2 = []
        hijo1_nuevo = []
        hijo2_nuevo = []
        hijo_mejor = []
        padre_peor = []

        print(binarioListaOrdenada)
        
        #for i in range(len(binaryLista)):
        #    i+1
        #while (contador < tasa ):
            #contador = contador + 1
        
        #escoje 2 elementos de la lista, esto de forma random
        padre1 = random.sample(list(binarioListaOrdenada), 1)
        padre2 = random.sample(list(binarioListaOrdenada), 1)

        #divide la lista original en varios caracteres
        for caracter in padre1[0]: #accedemos al elemento 0, para quitar la lista
            padre1_nuevo.append(caracter)
        #divide la lista original en varios caracteres
        for caracter in padre2[0]: #accedemos al elemento 0, para quitar la lista
            padre2_nuevo.append(caracter)
        print("Padre 1: ", padre1 , padre1_nuevo)
        print("Padre 2: ", padre2 , padre2_nuevo)

        #Supongamos que el punto de corte es el 4 ------> 1000 1000, se cuenta a la izquierda y se toma lo que contiene dentro del punto 4 hacia la izquierda del numero binario 
        #Cambio de ADN usando indices
        hijo1 = padre1_nuevo[:-4]
        #recorremos el padre usando el rango deceado para que comparta ADN al hijo contrario numerico
        for i in padre2_nuevo[5:]: #apartir del bit 4
            hijo1.append(i)
        #Cambio de ADN usando indices
        hijo2 = padre2_nuevo[:-4]
        #recorremos el padre usando el rango deceado para que comparta ADN al hijo contrario numerico
        for i in padre1_nuevo[5:]: #apartir del bit 4
            hijo2.append(i)

        #Volvemos a unir la lista
        hijo1_nuevo = [''.join(hijo1[0:])] #une la lista haciendo la hijos nuevos de un solo elemento
        hijo2_nuevo = [''.join(hijo2[0:])] #une la lista haciendo la hijos nuevos de un solo elemento

        #print("-----------Hijos nuevos-----------")
        print("Hijo1: " , hijo1_nuevo, hijo1)
        print("Hijo2: " , hijo2_nuevo, hijo2)

        #Empieza el calculo hijo 1 calculo de adaptativo
        numero_decimal = convBD(hijo1_nuevo)
        decimalReal = convDR(numero_decimal,ristra,rangomin, rangomax)
        realAdatado = convRA(decimalReal)
        #Empieza el calculo hijo 2 calculo de adaptativo
        numero_decimal2 = convBD(hijo2_nuevo)
        decimalReal2 = convDR(numero_decimal2,ristra,rangomin, rangomax)
        realAdatado2 = convRA(decimalReal2)

        #Empieza el calculo padre 1 calculo de adaptativo
        numero_decimal3 = convBD(padre1)
        decimalReal3 = convDR(numero_decimal3,ristra,rangomin, rangomax)
        realAdatado3 = convRA(decimalReal3)
        #Empieza el calculo padre 2 calculo de adaptativo
        numero_decimal4 = convBD(padre2)
        decimalReal4 = convDR(numero_decimal4,ristra,rangomin, rangomax)
        realAdatado4 = convRA(decimalReal4)

        print("valor padre1: ", realAdatado3)
        print("valor padre2: ", realAdatado4)
        print("valor hijo1: ", realAdatado)
        print("valor hijo2: ", realAdatado2)

        #Decide cual hijo evoluciono mejor
        if (realAdatado >= realAdatado2):
            print("hijo1 gano")
            hijo_mejor = hijo1_nuevo
        if (realAdatado < realAdatado2):
            print("hijo2 gano")
            hijo_mejor = hijo2_nuevo
        #Decide cual padre es el mas debil
        if (realAdatado3 >= realAdatado4):
            print("padre2 es mas debil")
            padre_peor = padre2
        if (realAdatado3 < realAdatado4):
            print("padre1 es mas debil")
            padre_peor = padre1

        print("Padre peor: ", padre_peor)
        print("Hijo mejor: ", hijo_mejor)

        #generar la lista resultante de los cambios del cruce
        binarioListaOrdenada_lista =  list(binarioListaOrdenada)#Convertimos a lista para que no nos de error
        for i in binarioListaOrdenada_lista:#recorremos uno a uno la primera lista
            if i==padre_peor[0]:#si un elemento de la lista primera es igual a un elemnto de la segunda lista....
                binarioListaOrdenada_lista.remove(i) #se remueve el valor igual
                binarioListaOrdenada_lista.extend(hijo_mejor)#se extiende la lista en la pocion desocupada con el valor del hijo mayor
        #print("Lista actualizada: ", binarioListaOrdenada_lista)
        binarioListaOrdenada = binarioListaOrdenada_lista
        contador = contador + 1
    return binarioListaOrdenada

def mutacion(binarioListaOrdenada):
    print("----------------Mutacion-----------------")
    mutado = []
    mutado_nuevo = []
    mutado_nuevo_unido = []
    #bit_mutado = int(input("Ingresa el bit que quieres cambiar: ")) 
    bit_mutado = 5
    mutado = random.sample(list(binarioListaOrdenada), 1)
    print(mutado)
    for caracter in mutado[0]: #accedemos al elemento 0, para quitar la lista
        mutado_nuevo.append(caracter)
    print(mutado_nuevo)
    
    for i in range(len(mutado_nuevo)): #Recorremos la lista por longitud
        #print(i+1)
        if (i+1 == bit_mutado): #Cuando el valor de mutacion se paresca a i hacemos el cambio en el respectivo indice
            #print(i)
            if(mutado_nuevo[i] == '0'): #Si el valor es 0 se cambia a 1
                mutado_nuevo[i] = 1
            else: #Si es 1 se queda tal cual 
                mutado_nuevo[i] = 0
    print("Ya esta mutado: ", mutado_nuevo)
    mutado_nuevo_unido = [''.join(map(str, mutado_nuevo[0:]))] #une la lista haciendo la hijos nuevos de un solo elemento
    print(mutado_nuevo_unido)

    #generar la lista resultante de los cambios de la mutacion
    print("Lista sin mutar", binarioListaOrdenada)
    #binarioListaOrdenada_lista =  binarioListaOrdenada.tolist() #Convertimos a lista para que no nos de error
    for i in binarioListaOrdenada:#recorremos uno a uno la primera lista
        if i==mutado[0]:#si un elemento de la lista primera es igual a un elemnto de la segunda lista....
            binarioListaOrdenada.remove(i)#se remueve el valor igual
            binarioListaOrdenada.extend(mutado_nuevo_unido)#se extiende la lista en la pocion desocupada con el valor del hijo mayor
            binarioListaFinal = binarioListaOrdenada
    #print("Lista actualizada: ", binarioListaFinal)
    return binarioListaFinal

def cruceDosPuntos(binarioListaOrdenada):
    contador = 1
    punto = 4

    print("----------------Cruce dos puntos-----------------")
    while (contador <= 5): #5 cruces por defecto
        print("cruce no.", "------>",  contador)
        print(binarioListaOrdenada)
        
        padre1 = []
        padre2 = []
        padre1_nuevo = []
        padre2_nuevo = []
        hijo1 = []
        hijo2 = []
        hijo1_nuevo = []
        hijo2_nuevo = []
        hijo_mejor = []
        padre_peor = []
        binarioListaOrdenada2 = []

        #for i in range(len(binaryLista)):
        #    i+1
        #while (contador < tasa ):
            #contador = contador + 1
        
        #escoje 2 elementos de la lista, esto de forma random
        padre1 = random.sample(list(binarioListaOrdenada), 1)
        padre2 = random.sample(list(binarioListaOrdenada), 1)

        #divide la lista original en varios caracteres
        for caracter in padre1[0]: #accedemos al elemento 0, para quitar la lista
            padre1_nuevo.append(caracter)
        #divide la lista original en varios caracteres
        for caracter in padre2[0]: #accedemos al elemento 0, para quitar la lista
            padre2_nuevo.append(caracter)

        print("Padre 1: ", padre1 , padre1_nuevo)
        print("Padre 2: ", padre2 , padre2_nuevo)

        """#Cambio de ADN usando indices
        hijo1 = padre1_nuevo[:-4]
        #recorremos el padre usando el rango deceado para que comparta ADN al hijo contrario numerico
        for i in padre2_nuevo[5:]: #apartir del bit 4
            hijo1.append(i)
        #Cambio de ADN usando indices
        hijo2 = padre2_nuevo[:-4]
        #recorremos el padre usando el rango deceado para que comparta ADN al hijo contrario numerico
        for i in padre1_nuevo[5:]: #apartir del bit 4
            hijo2.append(i)"""

        hijo1 = padre1_nuevo[0:4] + padre2_nuevo[-5:-2] + padre1_nuevo[-2:] #Corta del bit 6 al final, de ahi lo suma, del 3 al 5, suma las ultimas dos posiciones 
        #corte de 3-5, con una longitud de 9 de ristra
        hijo2 = padre2_nuevo[0:4] + padre1_nuevo[-5:-2] + padre2_nuevo[-2:] #Corta del bit 6 al final, de ahi lo suma, del 3 al 5, suma las ultimas dos posiciones 
        #corte de 3-5, con una longitud de 9 de ristra

        #Volvemos a unir la lista
        hijo1_nuevo = [''.join(hijo1[0:])] #une la lista haciendo la hijos nuevos de un solo elemento
        hijo2_nuevo = [''.join(hijo2[0:])] #une la lista haciendo la hijos nuevos de un solo elemento

        #print("-----------Hijos nuevos-----------")
        print("Hijo1: " , hijo1_nuevo, hijo1)
        print("Hijo2: " , hijo2_nuevo, hijo2)

        #Empieza el calculo hijo 1 calculo de adaptativo
        numero_decimal = convBD(hijo1_nuevo)
        decimalReal = convDR(numero_decimal,ristra,rangomin, rangomax)
        realAdatado = convRA(decimalReal)
        #Empieza el calculo hijo 2 calculo de adaptativo
        numero_decimal2 = convBD(hijo2_nuevo)
        decimalReal2 = convDR(numero_decimal2,ristra,rangomin, rangomax)
        realAdatado2 = convRA(decimalReal2)

        #Empieza el calculo padre 1 calculo de adaptativo
        numero_decimal3 = convBD(padre1)
        decimalReal3 = convDR(numero_decimal3,ristra,rangomin, rangomax)
        realAdatado3 = convRA(decimalReal3)
        #Empieza el calculo padre 2 calculo de adaptativo
        numero_decimal4 = convBD(padre2)
        decimalReal4 = convDR(numero_decimal4,ristra,rangomin, rangomax)
        realAdatado4 = convRA(decimalReal4)

        print("valor padre1: ", realAdatado3)
        print("valor padre2: ", realAdatado4)
        print("valor hijo1: ", realAdatado)
        print("valor hijo2: ", realAdatado2)

        #Decide cual hijo evoluciono mejor
        if (realAdatado >= realAdatado2):
            print("hijo1 gano")
            hijo_mejor = hijo1_nuevo
        if (realAdatado < realAdatado2):
            print("hijo2 gano")
            hijo_mejor = hijo2_nuevo
        #Decide cual padre es el mas debil
        if (realAdatado3 >= realAdatado4):
            print("padre2 es mas debil")
            padre_peor = padre2
        if (realAdatado3 < realAdatado4):
            print("padre1 es mas debil")
            padre_peor = padre1

        print("Padre peor: ", padre_peor)
        print("Hijo mejor: ", hijo_mejor)

        #generar la lista resultante de los cambios del cruce
        binarioListaOrdenada_lista =  list(binarioListaOrdenada) #Convertimos a lista para que no nos de error
        for i in binarioListaOrdenada_lista:#recorremos uno a uno la primera lista
            if i==padre_peor[0]:#si un elemento de la lista primera es igual a un elemnto de la segunda lista....
                binarioListaOrdenada_lista.remove(i)#se remueve el valor igual
                binarioListaOrdenada_lista.extend(hijo_mejor)#se extiende la lista en la pocion desocupada con el valor del hijo mayor
        #print("Lista actualizada: ", binarioListaOrdenada_lista)
        contador = contador + 1
    return binarioListaOrdenada_lista

"""" 
point = 0
    father = []
    for i in range(len(binarioListaOrdenada)):
        point = np.random.randint(1, ristra)
        father = random.sample(list(binarioListaOrdenada), 2)
        
        my_list = list(binarioListaOrdenada)
        my_list[i][:point] = father[0][:point]
        my_list[i][point:] = father[1][point:]
    
    print(my_list)


    for i in padre1[4:]:
        print(i)
    

        #punto = np.random.randint(4,ristra)
        #father = random.sample(binarioListaOrdenada, 2)

        #binarioListaOrdenada[contador][:punto] = father [0][:punto]
        #binarioListaOrdenada[contador][punto:] = father [1][punto:]
        #print (binarioListaOrdenada)


        point = 0
    father = []

    for i in range(len(binaryLista)):
        point = np.random.randint(1,ristra)
        father = random.sample(binarioListaOrdenada, 2)

        binaryLista[i][:point] = father[0][:point]
        binaryLista[i][point:] = father[1][point:]       
"""

poblacion = int(input("Ingrese poblacion: "))
ristra = int(input("Ingrese longitud de la ristra: "))
#porcentaje = int(input("Ingrese porcentaje de la tasa propuesta: "))

rangomin = int(input("Ingrese longitud de rangomin (2): "))
rangomax = int(input("Ingrese longitud de rangomax (17): "))
funcion_min = ((5 * math.cos (rangomin)) + (2*(rangomin**2)) + (8)) #funcion que depende del problema
funcion_max = ((5 * math.cos (rangomax)) + (2*(rangomax**2)) + (8))
print(f"Valor de la funcion-min : [{funcion_min}]")
print(f"Valor de la funcion-max : [{funcion_max}]")
#print(f"Valor de la ristra : [{ristra}]")
#tasa =  round((porcentaje * poblacion) / 100)
#print(tasa)
contador = 0
binaryLista = []
individuosAdaptados = []
binarioListaOrdenada = []
binarioListaCruce = []
binario_mutacion = []
binario_generacion = []

while(contador < poblacion):
    n = random.randint(0, 5000000)
    binary = bin(n)[2:]
    if len(str(binary)) == ristra:
        contador = contador + 1
        DR = convDR(n,ristra,rangomin, rangomax)
        RA = convRA(DR)
        print("Indivduo: ", "-------->", " Binario: ", binary, " Decimal: ", n, " Real: ", DR, " Adaptado: ", RA)
        individuosAdaptados.append(round(RA))
        binaryLista.append(binary)
    
binarioListaOrdenada = ordenamientoRuleta(binaryLista)
print("Lista ordenada: ", binarioListaOrdenada)

mostrador(binarioListaOrdenada)
