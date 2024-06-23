#EJERCICIO 1)
# v: Realiza un viaje (todos los viajes son de $56)
# r: Recarga saldo (todas las recargas son de $350)
# s: Visualiza el saldo actual (no modifica el saldo)
# x: El usuario decide terminar el programa
# Implementar la función verificar_transacciones() que dada una secuencia de caracteres s, devuelve el 
# saldo de la billetera al momento de terminar el programa. La finalización del programa está determinada 
# por: (1) aparición de una x, (2) el usuario está intentando hacer un pago sin saldo suficiente (en esta 
# billetera virtual no se permite saldo negativo), (3) no hay más transacciones en la lista.
def verificar_transacciones(s:str)->int:
    saldo:int = 0
    for i in range(0,len(s)):
        if s[i] == 's':
            saldo += 0
        elif s[i] == 'v' and saldo < 56:
            return saldo
        elif s[i] == 'v' and saldo >= 56:
            saldo -= 56
        elif s[i] == 'r':
            saldo += 350
        elif s[i] == 'x':
            return saldo
    return saldo

#EJERCICIO 2)
def valor_minimo(seguimiento_diario:list[(float,float)])->float:
    lista_de_minimas:list[float] = []
    for tupla in seguimiento_diario:
        lista_de_minimas.append(tupla[0])
    res:float = lista_de_minimas[0]
    for i in range(1,len(lista_de_minimas)):
        if res > lista_de_minimas[i]:
            res = lista_de_minimas[i]
    return res

#EJERCICIO 3)
def valores_extremos(cot_diarias:dict[str,list[(int,float)]])->dict[str,(float,float)]:
    empresas:list[str] = []
    for empresa in cot_diarias.keys():
        empresas.append(empresa)
    empresa_min_y_max:dict[str,(float,float)] = {}
    for empresa in empresas:
       empresa_min_y_max[empresa] = who_max_min(cot_diarias[empresa])
    return empresa_min_y_max
       
       
def who_max_min(info:list[(int,float)])->(float,float):
    valores:list[float] = []
    for tupla in info:
       valores.append(tupla[1])
    minimo = valores[0]
    maximo = valores[0]
    for i in range(1,len(valores)):
        if minimo > valores[i]:
            minimo = valores[i]
    for i in range(1,len(valores)):
        if maximo < valores[i]:
            maximo = valores[i]
    res = (minimo,maximo)
    return res

#EJERCICIO 4)
def es_sudoku_valido(matriz:list[list[int]])->bool:
    columnas:list[list[int]] = []
    columna:list[int] = []
    for i in range(0,9):
        for fila in matriz:
            columna.append(fila[i])
        columnas.append(columna)
        columna = []
    if no_hay_repetidos(quita_ceros(matriz)) == True and no_hay_repetidos(quita_ceros(columnas)) == True:
        return True
    else:
        return False
        
def quita_ceros(m:list[list[int]])->list[list[int]]:
    res = []
    fila_sin_ceros = []
    for fila in m:
        for numero in fila:
            if numero != 0:
                fila_sin_ceros.append(numero)
        res.append(fila_sin_ceros)
        fila_sin_ceros = []
    return res
                
def no_hay_repetidos(m:list[list[int]])->bool:
    for fila in m:
        for i in range(0,len(fila)):
            comp = fila[i]
            for j in range(i+1,len(fila)):
                if comp == fila[j]:
                    return False
    return True