#1)
def contar_lineas(archivo:str)->int:
    f = open(archivo)
    return len(f.readlines())

#2)
#def existe_palabra(palabra) 

def pertenecefin(x:list, y:chr)->bool:
    for c in x:
        if (y == c):
            return True
    return False

def separador(lista:[str])->[str]:
    res:[str] = []
    palabra:str = ""
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
           if lista[i][j] != " ":
            palabra += lista[i][j]
           if lista[i][j] == " ": 
            res.append(palabra)
    return res
