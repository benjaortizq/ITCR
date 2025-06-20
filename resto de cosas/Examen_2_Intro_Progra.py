##Primer ejercicio
#comprimir lista
#E : Una lista de enteros
#S : una lista con sus digitos consecuivos ordenados por cantidad
#R : la lista tiene que ser numerica
def comprimir_lista (lista) :
    tamano = len(lista)
    resultado=[]
    contador =1
    elemento_actual=lista[0]
    for i in range ( 1, tamano ) :
        if lista[i]== elemento_actual :
            contador+=1
            if i== ( tamano-1) :
                resultado+=[[elemento_actual, contador]]
                break
            continue
        elif lista[i]!= elemento_actual:
            resultado+= [ [elemento_actual, contador]]
            elemento_actual= lista[i]
            contador=1

    return resultado

##segundo ejercicio
#Natural
#e : una lista de elementos numericos desordenados
#s : una lista de listas con los elementos metidos en una lista que sigan los elementos ordenados de menos a mayor
#R : que la lista de entrada sea numerica

def natural(lista ) :
    tamano= len(lista)
    elemento_actual =lista[0]
    resultado=[]
    sublista=[elemento_actual]
    for i in range (1,tamano) :
        if lista[i] > elemento_actual :
            sublista+=[lista[i]]
            elemento_actual= lista[i]
            if i == tamano-1 :
                resultado+=[sublista]
                break
            continue
        else:
            resultado+=[sublista]
            elemento_actual = lista[i]
            sublista=[elemento_actual]
            if i== tamano-1 :
                resultado+=[sublista]
    return resultado

##3 :
#cruces perfectas
#E : una matriz cuadrada binaria
#s : un string que diga la cantidad de cruces que tiene la matriz
def cruces_perfectas(matriz) :
    cantidad_fil = len(matriz)
    cantidad_col = len(matriz[0])
    cantidad_cruces=0

    for i in range(1,cantidad_fil-1) :

        for j in range (1,cantidad_col-1):
            hay_arriba=False
            hay_abajo=False
            hay_iz = False
            hay_der = False
            if matriz[i][j]== 1 :
                #verificar arriba
                if matriz [i-1][j] ==1 :
                    hay_arriba=True
                #verificar abajo
                if matriz[i+1][j]== 1 :
                    hay_abajo=True
                #izquierda
                if matriz[i][j-1] == 1 :
                    hay_iz= True
                #derecha
                if matriz[i][j+1]== 1 :
                    hay_der= True
                #comprubar si cruz
                if (hay_abajo and hay_arriba) and (hay_iz and hay_der ):
                    cantidad_cruces+=1
            else :
                continue
    return cantidad_cruces

#ejercicio 4
#ceros _abajo de diagonal
#E : una matriz cuadrada
#s : Booleano

def ceros_abajo (matriz) :
    tamano= len(matriz)
    elementos_abajo = []
    elementos_arriba = []
    elementos_dia =[]
    #AGRUPADOR
    for i in range (tamano):
        for j in range (tamano):
            if i==j :
                elementos_dia+=[ matriz[i][j]]
            elif i < j :
                elementos_arriba+= [matriz[i][j]]
            else :
                elementos_abajo+= [matriz[i][j]]

    for elementos in elementos_abajo :
        if elementos!= 0 :
            return False
    for vector in elementos_dia :
        if vector== 0 :
            return False
    for buscador in elementos_arriba :
        if buscador ==0 :
            return False
    return True
