pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

todosIguales ::  (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) = x == head xs && todosIguales xs

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs  

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (xs) = not(todosDistintos xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar x (xs) | pertenece x xs == False = xs
              | pertenece x xs == True = aux x xs

aux :: (Eq t) => t -> [t] -> [t] 
aux n (x:xs) | n == x = xs
             | otherwise = x: aux n xs                      

quitartodos :: (Eq t) => t -> [t] -> [t]
quitartodos x (xs) | pertenece x (xs) == False = xs
                   | pertenece x (xs) == True = aux1 x xs 

aux1 :: (Eq t) => t -> [t] -> [t]
aux1 x (xs) | pertenece x (quitar x (xs)) == False = quitar x (xs)
            | pertenece x (quitar x (xs)) == True = aux1 x (quitar x (xs))

eliminarRepetidos :: (Eq t) => [t] -> [t]   
eliminarRepetidos (xs) | hayRepetidos xs == False = xs
                       | hayRepetidos xs == True = aux2 xs

aux2 :: (Eq t) => [t] -> [t] 
aux2 (x:xs) | pertenece x (xs) == False = aux2 (xs)
            | pertenece x (xs) == True && hayRepetidos (quitartodos x (x:xs)) == False = x:quitartodos x (x:xs)
            | pertenece x (xs) == True && hayRepetidos (quitartodos x (x:xs)) == True = x:aux2(quitartodos x (x:xs)) 

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (xs) (ys) | hayRepetidos (xs) == False && hayRepetidos (ys) == False = auxii (xs) (ys)
                          | hayRepetidos (xs) == True && hayRepetidos (ys) == False = auxii (eliminarRepetidos xs) (ys)
                          | hayRepetidos (xs) == False && hayRepetidos (ys) == True = auxii (xs) (eliminarRepetidos ys)
                          | hayRepetidos (xs) == True && hayRepetidos (ys) == True = auxii (eliminarRepetidos xs) (eliminarRepetidos ys) 

auxii :: (Eq t) => [t] -> [t] -> Bool
auxii [ ] (ys) = True
auxii (x:xs) (ys) | pertenece x ys == False = False
                  | pertenece x ys == True  = auxii (xs) (ys)

capicua :: (Eq t) => [t] -> Bool
capicua (xs) | (xs) == reverse(xs) = True
             | otherwise = False   




          
                  
                     
         




          
                  
                     
