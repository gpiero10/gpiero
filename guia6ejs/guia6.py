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
#1)
def peso_pino(altura: int)->int:
    if altura <= 3: 
       return altura*300
    else:
       return (altura - 3)*200 + 3*300 
print(peso_pino(5))
   
#2)
def es_peso_util(peso:int)->str:
    if 400<=peso<=1000:
       return("El peso sirve")
    else:
       return("El peso no sirve") 

print(es_peso_util(1001)) 
print(es_peso_util(399)) 
print(es_peso_util(777))

#3)
def sirve_pino(altura: int)->str:
    if 400<=peso_pino(altura)<=1000:
        return("Sirve")
    else:
        return("No sirve")
print(sirve_pino(5)) 
print(sirve_pino(3))  
print(sirve_pino(2))       

#4)
def sirve_pino_2(altura: int)->str:
    if es_peso_util(peso_pino(altura)) == "El peso sirve":
        return("Sirve el pino che")
    else:
        return("El pino no sirve chupapijas")
    
print(sirve_pino_2(4))
print(sirve_pino_2(2))

#Ejercicio 5)
#1)
def devolver_el_doble_si_es_par(numero:int)->int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero
    
print(devolver_el_doble_si_es_par(8))  

#2)
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int)->int:
    if numero % 2 == 0:
        return numero
    else:
        return (numero + 1) 
    
print(devolver_valor_si_es_par_sino_el_que_sigue(10))

#3)
def devolver_el_doble_si_es_multiplo_de_3_el_triple_si_es_multiplo_9(numero:int)->int:
    if numero % 9 == 0:
        return numero*3
    elif numero % 3 == 0:
        return numero*2
    else:
        return numero
print(devolver_el_doble_si_es_multiplo_de_3_el_triple_si_es_multiplo_9(9))
print(devolver_el_doble_si_es_multiplo_de_3_el_triple_si_es_multiplo_9(3))

#4)
def lindo_nombre(nombre:str)->str:
    if len(nombre) >= 5:
        return("Tu nombre tiene muchas letras!")
    else:
        return("Tu nombre tiene menos de 5 caracteres")       
print(lindo_nombre("Hatem"))   
print(lindo_nombre("Pier")) 

#5)
def elRango(numero:int)->str:
    if numero < 5:
        return("Menor a 5 (cuidado con Drake)")
    elif 10 <= numero <= 20:
        return ("Entre 10 y 20 (still cuidado con Drake)")
    elif numero > 20:
        return("Mayor a 20 (no temas a Drake)")

print(elRango(4))     
print(elRango(15))
print(elRango(69))

#6)
def cagaste_si(edad:int,sexo:str)->str:
    if (sexo == "Hombre" or sexo == "Mujer") and edad < 18:
        return("Anda de vacaciones pibe")
    elif sexo == "Hombre" and edad >= 65:
        return("Anda de vacaciones papucho")
    elif sexo == "Mujer" and edad >= 60:
        return("Anda de vacaciones mamucha")
    elif (sexo == "Hombre" or sexo == "Mujer") and edad >= 18 :
        return("Anda a laburar, gil laburante")   

print(cagaste_si(20,"Hombre"))
print(cagaste_si(65,"Hombre"))
print(cagaste_si(60,"Mujer"))

#Ejercicio 6)  
 
