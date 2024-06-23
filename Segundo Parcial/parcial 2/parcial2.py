#EJERCICIO 1)
def acomodar(lista:list[str])->list[str]:
    El_Leon:list[str] = []
    Massa_cocaina:list[str] = []
    res:list[str] = []
    for elemento in lista:
        if elemento == "LLA":
            El_Leon.append(elemento)
        elif elemento == "UP":
            Massa_cocaina.append(elemento)
    res:list[str] = Massa_cocaina + El_Leon
    return res

#EJERCICIO 2)
def pos_umbral(personas:list[int], umbral:int)->int:
    posicion:int = 0
    sumatoria_de_positivos:int = 0
    for i in range(0,len(personas)):
        if personas[i] >= 0 and sumatoria_de_positivos < umbral:
            sumatoria_de_positivos += personas[i]
            posicion:int = i
    if sumatoria_de_positivos <= umbral:
        posicion:int = -1
    return posicion

#EJERCICIO 3)
def columnas_repetidas(matriz:list[list[int]])->bool:
    matriz_div_2:list[list[float]] = []
    fila_div_2:list[float] = []
    for fila in matriz:
        for numero in fila:
            fila_div_2.append(numero/2)
        matriz_div_2.append(fila_div_2)
        fila_div_2:list[float] = []
    columnas_div_2:list[list[float]] = generador_columnas(matriz_div_2)
    for i in range(0,int(len(columnas_div_2)/2)):
        if columnas_div_2[i] != columnas_div_2[i+int(len(columnas_div_2)/2)]:
            return False
    return True
                
# aux
def generador_columnas(matriz:list[list[float]])->list[list[float]]:
    columnas:list[list[float]] = []
    columna:list[float] = []
    for i in range(0,len(matriz[0])):
        for fila in matriz:
            columna.append(fila[i])
        columnas.append(columna)
        columna = []
    return columnas
# fin aux

#EJERCICIO 4)
def cuenta_posiciones_por_nacion(naciones:list[str],torneos:dict[int,list[str]])->dict[str,list[int]]:
    res:dict[str,list[int]] = {}
    for pais in naciones:
        res[pais] = notar_posicion(pais,naciones,torneos)
    return res

# auxi
def notar_posicion(pais:str,naciones:list[str],torneos:dict[int,list[str]])->list[int]:
    res = [0]*len(naciones)
    for año in torneos.keys():
        for i in range(0,len(naciones)):
            if torneos[año][i] == pais:
                res[i] += 1
    return res 
# fin auxi
