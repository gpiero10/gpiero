#EJERCICIO 1)
#1.1)
def cant_lineas(archivo)->int:
    f = open(archivo)
    return len(f.readlines())
    f.close()
    
#1.2)
def pertenece(palabra:str,archivo)->bool:
    f = open(archivo)
    t = f.readlines()
    comp = ""
    for linea in t:
        for caracter in linea:
            if caracter != " " and caracter != "\n":
                comp += caracter
            else:
                if comp == palabra:
                    return True
                    f.close()
                else:
                    comp = ""
    f.close()
    return False

#1.3)
def cantidad_apariciones(palabra:str,archivo)->int:
    f = open(archivo)
    res:int = 0
    t = f.readlines()
    comp = ""
    if (pertenece(palabra,archivo) == False):
        return 0
    if (pertenece(palabra,archivo) == True):
        for linea in t:
            for caracter in linea:
                if caracter != " " and caracter != "\n":
                    comp += caracter
                else:
                    if comp == palabra:
                        res += 1
                        comp = ""
                    else:
                        comp = ""
    f.close()
    return res
             
#Ejercicio 2
def clonar_sincoments(archivo:str):
    f = open(archivo)
    lineas:list[str] = f.readlines()
    res = open("res.txt",'w')
    for linea in lineas:
        if es_linea_valida(borra_espacios_en_blanco(linea)) == True:
            res.write(linea)
    f.close()
    res.close()
    
def borra_espacios_en_blanco(linea:str)->str:
    res:str = ""
    for i in range(0,len(linea)):
        if linea[i] != " ":
            res += linea[i]
    return res

def es_linea_valida(linea:str)->bool:
    if linea[0] != "#":
        return True
    return False

#Ejercicio 3) problema en la ultima linea
def invertir_lineas(archivo:str):
    f = open(archivo)
    lineas:list[str] = f.readlines()
    res = open("reverso.txt",'w')
    for i in range(len(lineas)-1,-1,-1):
        res.write(lineas[i])
    f.close()
    res.close()
    
#Ejercicio 4)
def agregar_frase_al_final(archivo:str,frase:str):
    f = open(archivo,'a')
    f.write(" "+frase)
    f.close()

#Ejercicio 5)   
def agregar_frase_al_principio(archivo:str,frase:str):
    f = open(archivo,'r')
    lineas = [frase+"\n"]+f.readlines()
    f.close()
    f = open(archivo,'w')
    for linea in lineas:
        f.write(linea) 
    f.close()
    
#Ejercicio 6)

#Ejercicio 7) si no le meto enter a la ultima linea, el ultimo elemento no se agrega (CONSULTAR)
def promedio_estudiante(archivo,lu:str)->float:
    f = open(archivo)
    lineas = f.readlines()
    dataenlineas:list[list[str]] = []
    for linea in lineas:
        datadelalumno:list[str] = []
        data:str = ""    
        for caracter in linea:
            if caracter != "," and caracter != "\n":
                data += caracter
            if caracter == ",":
                datadelalumno.append(data)
                data = ""
            if caracter == "\n":
                datadelalumno.append(data)
                dataenlineas.append(datadelalumno)
            if data != "":
                datadelalumno.append(data)
    f.close()   
    cantmaterias:float = 0
    sumatoriadenotas:float = 0
    for datapersonal in dataenlineas:
        if lu == datapersonal[0]:
            sumatoriadenotas += float(datapersonal[3])
            cantmaterias += 1
    promedio:float = ((sumatoriadenotas)//(cantmaterias))
    return promedio

#Ejercicio 8) PILAS
from queue import LifoQueue as Pila
import random

def generar_num_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    res:Pila[int] = []
    i:int = 0
    while i < cantidad:
        res.append(random.randint(desde,hasta))
        i += 1
    return res

#Ejercicio 9)
def cant_elem(p:Pila)->int:
    res = 0
    contenido = []
    while p.empty() != True:
        contenido.append(p.get())
        res += 1
    for elemento in contenido[::-1]:
        p.put(elemento)
    return res

#EJERCICIO 10)
def maximo(p:Pila[int])->int:
    lista:list[int] = []
    while p.empty() != True:
        lista.append(p.get())
    for elemento in lista[::-1]:
        p.put(elemento)
    return maxp(lista)
    
def maxp(lista:list[int]):
    res = lista[0]
    for i in range(1, len(lista)):
        if res < lista[i]: 
            res = lista[i]
    return res

#EJERCICIO 11)

#EJERCICIO 12)
def evaluar_expresion(exp:str)->float:
    i = 0
    elem = ""
    lista = []
    while i < len(exp):
        if exp[i] == " ":
            lista.append(elem)
            elem = ""
            i += 1
        else:
            elem += exp[i]
            i += 1
    if elem != "": 
        lista.append(elem)
    p = Pila()
    for elem in lista:
        if elem == "+":
            a = p.get()
            b = p.get()
            p.put(float(a)+float(b))
        elif elem == "-":
            a = p.get()
            b = p.get()
            p.put(float(b)-float(a))
        elif elem == "/":
            a = p.get()
            b = p.get()
            p.put(float(b)/float(a))
        elif elem == "*":
            a = p.get()
            b = p.get()
            p.put(float(a)*float(b))                
        else:
            p.put(elem)
    return p.get() 

#EJERCICICO 13) COLAS
from queue import Queue as Cola
import random

def gnum(cantidad:int,desde:int,hasta:int)->Cola[int]:
    res:Cola[int] = Cola()
    i:int = 0
    while i < cantidad:
        res.put(random.randint(desde,hasta))
        i += 1
    return res

#EJERCICIO 14)
def cant_elem_pt2(c:Cola)->int:
    res:int = 0
    contenido:list[int] = []
    while c.empty() != True:
        contenido.append(c.get())
        res += 1
    for elemento in contenido:
        c.put(elemento)
    return res

#DICCIONARIO EJEMPLO: d = {"Messi":8,"Neymar":0}

#EJERCICIO 15)
def busco_maximo(c:Cola[int])->int:
    lista = []
    while c.empty() != True:
        lista.append(c.get())
    for elemento in lista:
        c.put(elemento)
    return maxp(lista)

#EJERCICIO 16)
import random
def armar_secuencia_de_bingo()->Cola[int]:
    lista = []
    i = 0
    cola:Cola[int] = Cola()
    while i <= 99:
        lista.append(i)
        i += 1
    random.shuffle(lista) 
    for elemento in lista:
        cola.put(elemento)  
    return cola

#def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:

#EJERCICIO 17)
def n_pacientes_urgentes(c:Cola[(int,str,str)])->int:
    lista:list[(int,str,str)] = []
    contador = 0
    while c.empty() != True:
        lista.append(c.get())
    ye = rebana(lista)
    for listita in ye:
        if 1 <= listita[0] <= 3:
            contador += 1
    for elemento in lista:
           c.put(elemento)
    return contador
    
# REBANADOR FUNCION AUXILIAR
def rebana(l:[(int,str,str)])->list[list[int,str,str]]:
    rebanados:list[list[int,str,str]] = []
    listita:list[int,str,str] = []
    for elemento in l:
        for valor in elemento:
            listita.append(valor)
        rebanados.append(listita)
        listita = []  
    return rebanados
#FIN REBANADOR

#EJERCICIO 18)
def atencion_a_clientes(c:Cola[(str,int,bool,bool)])->Cola[(str,int,bool,bool)]:
    lista = []
    lista_prioridad:list[(str,int,bool,bool)] = []
    lista_preferencial:list[(str,int,bool,bool)] = []
    lista_resto:list[(str,int,bool,bool)] = []
    lista_ordenada:list[(str,int,bool,bool)] = []
    res:Cola[(str,int,bool,bool)] = Cola()
    while c.empty() != True:
        lista.append(c.get())
    for elemento in lista:
        if elemento[3] is True:
            lista_prioridad.append(elemento)
        elif elemento[2] is True: 
            lista_preferencial.append(elemento)
        else:
            lista_resto.append(elemento)
    lista_ordenada = lista_prioridad + lista_preferencial + lista_resto
    for elemento in lista_ordenada:
        res.put(elemento)
    for elemento in lista:
        c.put(elemento)
    while res.empty() != True:
        print(res.get())

#EJERCICIO 19)
def agrupar_por_longitud(archivo:str)->dict:
    f = open(archivo)
    lineas = f.readlines()
    #Rebanador
    lista:list[str] = []
    palabra = ""
    for linea in lineas:
        for caracter in linea:
            if caracter == " " or caracter == "\n":
                lista.append(palabra)
                palabra = ""
            else:
                palabra += caracter
    if palabra != "":
        lista.append(palabra)
    #FIN REBANADOR
    diccionario:dict = {}
    for palabra in lista:
        if len(palabra) in diccionario:
            diccionario[len(palabra)] += 1
        else:
            diccionario[len(palabra)] = 1
    return diccionario

#EJERCICIO 20)
def calcular_promedio_por_estudiante(archivo_de_notas:str)->dict[str,float]:
    f = open(archivo_de_notas)
    lineas = f.readlines()
    #Rebanador
    lista_de_todos:list[list[str]] = []
    lista_por_alumno:list[str] = []
    palabra = ""
    for linea in lineas:
        for caracter in linea:
            if caracter == "," or caracter == "\n":
                lista_por_alumno.append(palabra)
                palabra = ""
            else:
                palabra += caracter
        if palabra != "":
            lista_por_alumno.append(palabra)
        lista_de_todos.append(lista_por_alumno)
        lista_por_alumno:list[str] = []
    #FIN REBANADOR
    #Lu´s unicos
    lu_uses:list[str] = []
    for elemento in lista_de_todos:
        if pertenece(elemento[0],lu_uses) != True:
             lu_uses.append(elemento[0])
    #FIN Lu´s unicos
    diccionario_de_notas:dict[str,float] = {}
    for elemento in lista_de_todos:
        if not elemento[0] in diccionario_de_notas:
            diccionario_de_notas[elemento[0]] = float(elemento[3])
        else:
            diccionario_de_notas[elemento[0]] += float(elemento[3])
    diccionario_de_materias:dict[str,int] = {}
    for elemento in lista_de_todos:
        if not elemento[0] in diccionario_de_materias:
            diccionario_de_materias[elemento[0]] = 1
        else:
            diccionario_de_materias[elemento[0]] += 1
    diccionario_total:dict[str,float] = {}
    for lu in lu_uses:
        diccionario_total[lu] = float(diccionario_de_notas[lu])/float(diccionario_de_materias[lu])
    return diccionario_total
        
def pertenece(y:str,x:list[str])->bool:
    for i in range(0,len(x)):
        if y == x[i]:
            return True
    return False

#EJERCICIO 21)
def la_palabra_mas_frecuente(archivo:str)->str:
    f = open(archivo)
    lineas = f.readlines()
    #REBANAR
    lista:list[str] = []
    palabra:str = ""
    for linea in lineas:
        for caracter in linea:
            if caracter == " " or caracter == "\n" or caracter == ",":
                lista.append(palabra)
                palabra:str = ""
            else:
                palabra += caracter
    if palabra != "":
        lista.append(palabra)    
    #FIN REBANAR
    diccionario:dict[str,int] = {}
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    res:str = ""
    for clave in diccionario:
        if res == "":
            res = clave
        elif diccionario[clave] > diccionario[res]:
            res = clave
    return res

#EJERCICIO 22)
historiales:dict[str,Pila[str]] = {}
#2)
def visitar_sitio(historiales:dict[str,Pila[str]], usuario:str, sitio: str):
    sitios:Pila[str] = Pila()
    sitios.put(sitio)
    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        historiales[usuario] = sitios

#3)
def navegar_atras(historiales:dict[str,Pila[str]], usuario:str):
    lista:list[str] = []
    while historiales[usuario].empty() != True:
        lista.append(historiales[usuario].get())
    for i in range(len(lista)-1,0,-1):
        historiales[usuario].put(lista[i])

#EJERCICIO 23)
