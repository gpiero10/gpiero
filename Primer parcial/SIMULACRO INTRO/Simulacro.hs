---Ejercicio 1)
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = False
relacionesValidas (x:[]) = fst x /= snd x
relacionesValidas (x:xs) | auxrelval x xs == True = relacionesValidas(xs)
                         | auxrelval x xs == False = False   
             

auxrelval :: (String, String) -> [(String, String)] -> Bool
auxrelval (a,b) [] = True
auxrelval (a,b) (x:xs) | a == b = False
                       | a == fst x && b == snd x || a == snd x && b == fst x = False
                       | otherwise = auxrelval (a,b) xs


---Ejercicio 2)
personas :: [(String, String)] -> [String] 
personas [] = []
personas (x:xs) | relacionesValidas(x:xs) == True = recursionista(auxpersonas(x:xs)) 

auxpersonas :: [(String, String)] -> [String]
auxpersonas (x:[]) = (fst x):[snd x]
auxpersonas (x:xs) = (fst x):(snd x):auxpersonas(xs)

eliminaTodos :: [String] -> [String] 
eliminaTodos (x:[]) = []
eliminaTodos (x:y:xs) | x /= y = y:eliminaTodos(x:xs)
                      | x == y = eliminaTodos(x:xs)

recursionista :: [String] -> [String]
recursionista [] = []
recursionista (x:[]) = [x]
recursionista (x:xs) = [x]++recursionista(eliminaTodos(x:xs))


---Ejercicio 3)
amigosDe :: String -> [(String, String)] -> [String] 
amigosDe a (xs) | pertenece (a) (personas(xs)) == True = eliminatodosconref a (auxamixers a (xs))
                | pertenece (a) (personas(xs)) == False = []

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece a [] = False
pertenece a (x:xs) | a == x = True
                   | a /= x = pertenece a (xs)

auxamixers :: String -> [(String, String)] -> [String] 
auxamixers a [] = []
auxamixers a (x:xs) | pertenece2 (a) (x) == True = fst x:snd x:auxamixers a (xs)
                    | pertenece2 (a) (x) == False = auxamixers a (xs)
            
pertenece2 :: (Eq t) => t -> (t,t) -> Bool
pertenece2 a (t1,t2) | a == t1 || a == t2 = True
                     | a /= t1 && a /= t2 = False

eliminatodosconref :: String -> [String] -> [String]
eliminatodosconref a [] = []
eliminatodosconref a (x:xs) | a == x && pertenece a (xs) == False = xs
                            | a == x && pertenece a (xs) == True = eliminatodosconref a (xs)    
                            | a /= x = x:eliminatodosconref a (xs) 


---Ejercicio 4)                                                 
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos (x:[]) = fst x
personaConMasAmigos (xs) = comparaegos(auxpersonas (xs))

contadordeapa :: String -> [String] -> Int
contadordeapa a [] = 0
contadordeapa a (x:xs) | a /= x = contadordeapa a (xs)
                       | a == x = 1 + contadordeapa a (xs) 
                      
comparaegos :: [String] -> String
comparaegos (x:[]) = x
comparaegos (x:y:xs) | contadordeapa x (x:y:xs) >= contadordeapa y (x:y:xs) = comparaegos (x:xs)
                     | contadordeapa x (x:y:xs) < contadordeapa y (x:y:xs) = comparaegos (y:xs)


inverso :: [Int] -> [Int]
inverso [] = []
inverso (x:xs) = inverso(xs)++[x]