import math
#Ejercicio 1
#A)
def imprimir_hola_mundo() -> None:
 print("¡Hola mundo!")
print(imprimir_hola_mundo())
#B)   
def imprime_un_verso() -> None:
 print("Baby we livin the moment\nIm aware im a king\n4am in the morning and im zonin")
print(imprime_un_verso())
#C)    
def raizDe2() -> float: 
    return round(math.sqrt(2),4)
print(raizDe2())
#D)
def factorial_de_2() -> int:
    return math.factorial(2)
print(factorial_de_2())
#E)  
def perimetro() -> float:
    return (math.pi)* 2
print(perimetro())

#Ejercicio 2
#1)
def imprimir_saludo(nombre:str) -> None:
    print("Hola "+nombre+", Chupapijas")

imprimir_saludo("hatem")
#2)
def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)
    
print(raiz_cuadrada_de(16))
print(raiz_cuadrada_de(64))
print(raiz_cuadrada_de(13))

#3)
def farenheit_a_Celsius(temp_far: float) -> float:
    return ((temp_far - 32)*5)/9
print(farenheit_a_Celsius(271))

#4)
def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo*2)
print(imprimir_dos_veces("Let's have a toast for the assholes"))   

#5) 
def es_multiplo_de(n: float, m: float) -> bool:
    if m % n == 0:
       return True
    else:
        return False        
print(es_multiplo_de(2, 4))
print(es_multiplo_de(4, 4))
print(es_multiplo_de(10, 50))
#6)
def es_par(numero: int) -> bool:
    if es_multiplo_de(2, numero) == True:
        return True
    else:
        return False 
print(es_par(20))    
print(es_par(21))
print(es_par(103))
  
#7)
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    print(math.ceil((comensales*min_cant_de_porciones)/8))   
    
print(cantidad_de_pizzas(4,2))  

#Ejercicio 3)
#1)
def alguno_es_cero(numero1:float, numero2:float)->bool:
    return (numero1==0) or (numero2==0)

print(alguno_es_cero(0.1,0.2))

#2)
def ambos_son_cero(numero1:float, numero2:float)->bool:
    return (numero1==0) and (numero2==0)

print(ambos_son_cero(0,0))

#3)
def es_nombre_largo(nombre: str)-> bool:
    return 3<=len(nombre)<= 8

print(es_nombre_largo("Hatem"))
print(es_nombre_largo("Gi"))      

#4)
def es_bisiesto(año: int)-> bool:
    return año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)  

print(es_bisiesto(2024))      
print(es_bisiesto(2023))     

#Ejercicio 4)
 