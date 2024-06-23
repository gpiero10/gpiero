#EJERCICIO 1)
def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    res:list[int] = []
    for codigo in codigos_barra:
        if es_primo(succionador(codigo)) == True:
            res.append(codigo)
    return res
    
def succionador(numero:int)->int:
    stringus = str(numero)
    res:str = ""
    for i in range(len(stringus)-3,len(stringus)):
        res += stringus[i]
    return int(res)
            
def es_primo(numero:int)->bool:
    if numero == 1:
        return False
    elif numero == 0:
        return False
    for i in range(2,numero-1):
        if numero % i == 0:
            return False
    return True

#EJERCICIO 2)
def stock_productos(stock_cambios:list[(str,int)])->dict[str,(int,int)]:
    productos:list[str] = []
    for tupla in stock_cambios:
        if not tupla[0] in productos:
            productos.append(tupla[0])
    diccionario_fin:dict[str,(int,int)] = {}
    lista_stock_por_producto:list[int] = []
    for producto in productos:
        for tupla in stock_cambios:
            if producto == tupla[0]:
                lista_stock_por_producto.append(tupla[1])
        diccionario_fin[producto] = min_y_max(lista_stock_por_producto)
        lista_stock_por_producto = []
    return diccionario_fin
    
def min_y_max(lista:list[int])->(int,int):
    minimo = lista[0]
    maximo = lista[0]
    for i in range(1,len(lista)):
        if minimo > lista[i]:
            minimo = lista[i]
        if maximo < lista[i]:
            maximo = lista[i]
    res = (minimo,maximo)
    return res

#EJERCICIO 3)
def un_responsable_por_turno(grilla_horaria:list[list[str]])->list[(bool,bool)]:
    dias:list[list[str]] = []
    columna:list[str] = []
    for i in range(0,len(grilla_horaria[0])): 
        for fila in grilla_horaria:
            columna.append(fila[i])
        dias.append(columna)
        columna = []
    res:list[(bool,bool)] = []
    for dia in dias:
        encargado_mañana:str = dia[0]
        encargado_tarde:str = dia[4]
        valor1 = True
        valor2 = True 
        for i in range(1,4):
            if encargado_mañana != dia[i]:
                valor1 = False
        for j in range(4,8):    
            if encargado_tarde != dia[j]:
                valor2 = False
        tupla = (valor1,valor2)
        res.append(tupla)
        tupla = ()
    return res

#EJERCICIO 4)
# def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str])->int: