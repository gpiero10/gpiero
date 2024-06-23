from queue import Queue as Cola 
#EJERCICIO 1)
def reordenar_cola_priorizando_vips(filaClientes:Cola[(str,str)])->Cola[str]:
    lista_de_clientes:list[(str,str)] = []
    while filaClientes.empty() != True:
        lista_de_clientes.append(filaClientes.get())
    lista_vip:list[str] = []
    lista_comun:list[str] = []
    for tupla in lista_de_clientes:
        if tupla[1] == "vip":
            lista_vip.append(tupla[0])
        elif tupla[1] == "comun":
            lista_comun.append(tupla[0])
    lista_final:list[str] = lista_vip + lista_comun
    res:Cola[str] = Cola()
    for elemento in lista_final:
        res.put(elemento)
    for tupla in lista_de_clientes:
        filaClientes.put(tupla)
    return res

#EJERCICIO 2)
estrategias:dict[str,str] = {}
def torneo_de_gallinas(estrategias:dict[str,str])->dict[str,int]:
    participantes:list[str] = []
    cagones:list[str] = []
    valientes:list[str] = []
    for pata in estrategias.keys():
        participantes.append(pata)
    for chabon in participantes:
        if estrategias[chabon] == "me desvio siempre":
            cagones.append(chabon)
        elif estrategias[chabon] == "me la banco y no me desvio":
            valientes.append(chabon)
    puntaje:dict[str,int] = {}
    for chabon in participantes:
        if chabon in valientes:
            puntaje[chabon] = (len(valientes) - 1)*(-5) + len(cagones)*10
        elif chabon in cagones:
            puntaje[chabon] = (len(cagones) - 1)*(-10) + len(valientes)*(-15)
    return puntaje
                        
    # si ambos son gallinas: -10 puntos para ambos
    # si uno es gallina y el otro no: -15 puntos para el gallina y +10 para el valiente 
    # si ambos son valientes: -5 puntos para ambos
    
#EJERCICIO 3)
def quien_gano_el_tateti_facilito(tablero:list[list[chr]])->int:
    columnas:list[list[chr]] = []
    columna:list[chr] = []
    for i in range(0,len(tablero[0])):
        for fila in tablero:
            columna.append(fila[i])
        columnas.append(columna)
        columna = []
    res = 0
    if hay_tres_consecutivos('X',columnas) == True and hay_tres_consecutivos('O',columnas) == False:
        res = 1
    elif hay_tres_consecutivos('O',columnas) == True and hay_tres_consecutivos('X',columnas) == True:
        res = 3
    elif hay_tres_consecutivos('O',columnas) == True and hay_tres_consecutivos('X',columnas) == False:
        res = 2
    elif hay_tres_consecutivos('O',columnas) == False and hay_tres_consecutivos('X',columnas) == False:
        res = 0
    return res

# auxi
def hay_tres_consecutivos(marcacion:chr,columnas:list[list[chr]])->bool:
    contador_consecutivo:int = 0
    for columna in columnas:
        for elemento in columna:
            if marcacion == elemento:
                contador_consecutivo += 1
            elif marcacion != elemento and contador_consecutivo < 3:
                contador_consecutivo = 0
        if contador_consecutivo >= 3:
            return True
        else:
            contador_consecutivo = 0
    return False      
# fin auxi                       

#EJERCICIO 4)
def cuantos_sufijos_son_palindromos(palabra:str)->int:
    sufijos:list[str] = generador_sufijos(palabra)
    res = 0
    for sufijo in sufijos:
        if sufijo == coloca_al_reves(sufijo):
            res += 1
    return res   

def coloca_al_reves(palabra:str)->str:
    res = ""
    for i in range(len(palabra)-1,-1,-1):
        res += palabra[i]
    return res
def generador_sufijos(palabra:str)->list[str]:
    sufijos = []
    for i in range(0,len(palabra)):
        sufijo = ""
        for j in range(i,len(palabra)):
            sufijo += palabra[j]
        sufijos.append(sufijo)
    return sufijos    