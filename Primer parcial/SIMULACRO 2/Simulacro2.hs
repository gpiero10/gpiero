import Data.Bits (Bits(xor))
---Ejercicio 1)
atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes (x:xs) (ys) n | n >= golesatitulares ys = n - golesatitulares ys 

golesatitulares :: [Int] -> Int
golesatitulares (x:[]) = x
golesatitulares (x:xs) = x + golesatitulares(xs)

---Ejercicio 2)
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = False
equiposValidos (xs) = todosref(aplanadora xs)

aplanadora :: [(String, String)] -> [String]
aplanadora (x:[]) = fst x:[snd x]
aplanadora (x:xs) = fst x:snd x:aplanadora(xs)

hayrepesconref :: String -> [String] -> Bool
hayrepesconref a [] = False
hayrepesconref a (x:xs) | a == x = True
                        | a /= x = hayrepesconref a (xs)

todosref :: [String] -> Bool
todosref (x:[]) = True
todosref (x:xs) | hayrepesconref x xs == True = False
                | hayrepesconref x xs == False = todosref(xs)   

---Ejercicio 3)  
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles a (xs) (ys) = 100*division (auxi a (xs) (ys)) (golesatitulares ys)

auxi :: String -> [(String, String)] -> [Int] -> Int  
auxi a (xs) (ys) = ultimo(encuentratripla a (asociador xs ys))

asociador :: [(String, String)] -> [Int] -> [(String, String, Int)]
asociador [] [] = []
asociador (x:xs) (y:ys) = creatripla x y:asociador (xs) (ys)   
 
creatripla :: (String, String) -> Int -> (String, String, Int)
creatripla (a,b) n = (a,b,n)

encuentratripla :: String -> [(String, String, Int)] -> (String, String, Int)
encuentratripla a [] = ("no","hay",0)
encuentratripla a (x:xs) | a == segundo x = x
                         | a /= segundo x = encuentratripla a (xs)

segundo :: (String, String, Int) -> String
segundo (a,b,c) = b

ultimo :: (String, String, Int) -> Int
ultimo (a,b,c) = c

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

--- Ejercicio 4)
vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida (xs) (ys) = menosgoleado(asociador (xs) (ys))

menosgoleado ::  [(String, String, Int)] -> String
menosgoleado (x:[]) = segundo x
menosgoleado (x:y:xs) | ultimo x <= ultimo y = menosgoleado(x:xs)
                      | ultimo x > ultimo y = menosgoleado(y:xs) 