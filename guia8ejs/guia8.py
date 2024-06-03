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
