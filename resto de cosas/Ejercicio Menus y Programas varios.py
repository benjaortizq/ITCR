def menuPrincipal () :
    return 












#Programa  1 
#calcular cual es la potencia de 10 ams cercana a un numero. si esta a la misama distancia de 2 potencias de 10 , devolver la que es menor 

# #E : Un numero positivo 
#S : una potencia de 10 . 
#R : numeros negativos . 

def potenciaMasCercana (numero) :

    exponente_diez=0 
    while numero > 10** exponente_diez : 
        exponente_diez+=1 
    potencia_inmediata = 10 ** exponente_diez
    potencia_anterior = 10 ** ( exponente_diez-1 )
    if ( numero - potencia_anterior) <= (potencia_inmediata - numero ) : 
        return potencia_anterior
    return  potencia_inmediata


#
print( potenciaMasCercana (1.3))

def menuPotenciaMasCercana () : 
    print (" 1. **********POTENCIA MAS CERCANA A UN NUMERO **********")
    numero_para_potencia = input ("Ingrese un numero positivo  a continuacion :   ")
    try : 
        print ("La potencia mas cercana del numero ", numero_para_potencia , "es : " ,potenciaMasCercana (numero_para_potencia) )
    except : 
       print ( "Error en uno de los parametros : \n -- Solo se permiten numeros positivos. ")    



#Programa que retorne la cantiad de digitos decimales de de un numero positivo entero 
#E : un numero decimal entero positivo 
#S : la cantidad de digitos decimales que tiene el numero (osea la cantidad de digitos supongo yo )
# R : solo numeros positivos enteros 
def cantidadDecimales (numero) : 
    contador = 0 
    while numero > 0 : 
        numero //= 10 
        contador+=1
    return contador 
print (cantidadDecimales(0)) #en menu verificar con resultado . 
print (cantidadDecimales(1123))

def menuCantidadDecimales () : 
    print (" 2. ********** CANTIDAD DE DECIMALES DE UN NUMERO ********** ") 
    numero_para_contar = input ("Ingrese el numero entero positivo  que desea saber la cantidad de decimales : ")
    try : 
       numero_para_contar = int(numero_para_contar)
       if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("La cantidad de decimales del numero ", numero_para_contar, "es : ", cantidadDecimales (numero_para_contar ) )
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros ")

menuCantidadDecimales () 

# 3 . digitos diferentes 
#e : Un numero 
#s : cantidad de digitos diferentes que tiene el numero 
# r : Solo numeros enteros positivos decimales 

def cantidadDigitosDiferentes ( numero ) : 
    cantidad_diferentes = 0 
    digito_anterior = numero % 10  
    digito_actual = 0
    while numero > 0 : 
        numero//=10 
        digito_actual = numero % 10 
        if digito_actual != digito_anterior : 
            cantidad_diferentes +=1 
        digito_anterior= digito_actual
    return cantidad_diferentes
        
print (cantidadDigitosDiferentes(1030211))
