sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

sumarN :: Int -> [Int] -> [Int]
sumarN n [] = []
sumarN n (x:xs) = (n + x):sumarN n (xs)       

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero (x:xs) = x+x:sumarN  x xs

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo (xs) = sumarN (head(reverse xs)) (xs)

pares :: [Int] -> [Int] 
pares [] = []
pares (x:xs) | mod x 2 == 0 = x:pares(xs) 
             | otherwise = pares(xs)

multiplosDeN :: Int -> [Int] -> [Int]              
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:multiplosDeN n (xs) 
                      | mod x n /= 0 = multiplosDeN n (xs)

ordenar :: [Int] -> [Int] 
ordenar [] = []
ordenar [x] = [x]
ordenar (xs) = minimo(xs):ordenar(quitar (minimo xs) (xs))

minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:xs) | x < y = minimo (x:xs)
                | otherwise = minimo (y:xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar x (xs) | pertenece x xs == False = xs
              | pertenece x xs == True = aux x xs

aux :: (Eq t) => t -> [t] -> [t] 
aux n (x:xs) | n == x = xs
             | otherwise = x: aux n xs    

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs                          


            