def menuPrincipal () :
    while True : 
        print ("MENU 31 EJERCICIOS : ")
        opcion = input("Escriba una opción: ")

        if opcion.lower() == "salir":
            print("Saliendo del programa. 👋")
            break

        try:
            opcion = int(opcion)
            if opcion == 0 :
                menuPrincipalCompleto()
            if opcion == 1:
                menuPotenciaMasCercana()
            elif opcion == 2:
                menuCantidadDecimales()
            elif opcion == 3:
                menucuentaDigitosDiferentes()
            elif opcion == 4:
                menuNumeroPalindromo()
            elif opcion == 5:
                menuDivisionTruncada()
            elif opcion == 6:
                menuOcurreEn()
            elif opcion == 7:
                menuOcurreEn2()
            elif opcion == 8:
                menuMayorDigito()
            elif opcion == 9:
                menuOcurreMas()
            elif opcion == 10:
                menuAgregarDigito()
            elif opcion == 11:
                menuDivisionResiduo()
            elif opcion == 12:
                menuSuprimirDigito()
            elif opcion == 13:
                menuesPrimoPalindromo()
            elif opcion == 14:
                menuCuadradoPerfecto()
            elif opcion == 15:
                menuSumaFraccionesPatron()
            elif opcion == 16:
                menuSumayRestaFraccionesPatron()
            elif opcion == 17:
                menuAnoDesdeMilNueveOchenta()
            elif opcion == 18:
                menuSumaPares()
            elif opcion == 19:
                menuNacioBiciestto()
            elif opcion == 20:
                menuCantidadCuadrados()
            elif opcion == 21:
                menuPrimoProximo()
            elif opcion == 22:
                menuCantidadPalindromosAnteriores()
            elif opcion == 23:
                menuCuantosCuadradosEntre()
            elif opcion == 24:
                menufuncionTruncate()
            elif opcion == 25:
                menuMenoresANumeroFib()
            elif opcion == 26:
                menuMenoresFibonacciPar()
            elif opcion == 27:
                menuRedondeo()
            elif opcion == 28:
                cantidadPrimosRango()
            elif opcion == 29:
                menuSumaCuadradosMayorA()
            elif opcion == 30:
                menuSumaPrimosMayorA()
            else:
                print("❌ Opción inválida. Ingrese un número entre 1 y 30.")
        except:
            print("❌ Error: Ingrese un número válido o 'salir' para terminar.") 

def menuPrincipalCompleto () :

    print("\n====== MENÚ PRINCIPAL ======")
    print("1. menuPotenciaMasCercana")
    print("2. menuCantidadDecimales")
    print("3. menucuentaDigitosDiferentes")
    print("4. menuNumeroPalindromo")
    print("5. menuDivisionTruncada")
    print("6. menuOcurreEn")
    print("7. menuOcurreEn2")
    print("8. menuMayorDigito")
    print("9. menuOcurreMas")
    print("10. menuAgregarDigito")
    print("11. menuDivisionResiduo")
    print("12. menuSuprimirDigito")
    print("13. menuesPrimoPalindromo")
    print("14. menuCuadradoPerfecto")
    print("15. menuSumaFraccionesPatron")
    print("16. menuSumayRestaFraccionesPatron")
    print("17. menuAnoDesdeMilNueveOchenta")
    print("18. menuSumaPares")
    print("19. menuNacioBiciestto")
    print("20. menuCantidadCuadrados")
    print("21. menuPrimoProximo")
    print("22. menuCantidadPalindromosAnteriores")
    print("23. menuCuantosCuadradosEntre")
    print("24. menufuncionTruncate")
    print("25. menuMenoresANumeroFib")
    print("26. menuMenoresFibonacciPar")
    print("27. menuRedondeo")
    print("28. cantidadPrimosRango")
    print("29. menuSumaCuadradosMayorA")
    print("30. menuSumaPrimosMayorA")
    print("Escriba 'salir' para terminar.")

    opcion = input("Escriba una opción: ")

    if opcion.lower() == "salir":
        print("Saliendo del programa. 👋")
        return

    try:
        opcion = int(opcion)

        if opcion == 1:
            menuPotenciaMasCercana()
        elif opcion == 2:
            menuCantidadDecimales()
        elif opcion == 3:
            menucuentaDigitosDiferentes()
        elif opcion == 4:
            menuNumeroPalindromo()
        elif opcion == 5:
            menuDivisionTruncada()
        elif opcion == 6:
            menuOcurreEn()
        elif opcion == 7:
            menuOcurreEn2()
        elif opcion == 8:
            menuMayorDigito()
        elif opcion == 9:
            menuOcurreMas()
        elif opcion == 10:
            menuAgregarDigito()
        elif opcion == 11:
            menuDivisionResiduo()
        elif opcion == 12:
            menuSuprimirDigito()
        elif opcion == 13:
            menuesPrimoPalindromo()
        elif opcion == 14:
            menuCuadradoPerfecto()
        elif opcion == 15:
            menuSumaFraccionesPatron()
        elif opcion == 16:
            menuSumayRestaFraccionesPatron()
        elif opcion == 17:
            menuAnoDesdeMilNueveOchenta()
        elif opcion == 18:
            menuSumaPares()
        elif opcion == 19:
            menuNacioBiciestto()
        elif opcion == 20:
            menuCantidadCuadrados()
        elif opcion == 21:
            menuPrimoProximo()
        elif opcion == 22:
            menuCantidadPalindromosAnteriores()
        elif opcion == 23:
            menuCuantosCuadradosEntre()
        elif opcion == 24:
            menufuncionTruncate()
        elif opcion == 25:
            menuMenoresANumeroFib()
        elif opcion == 26:
            menuMenoresFibonacciPar()
        elif opcion == 27:
            menuRedondeo()
        elif opcion == 28:
            cantidadPrimosRango()
        elif opcion == 29:
            menuSumaCuadradosMayorA()
        elif opcion == 30:
            menuSumaPrimosMayorA()
        else:
            print("❌ Opción inválida. Ingrese un número entre 1 y 30.")
    except:
        print("❌ Error: Ingrese un número válido o 'salir' para terminar.")




#Programa  1 
#calcular cual es la potencia de 10 ams cercana a un numero. si esta a la misama distancia de 2 potencias de 10 , devolver la que es menor 

# #E : Un numero positivo 
#S : una potencia de 10 . 
#R : numeros negativos . 
def potenciaMasCercana (numero) :
    numero= int(numero)
    exponente_diez=0 
    while numero > 10** exponente_diez : 
        exponente_diez+=1 
    potencia_inmediata = 10 ** exponente_diez
    potencia_anterior = 10 ** ( exponente_diez-1 )
    if ( numero - potencia_anterior) <= (potencia_inmediata - numero ) : 
        return potencia_anterior
    return  potencia_inmediata
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
# 3 . digitos diferentes 
#e : Un numero 
#s : cantidad de digitos diferentes que tiene el numero 
# r : Solo numeros enteros positivos decimales 

#este me hizo llorar y pensarlo por 2 dias enteros . xd 
def cuentaDigitosDiferentes(num):
    if num == 0:
        return 1
    digitos_recorridos = 0    
    digitos_diferentes = 0    
    exponente = 0             
    hay_cero = False          
    while num > 0:
        digito_actual = num % 10
        esta_repetido = False
        if digito_actual == 0:
            while num > 0 and num % 10 == 0:
                num //= 10
            if not hay_cero:
                hay_cero = True
                digitos_diferentes += 1
            esta_repetido = True
        temporal = digitos_recorridos
        while temporal > 0 and not esta_repetido:
            if digito_actual == temporal % 10:
                esta_repetido = True
            else:
                temporal //= 10
        if not esta_repetido:
            digitos_recorridos += digito_actual * (10 ** exponente)
            exponente += 1
            digitos_diferentes += 1

        num //= 10

    return digitos_diferentes
def menucuentaDigitosDiferentes () : 
    print (" 3. ********** CANTIDAD DE DIGITOS DIFERENTES DE UN NUMERO  ********** ") 
    numero_para_contar = input ("Ingrese el numero entero positivo  que desea saber la cantidad de decimales : ")
    try : 
       numero_para_contar = int(numero_para_contar)
       if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("La cantidad de decimales diferentes de ", numero_para_contar, "es : ", cuentaDigitosDiferentes (numero_para_contar ) )
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros ")
# 3 . digitos diferentes 
#numero palindromo 
#E : un numero 
#s un booleano 
#R : 
#ocupo saber la cantidad de digitos del numero 
#shay que recorrer el numero de derecha a izquiera  . 
def numeroPalindromo (num) : 
    es_palindromo= True 
    num=int(num)
    digitos_numero= cantidadDecimales (num)
    if num== 0 : 
        return False
    if 0 < num and num  < 10  : 
        return es_palindromo
    while num > 0 and es_palindromo :
        digitos_numero= cantidadDecimales (num)
        potencia_numero=(10**(digitos_numero-1))
        primer_digito = num// potencia_numero
        ultimo_digito = num%10
        if primer_digito != ultimo_digito : 
            es_palindromo = False
        #condicion por si hay un numero atrapado entre varios ceros 
        num = (num % potencia_numero) // 10
        if (cantidadDecimales(num) != digitos_numero-2 ) and num != 0  : 
            while num%10== 0 : 
                num//=10 
    return es_palindromo
def menuNumeroPalindromo ( ) : 
    print (" 4. **********NUMERO PALINDROMO  **********")
    numero_para_funcion = input (" Ingrese un numero entero positivo que quiera saber si es palindromo o no : ")
    if numero_para_funcion <0 : 
        print( "ERROR : Uno o mas parametros no se cumplen \n --Numeros enteros positivos solamente ")
        return menuPrincipal()

    try : 
        respuesta =numeroPalindromo (numero_para_funcion)
        if respuesta : 
            print( " El numero ", numero_para_funcion, " Es palidromo " )
        else : 
            print ("El numero ", numero_para_funcion, " No es palidromo ")
    except : 
        "ERROR : Uno o mas parametros no se cumplen \n --Numeros enteros positivos solamente "
    menuPrincipal()
#dIVISION tRUNCADA 
#E : Dos numeros, un numero que es el restado, otro que resta( divide xd)
# : S , la cantidad de veces que el segundo numero resta el primero hasta que quede de residuo nu numero < restador
#r solo numeros enteros enteros positivos
def divisionTruncada(dividendo,divisor ) : 
    cociente= 0 
    while dividendo > 0 and divisor <= dividendo : 
        dividendo-=divisor
        cociente+=1
    return cociente
def menuDivisionTruncada () : 
    print (" 5. **********Division Truncada  **********")
    print ("La división truncada es una operación matemática en la que se divide un número y se descarta la parte decimal, quedándose solo con la parte entera del cociente\n")
    try: 
        dividendo = int(input ("Ingrese el numero que quiera dividir"))
        divisor= int( input(" Ingrese el numero de veces que quiera dividir :"))
        if divisor ==0 or dividendo ==0 : 
            print( "ERROR : Uno o mas parametros no se cumplen \n --Numeros enteros positivos solamente ")
            return menuPrincipal()
        respuesta= divisionTruncada (dividendo, divisor) 
        print ("El resultado es " , respuesta, "restas, entonces " , respuesta, " es el resutlado. ")
    except : 
        print( "ERROR : Uno o mas parametros no se cumplen \n --Numeros enteros positivos solamente\n -- Division por cero no es posible")
    return menuPrincipal()
#6. ocurer en cada digito .
#E Un numero  
#S Otro numero que indique en que pocicion ocurre por primera vez el numero de entrada 
#r : nada
def OcurreEn(cantidad, digito ) : 
    posicion=0
    se_encontro = False 
    while cantidad > 0 : 
        if cantidad%10== digito : 
            se_encontro= True
            return posicion+1
        posicion+=1
        cantidad//=10  
    if not se_encontro : 
        return 0
def menuOcurreEn () : 
    print (" 6. ********** Ocurre en (primero)   ********** ") 
    primer_numero = input ("Ingrese la cantidad   : ")
    segundo_numero = input ("Ingrese el digito que sedea saber en que poscicion aparece en la cantidad  : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)

       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if OcurreEn(primer_numero, segundo_numero) == 0 : 
           print ("El numero ", segundo_numero , " no se encuentra en " , primer_numero)
       else : 
           print (" El numero ", segundo_numero, " se encuentra en la poscicion ", OcurreEn(primer_numero, segundo_numero), "del numero ", primer_numero)
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros ")

#problema 7 , ocurreen 2 
#E : Dos numeros, uno siendo la cantidad y otro el numero que se quiere encontrar
#S : Un numero, este siendo la posicion del digito que se queria encontrar 
#R : 
def OcurreEn2 (numero, digito) : 
    poscicion = 1 
    exponente= (cantidadDecimales(numero)) - 1 
    se_encontro = False 
    while numero>0 :
        if digito ==( numero // (10**exponente)) : 
            return poscicion
        poscicion+=1 
        numero%= (10**exponente)
        exponente-=1
    if not se_encontro : 
        return 0
def menuOcurreEn2 () : 
    print (" 6. ********** Ocurre en (Segundo)   ********** ") 
    primer_numero = input ("Ingrese la cantidad   : ")
    segundo_numero = input ("Ingrese el digito que sedea saber en que poscicion aparece en la cantidad  : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)

       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if OcurreEn2(primer_numero, segundo_numero) == 0 : 
           print ("El numero ", segundo_numero , " no se encuentra en " , primer_numero)
       else : 
           print (" El numero ", segundo_numero, " se encuentra en la poscicion (de izquiera a derecha)", OcurreEn2(primer_numero, segundo_numero), "del numero ", primer_numero)
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros ")
#Problema 8 : Mayordigito 
#E : un numero 
#S : el digito de ese numero que es el mas grande 
#R : 
def MayorDigito (cantidad ) :    
    digito_mayor = 0
    while cantidad > 0 : 
        if cantidad%10 > digito_mayor : 
            digito_mayor= cantidad%10 
        cantidad//=10 
    return digito_mayor
def menuMayorDigito () : 
    print (" 8. ********** Digito mas grande ********** ") 
    numero_para_contar = input ("Ingrese un numero entero positivo: ")
    try : 
       numero_para_contar = int(numero_para_contar)
       if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("El digito mas grande del numero  ", numero_para_contar , " es el ", MayorDigito(numero_para_contar) )
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
#problema 9 : Digito que aparece mas veces en 
#E : 1 numero 
#S : otro numero , siendo este el digito que aparece mas veces . 
#R : NADA 
def apariciones (digito , num ) : 
    if digito == 0 and num == 0 : 
        return 1 
    contador = 0 
    while num> 0 : 
        if num%10 == digito : 
            contador+=1 
        num//=10 
    return contador   
def ocurreMas(num) : 
    digito_mas_apariciones = 0
    apariciones_de_digito_actual = 0
    cantidad_digitos = cantidadDecimales ( num ) 
    contador = 0 
    while num > 0 : 
        cantidad_apariciones = ( apariciones(num%10, num ))
        #print (cantidad_apariciones, "esto es apariciones" )
        if apariciones_de_digito_actual < cantidad_apariciones : 
            digito_mas_apariciones = num%10 
            apariciones_de_digito_actual = apariciones(num % 10, num)
            contador =1 
        elif apariciones_de_digito_actual==cantidad_apariciones : 
            contador+=1 
        num//=10 
    if contador == cantidad_digitos :
        return -1 
    return digito_mas_apariciones
def menuOcurreMas () : 
    print (" 9. ********** Digito  que mas aparece  ********** ") 
    numero_para_contar = input ("Ingrese un numero entero positivo: ")
    try : 
       numero_para_contar = int(numero_para_contar)
       if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("El digito que mas ocurre en el numero ", numero_para_contar , " es el ", ocurreMas(numero_para_contar) )
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
#EJ 10 
#E : dos numeros , un numero al que se le suma y un digito sumador 
#S : un numero entero 
#R : nada 
def AgregarDigito (cantidad, digito ) : 
    resultado = 0 
    exponente = 0 
    while cantidad > 0 : 
        digito_resultado = (cantidad %10 ) + digito 
        if digito_resultado > 9 : 
            digito_resultado%=10 
        resultado = (resultado )+ (digito_resultado * (10**exponente)) 
        exponente+=1 
        cantidad//=10
    return resultado 
def menuAgregarDigito () : 
    print (" 10. ********** Agregar Digito  ********** ") 
    primer_numero = input ("Ingrese la cantidad que desea que se le agregue    : ")
    segundo_numero = input ("Ingrese la cantidad que desea agregar  : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)
       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("Al agregarle la cantidad de  ", segundo_numero, " a todos los digitos de  ", primer_numero, "queda como resultado el numero ,", AgregarDigito( segundo_numero, primer_numero))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")

#problema 11 : Resodio 
# E : 2 numeros., el dividendo y divisor 
#S : el residuo
#R : anda 
def divisionResiduo (dividendo , divisor ) : 
    cociente = 0 
    while dividendo > 0 and divisor <= dividendo : 
        dividendo-=divisor
        cociente+=1
    return dividendo
def menuDivisionResiduo () : 
    print (" 11. ********** Residuo de una Division   ********** ") 
    primer_numero = input ("Ingrese la cantidad que desea dividir (dividendo)    : ")
    segundo_numero = input ("Ingrese la cantidad de veces que desea dividir el numero (divisor)  : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)
       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("Al dividir la cantidad de ", primer_numero, "entre ", segundo_numero , "', se obtiene como residuo ", divisionResiduo(primer_numero, segundo_numero ))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
#13/12 , no se .un errror nno se si es en el doc xd . llamemosle ejercicio 12
#Suprimir digito 
#E: 2 numeros , uno es el digito que se quiere suprimir y el otro es el numero al que se le quiere suprimir el digito 
#S : El numero con los digitos suprimidos 
def suprimirDigito (num, suprimido ) : 
    digito_de_num = 0 
    resultado= 0 
    exponente = 0 
    while num > 0 : 
        digito_de_num = num%10 
        if digito_de_num != suprimido : 
            resultado = resultado + (digito_de_num * (10**exponente))
            exponente+=1 
        num//=10 
    return resultado 
def menuSuprimirDigito () : 
    print (" 12. ********** Suprimir Digito    ********** ") 
    primer_numero = input ("Ingrese la cantidad que desea que sea suprimida   : ")
    segundo_numero = input ("Ingrese el digito que desea que sea suprimido   : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)
       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("Al suprimir al numero  ", primer_numero, "el digito ", segundo_numero , "', se obtiene como resultado  ", suprimirDigito(primer_numero, segundo_numero ))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
# 14. Primo Palindromo 
#E : un numero 
# S : Un booleano 
#R : nada 
"""FUNCION AUXILIAR Determina si un numero es primo   """   
def esPrimo (num ) :
    primo_mas_grande = 2 
    resultado = True 
    while primo_mas_grande <= num :
        if num % primo_mas_grande == 0 and num != primo_mas_grande: 
            return False 
        primo_mas_grande+=1 
    return resultado
def esPrimoPalindromo (numero): 
    palindromo= numeroPalindromo(numero)
    primo= esPrimo(numero)
    if palindromo and primo: 
        return True 
    return False
def menuesPrimoPalindromo() : 
    print (" 14. ********** Verificar si un numero es Primo y Palindromo  ********** ") 
    numero_para_contar = input ("Ingrese un numero entero positivo: ")
    try : 
       numero_para_contar = int(numero_para_contar)
       if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       else : 
            if esPrimoPalindromo(numero_para_contar) :
               print ("El numero es Primo Y palindromo ")
            else : 
               print ("El numero no es primo y palindromo")
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")#15 : CuadradoPerfecto 
#E : Numero 
#S : otro numero 
# R : nada 
def cuadradoPerfecto(num) : 
    contador =1
    cuadrado = 0
    while num> contador*contador : 
        cuadrado= contador*contador
        contador+=1
    return cuadrado
def menuCuadradoPerfecto() : 
    print (" 15. ********** Un cuadrado perfecto menor a Numero   ********** ") 
    numero_para_contar = input ("Ingrese un numero entero positivo: ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
        print (" El numero cuadrado perfecto mas grande que sea menor a ", numero_para_contar, "es : " , cuadradoPerfecto(numero_para_contar))

    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
        

#16 : Suma de fracciones 
# E :numero, siendo este la cantidad de digitos a sumar 
#S: otro numero, la sumatoria de todas las fracciones
#r : nada
def sumafraccionesPatron (num) :
    contador = 0
    dividendo= 2
    divisor = 4
    resultado= 0 
    while contador < num : 
        fraccion_actual= dividendo/divisor
        divisor+=3 
        dividendo+=2 
        fraccion_siguiente = dividendo/divisor
        resultado =  resultado+fraccion_actual+fraccion_siguiente
        contador+=1
    return resultado
def menuSumaFraccionesPatron() : 
    print (" 16. ********** Sumatoria de Fracciones en Patron (Suma solamente )   ********** ") 
    numero_para_contar = input ("Ingrese el nuemero de terminos a sumar : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos (ya que es numero de terminos)  ")
        
        return print ("La sumatoria de la cantidad de terminos ", numero_para_contar, "del patron de fracciones es : ", sumafraccionesPatron(numero_para_contar))

    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")#17 : Suma de fracciones 
# E :numero, siendo este la cantidad de digitos a computar 
#S: otro numero, el resultado  de todas las fracciones
#r : nada
def sumayrestafraccionesPatron (num) :
    contador = 0 
    dividendo = 1 
    divisor = 4 
    resultado = 0 
    while contador < num : 
        primera_fraccion = dividendo/divisor
        if contador%2 == 1 : 
            resultado = resultado- primera_fraccion
        else : 
            resultado =  resultado+primera_fraccion
        contador+=1 
        dividendo+= 3 
        divisor +=3 
    return resultado
def menuSumayRestaFraccionesPatron() : 
    print (" 17. ********** Sumatoria de Fracciones en Patron (Suma y resta )    ********** ") 
    numero_para_contar = input ("Ingrese el nuemero de terminos a sumar : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos (ya que es numero de terminos)  ")
        
        return print ("La sumatoria de la cantidad de terminos ", numero_para_contar, "del patron de fracciones es : ", sumayrestafraccionesPatron(numero_para_contar))

    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
        

#17 : Suma de fracciones # print (sumayrestafraccionesPatron (1))

#EJ 18 : ano nacimiento 
# # e : 3 numeros , dia , mes , anyo 
#s : numero o un string ,  numero siendo la cantidad de dias. sitring si la fecha brindada es menor a la fecha de referencia 
"""FUNCION AUXILIAR   """   
def anoBiciesto(year) : 
    #divisibilidad por 4 : 
    if year %4 == 0 : 
        if year %100 == 0 and year%400 == 0 : 
            return True 
        elif year%100 != 0 :
            return True 
    return False 
def anoDesdeMilNueveOchenta (day, month,year) : 
    #fecha de referencia  : 1/01/1980 
    es_biciesto_global = anoBiciesto(year)
    tempoal_anyo = year
    sumatoria_dias = 0
    if 1980 <= year : 
        while tempoal_anyo> 1980 : 
            es_biciesto_ciclo = anoBiciesto(tempoal_anyo)
            if es_biciesto_ciclo : 
                sumatoria_dias+= 366 
            else : 
                sumatoria_dias+=365
            tempoal_anyo-=1
        if month >=1 : 
            while month>1 : 
                #si el mes es febrero 
                if month == 2 : 
                    #si es biciesto el anyo 
                    if es_biciesto_global : 
                        sumatoria_dias+= 29 
                    else : 
                        sumatoria_dias+=28 
                #si es mes con 30 dias 
                elif month == 4 or month == 6 or month == 9 or month == 11 : 
                    sumatoria_dias+=30 
                #si es mes con 31 dias 
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 : 
                    sumatoria_dias+=31 
                #resta 1 al mes , asi ir sumando hasta llegara a 0 
                month -=1 
        #sumamos los dias a la cuenta de los dias 
        if year > 1980 : 
            sumatoria_dias+= day
    return sumatoria_dias
def menuAnoDesdeMilNueveOchenta () : 
    print (" 18. ********** Calculadora de cantidad de dias desde 1/1/1980    ********** ") 
    print ("-------------INGRESE UNA FECHA A CONTINUACION ---------------") 
    anio = input ( "Ingrese el Año de su fecha")
    mes = input ( "Ingrese el Mes de su fecha")
    dia = input ( "Ingrese el Dia de su fecha")
    try : 
        anio = int(anio)
        mes = int(mes)
        dia = int(dia)
        if 31<dia<=0 or 12<mes<=0  : 
            return print (" Error en uno de los parametros : \n -- Fecha ingresada es invalida (Mes o Dia invalidos ) ")
        return print ( "La cantidad de dias desde el 1/1/1980 hasta la fecha de " , dia, "/" , mes , "/", anio , "/ " ,"es de :", anoDesdeMilNueveOchenta(dia, mes , anio) )
    except : 
        print ("ERROR en uno de los parametros : La fecha ingresada es invalida (Solo numeros enteros para el mes, dia y año)")
#19 : suma pares 
# E: un numero 
#S: Otro numero 
#R : nada 
def sumaPares ( num ) : 
    resultado = 0 
    while num > 0 : 
        digito = num%10 
        if digito %2 == 0 : 
            resultado+=digito
        num//=10 
    return resultado
def menuSumaPares() : 
    print (" 19. ********** Sumatoria de digitos pares    ********** ") 
    numero_para_contar = input ("Ingrese un nuemero  : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos  ")
        
        return print ("La sumatoria delos digitos pares de  ", numero_para_contar, " es : ", sumaPares(numero_para_contar))

    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")


#eJ 20 : Nacio en biciesto 
#E : 1 numeros , dia , mes , anyo 
#S : un bool 
#R : nada 
def nacioBiciestto(dia,mes,anyo ) : 
    #XD
    resultado = anoBiciesto(anyo)
    return resultado
def menuNacioBiciestto () : 
    print (" 120. ********** Calculadora de cantidad año de nacimiento biciesto   ********** ") 
    print ("-------------INGRESE SU FECHA DE CUMPLEAñOS A CONTINUACION ---------------") 
    anio = input ( "Ingrese el Año de su fecha")
    mes = input ( "Ingrese el Mes de su fecha")
    dia = input ( "Ingrese el Dia de su fecha")
    try : 
        anio = int(anio)
        mes = int(mes)
        dia = int(dia)
        if 31<dia<=0 or 12<mes<=0  : 
            return print (" Error en uno de los parametros : \n -- Fecha ingresada es invalida (Mes o Dia invalidos ) ")
        if nacioBiciestto(anio , mes , dia ) : 
            return print ("el año de nacimiento es biciesto")
        return print ("el año de nacimiento  no es biciesto")
    except : 
        print ("ERROR en uno de los parametros : La fecha ingresada es invalida (Solo numeros enteros para el mes, dia y año)")


#21 cantiodad Cuadrados Perfectos 
#E : 1 numero 
#S : otro numero 
#R :nada 
def cantidadCuadrados ( num ) : 
    import math
    raiz_numero =type (int( math.sqrt(num))) == int 
    cuadrado = 1 
    contador=1 
    while cuadrado**2 < num  : 
        cuadrado+=1
        contador+=1 
    if raiz_numero : 
        return contador-1
    return contador 
def menuCantidadCuadrados() : 
    print (" 21. ********** Cantidad Cuadrados    ********** ") 
    numero_para_contar = input ("Ingrese un numero : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        
        return print ("La cantidad de cuadrados que existen menores al numero ", numero_para_contar , "es de : ", cantidadCuadrados(numero_para_contar))

    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")

#22 : primo mas proximo 
#E :un numero 
#S otro numero , enumero primo 
#E : nada 
def primoProximo ( num ) : 
    if num == 0 or num == 1 : 
        return 2 
    contador_hacia_arriba = num+1
    contador_hacia_abajo = num-1
    es_primo_abajo = esPrimo (contador_hacia_abajo)
    es_primo_arriba = esPrimo (contador_hacia_arriba)
    resultado = 0 
    while not es_primo_arriba :
        contador_hacia_arriba+=1 
        es_primo_arriba = esPrimo (contador_hacia_arriba)
    while not es_primo_abajo :
        contador_hacia_abajo -=1 
        es_primo_abajo = esPrimo(contador_hacia_abajo)
    if esPrimo(num) : 
        return  num
    
    dist_arriba = contador_hacia_arriba - num
    dist_abajo = num - contador_hacia_abajo

    if dist_arriba < dist_abajo:
        return contador_hacia_arriba
    elif dist_abajo < dist_arriba:
        return contador_hacia_abajo
    else:
        return contador_hacia_abajo 
def menuPrimoProximo() : 
    print (" 22. ********** Primo Mas Proximo    ********** ") 
    numero_para_contar = input ("Ingrese un numero : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos  ")
        
        return print ("El numero primo mas proximo a ", numero_para_contar , "es : ", primoProximo(numero_para_contar))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
# 23 : CUANTOS PALINDROMOS ANTES DE NUMERO 
#e : NUMERO 
#s : NUMERO 
#R : ENTEROS POSITIVOS 

def cantidadPalindromosAnteriores (num ) :
    contador = 0
    resultado = 0 
    while contador < num : 
        contador +=1 
        if numeroPalindromo( contador) : 
            resultado +=1
    if numeroPalindromo(num) : 
        return resultado-1 
    return resultado
def menuCantidadPalindromosAnteriores() : 
    print (" 23. ********** Cantidad de numeros palindromos anteriores********** ") 
    numero_para_contar = input ("Ingrese un numero entero positivo a continuacion  : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        
        return print ("Existen ", cantidadPalindromosAnteriores(numero_para_contar), " numeros palindromos anteriores a ", numero_para_contar)
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
# 23 : CUANTOS PALINDROMOS ANTES DE NUMERO 
#24 : cuantos cuadrados perfectos entre ellos 
# e : dos numero 
# S : otro numero 
#R : nada 

def cuantosCuadradosEntre ( menor,mayor  ) : 
    contador_cuadrados = 0 
    cuadrados_cantidad = 0 
    while contador_cuadrados *contador_cuadrados <= menor : 
        contador_cuadrados+=1
    #Segundo Ciclo para saber la cantidad de cuadrados que hay desde el menor al mayor
    while contador_cuadrados* contador_cuadrados < mayor :
        contador_cuadrados+=1
        cuadrados_cantidad+=1
    return cuadrados_cantidad
def menuCuantosCuadradosEntre () : 
    print (" 24. ********** Cuantos cuadrados entre  ********** ") 
    primer_numero = input ("Ingrese  el primer numero del rango que desea averiguar    : ")
    segundo_numero = input ("Ingrese el ultimo numero del rango que desea averiguar   : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)
       if primer_numero < 0  or segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       
       print ("Existen ", cuantosCuadradosEntre(primer_numero, segundo_numero), " numeros cuadrados perfectos entre ", primer_numero, "y ", segundo_numero)
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")    
#25 : funcion truncate 
#E : 1 numero float 
#S : el numero pero en int 
# R : nada 
def funcionTruncate(num) : 
    contador_decimales = 0 
    numero_completo = 0 
    while (type(num)== float) : 
        try : 
            num= int(num)
        except : 
            num*=10 
            contador_decimales +=1
    numero_completo = num//(10** contador_decimales)
    return numero_completo
def menufuncionTruncate() : 
    print (" 25. ********** Truncar ********** ") 
    numero_para_contar = input ("Ingrese un numero  positivo a continuacion  : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros  positivos   ")
        
        return print ("El numero truncado es : ", funcionTruncate(numero_para_contar))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros positivos")

#Serie Finobbacci 
#E : un numero 
#S : otro numero 
# R : nnada 
def numerosFibonacci(n) :
    contador = 0
    resultado = 0
    digito_fib_sig = 0 
    digito_fib_ant=1 
    while n > contador :
        if n== 1 : 
            return 0 
        resultado = digito_fib_ant+digito_fib_sig
        digito_fib_ant= digito_fib_sig
        digito_fib_sig= resultado
        contador+=1
    return resultado
def menoresANumeroFib(num) : 
    comparador= 0
    contador = 0 
    while num>= comparador:
        comparador= numerosFibonacci(contador)
        contador+=1
    return contador-1 
def menuMenoresANumeroFib() : 
    print (" 26. ********** Menores a numero en serie Fibonacci ********** ") 
    numero_para_contar = input ("Ingrese un numero  entero positivo a continuacion  : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        
        return print ("La cantidad de numeros de la serie de fibonacci menores a ", numero_para_contar, "es de : ", menoresANumeroFib(numero_para_contar))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")
#Serie fibonanci pares que 
#E : un numero 
#S : otro numero 
#R : nada 

def menoresFibonacciPar(cantidad) : 
    resultado = 0
    contador_de_serie = 2
    num_fib= 0
    while num_fib < cantidad : 
        if num_fib%2 == 0 : 
            resultado+=1 
        num_fib = numerosFibonacci(contador_de_serie)
        contador_de_serie+=1   
    return resultado
def menuMenoresFibonacciPar() : 
    print (" 27. ********** Menores a numero en serie Fibonacci que sean pares ********** ") 
    numero_para_contar = input ("Ingrese un numero  entero positivo a continuacion  : ")
    try : 
        numero_para_contar = int(numero_para_contar)
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        
        return print ("La cantidad de terminos de la serie de fibonacci que sean pares y sean menores a ", numero_para_contar, "son  de : ", menoresFibonacciPar(numero_para_contar))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")

#28 . redondeo 
#E : un float 
#S : un numero entero , redondeado 
#r :  
def redondeo (num) : 
    parte_decimal = abs( num- int(num))
    if parte_decimal> 0.5 : 
        return int(num)+1
    return int(num)
def menuRedondeo() : 
    print (" 28. ********** Redondeo de un numero con decimales  ********** ") 
    numero_para_contar = input ("Ingrese un numero positivo a continuacion  : ")
    try : 
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros positivos   ")
        return print ("El numero redondeado es : ", redondeo(numero_para_contar))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros positivos")

#29 , cantidad de primos rango 
#E : 2 numeros 
#s : un numero , la cantidad de primo s
#R : nada 
def cantidadPrimosRango(primer_numero, segundo_numero  ) : 
    resultado=0 
    contador= primer_numero
    while contador< segundo_numero : 
        if esPrimo(contador) : 
            resultado+=1 
        contador+=1 
    return resultado
def cantidadPrimosRango () : 
    print (" 29. ********** CANTIDAD DE NUMEROS PRIMOS ENTRE DOS NUMEROS  ********** ") 
    primer_numero = input ("Ingrese el primer numero  (limite inferior) : ")
    segundo_numero = input ("Ingrese el segundo numero (limite superior)   : ")
    try : 
       primer_numero = int(primer_numero)
       segundo_numero= int(segundo_numero)
       if primer_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       if segundo_numero < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos.  ")
       print ("La cantidad de numeros primos entre los numeros ", primer_numero , "y ", segundo_numero, "es de : ",cantidadPrimosRango(primer_numero, segundo_numero))
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros enteros positivos")

#30 suma de cuadrados perfectos 
#E : un numero 
#S : otro numero 
#R : nada 

def sumaCuadradosMayorA(cantidad) : 
    contador = 1
    sumatoria = 0 
    cuadrado = 0
    while sumatoria <cantidad:
        cuadrado = contador**2  
        sumatoria += cuadrado
        contador+=1 
    return contador
def menuSumaCuadradosMayorA() : 
    print (" 30. ********** Cuantos cuadrados como minimo para llegar a numero  ********** ") 
    numero_para_contar = input ("Ingrese un numero positivo entero a continuacion  : ")
    try : 
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        return print ("La cantidad de numeros cuadrados perfectos minima  que se tienen que sumar para obtener una cantidad mayor a", numero_para_contar , " son de ", sumaCuadradosMayorA(numero_para_contar))
                    
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros positivos")
#31 Suma de primos 
#e : un numero 
#s : otro numero 
#R : nada 

def SumaPrimosMayorA(cantidad) : 
    contador = cantidad
    resultado = 0  
    sumatoria = 0
    while sumatoria < cantidad : 
        if esPrimo(contador) : 
            resultado+=1 
            sumatoria+=contador
            print (contador, "contador" )
            print (sumatoria, "valor sum ")
        contador-=1
    return resultado
def menuSumaPrimosMayorA() : 
    print (" 31. ********** Cuantos numeros primos como minimo para llegar a numero  ********** ") 
    numero_para_contar = input ("Ingrese un numero positivo entero a continuacion  : ")
    try : 
        if numero_para_contar < 0 : 
           return print (" Error en uno de los parametros : \n -- Solo numeros enteros positivos   ")
        return print ("La cantidad de numeros primos  minima  que se tienen que sumar para obtener una cantidad mayor a", numero_para_contar , " es de ", menuSumaPrimosMayorA(numero_para_contar))
                    
    except : 
        print ( " Error en uno de los parametros : \n -- Solo numeros positivos")

    
menuPrincipal()