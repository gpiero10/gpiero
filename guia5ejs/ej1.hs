longitud :: [t] -> Integer 
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo (xs) = last xs

principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x : principio xs

reverso :: [t] -> [t]
reverso (xs) = reverse xs 

