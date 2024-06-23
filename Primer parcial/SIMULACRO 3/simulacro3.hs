import Data.Bits (Bits(xor))
---Ejercicio 1)
votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco _ [] n = n
votosEnBlanco (xs) (ys) n = n - sumadevotos(ys) 

sumadevotos :: [Int] -> Int
sumadevotos (x:[]) = x
sumadevotos (x:xs) = x + sumadevotos(xs)


---Ejercicio 2)
formulasValidas :: [(String, String)] -> Bool
formulasValidas (x:[]) = True
formulasValidas (xs) = esValida(aplanador(xs))

aplanador :: [(String, String)] -> [String]
aplanador [] = []
aplanador (x:[]) = fst x:snd x:aplanador[]
aplanador (x:xs) = fst x:snd x:aplanador(xs) 

hayrepetidosconrefe :: String -> [String] -> Bool
hayrepetidosconrefe a [] = False
hayrepetidosconrefe a (x:xs) | a == x = True
                             | a /= x = hayrepetidosconrefe a (xs)

esValida :: [String] -> Bool
esValida (x:[]) = True
esValida (x:xs) | hayrepetidosconrefe x xs == True = False
                | hayrepetidosconrefe x xs == False = esValida(xs)         


---Ejercicio 3) 
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos _ [] [] = 0
porcentajeDeVotos a (xs) (ys) = 100*division (votoasoc(encuentratripla a (asociador xs ys))) (sumadevotos ys)

asociador :: [(String,String)] -> [Int] -> [(String,String,Int)] 
asociador [] [] = []
asociador (x:xs) (y:ys) = creatripla x y:asociador(xs) (ys) 

creatripla :: (String,String) -> Int -> (String,String,Int)
creatripla (a,b) c = (a,b,c)

encuentratripla :: String -> [(String,String,Int)] -> (String,String,Int)
encuentratripla a (x:xs) | a == primero x = x
                         | a /= primero x = encuentratripla a xs

primero :: (String,String,Int) -> String
primero (a,b,c) = a

votoasoc :: (String,String,Int) -> Int
votoasoc (a,b,c) = c

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

---Ejercicio 4)
proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente (xs) (ys) = whoTheGoat(asociador xs ys)

whoTheGoat :: [(String,String,Int)] -> String
whoTheGoat (x:[]) = primero x
whoTheGoat (x:y:xs) | votoasoc x >= votoasoc y = whoTheGoat (x:xs)
                    | votoasoc x < votoasoc y = whoTheGoat (y:xs)

    