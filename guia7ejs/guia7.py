
#Ejercicio 1)
#1)
def pertenece(x:list[int],y:int)->bool:
    for i in range(0,len(x),1):
        if (y == x[i]):
            return True
    return False
    
def pertenece_pt2(x:list[int],y:int)->bool:
    i:int = 0
    while (i<len(x)):
        if (y == x[i]):
            return True
        i += 1
    return False    

def pertenece_pt3(x:int, lista:list[int])->bool:
    i:int = len(lista)-1
    while i>=0:
        if (x == lista[i]):
            return True
        i -= 1
    return False 

#2)
def divide_a_todos(lista:list[int],x:int)->bool:
    for i in range(0,len(lista)):
        if lista[i] % x !=0:
            return False
    return True     

#3)
def sumatodos(lista:list[int])->int:
    acumulado:int = 0
    for i in range(0,len(lista)):
        acumulado += lista[i]
    return acumulado    
#4)
def ordenados(lista:list[int])->bool:
    for i in range(0,len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True 

#5)
def mayora7(lista:list[str])->bool:
    for i in range(0,len(lista)):
        if len(lista[i]) > 7:
            return True
    return False       

#6)
def es_palindromo(palabra:str)->bool:
    # Convertir la palabra a minúsculas y quitar los espacios
    palabra = palabra.lower().replace(" ", "")
    
    # Verificar si la palabra es igual a su reverso
    return palabra == palabra[::-1]

#7)
def contraseña_apta(contra:str)->str:
    if len(contra)<5:
        return("ROJO")
    elif len(contra) > 8 and hay_mayuscula(contra) == True and hay_minuscula(contra) == True and hay_numero(contra) == True:
        return("VERDE")
    else:
        return("AMARILL0")
                                       

def hay_mayuscula(palabra:str)->bool:
    for caracter in palabra:
        if caracter.isupper()==True:
            return True
    return False

def hay_minuscula(palabra:str)->bool:
    for caracter in palabra:
        if caracter.islower()==True:
            return True
    return False

def hay_numero(palabra:str)->bool:
    for caracter in palabra:
        if caracter.isnumeric()==True:
            return True
    return False

#8)
def historial_bancario(actividad:list[(str,int)])->int:
    saldo:int= 0
    for tupla in actividad:
        if tupla[0] == 'R':
            saldo -= tupla[1]
        elif tupla[0] == 'I':
            saldo += tupla[1]
    return saldo

#9)
def tresvocalesdist(palabra:str)->bool:
    i:int = 0
    for caracter in palabra:
        if caracter in ('a'):     
           i += 1
        elif caracter in ('e'):     
           i += 1
        elif caracter in ('i'):     
           i += 1      
        elif caracter in ('o'):     
           i += 1
        elif caracter in ('u'):     
           i += 1
    if i >= 3:
        return True
    else:
        return False
    
#EJERCICIO 2)
#1)
def borrapar_ponecero(lista:list[int])->list[int]:
    for i in range(0,len(lista),2):
        lista[i] = 0
    return lista    

#2)
def borrapar_ponecero_pt2(lista:list[int])->list[int]:
    res:list[int] = []
    for i in range(0,len(lista),1):
        if (i%2==0):
            res.append(0)
        else:
            res.append(lista[i])
    return res

#3)                       
def pertenecefin(x:list, y:chr)->bool:
    for c in x:
        if (y == c):
            return True
    return False

def borra_vocal(palabra:str)->str:
    concatenacion:str = ""
    for i in range(len(palabra)):
        if pertenecefin(['A','E','I','O','U','a','e','i','o','u'],palabra[i])==True:
            concatenacion = concatenacion
        else:
            concatenacion += palabra[i]
    return concatenacion

#4)
def reemplaza_vocal(palabra:list[chr])->list[chr]:
    concatenacion:str = ""
    for i in range(len(palabra)):
        if pertenecefin(['a','e','i','o','u'],palabra[i])==True:
            concatenacion += "_"
        else:
            concatenacion += palabra[i]
    return concatenacion

#5)
def da_vuelta_string(palabra:str)->str:
    res:str=""
    for i in range(0,len(palabra)):
        res += palabra[len(palabra)-i-1]
    return res

#6)
def eliminar_repetidos(palabra:str)->str:
    res:str = ""
    for i in range(0,len(palabra)):
        if (palabra[i] not in res):
            res += palabra[i]
    return res

#EJERCICIO 3)
def aprobado(notas:[int])->int:
    for nota in notas:
        if mayor_igual_a_4(notas) == True and promedio(notas) >= 7:
            return 1
        elif mayor_igual_a_4(notas) == True and (4 <= promedio(notas) < 7):
            return 2
        elif mayor_igual_a_4(notas) == False or promedio(notas) < 4:
            return 3
        
def mayor_igual_a_4(lista:[int])->bool:
    for i in range(0,len(lista)):
        if lista[i] < 4:
            return False
    return True
            
    
def promedio(lista:[int])->int:
    acumulado:int = 0
    for numero in lista:
        acumulado += numero
    res:int = (acumulado)//(len(lista))
    return res 

#EJERCICIO 4) INPUT TYPE EXERCISES
#1)
def estudiantes()->[str]:
    res:[str] = []
    nombre = ""
    while (nombre != "listo"):
        print("Ingrese los nombres: ")
        nombre=input()
        if nombre != "listo":
            res.append(nombre)
    return res
#2)

       
 
