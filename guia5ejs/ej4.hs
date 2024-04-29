--- Inciso A)
sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos [] = []
sacarEspaciosRepetidos (x:[])=[x]
sacarEspaciosRepetidos (x:y:xs) | x==y && x==' ' = sacarEspaciosRepetidos(y:xs)
                                | otherwise = x:(sacarEspaciosRepetidos(y:xs))

--- Inciso B)
contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x==' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs

sacarEspacioFin :: [Char] -> [Char]
sacarEspacioFin [] = []
sacarEspacioFin (x:[]) | x==' '=[] 
                       | otherwise = [x]
sacarEspacioFin (x:xs) = x:(sacarEspacioFin xs)

sacarEspacioInicio :: [Char] -> [Char]
sacarEspacioInicio [] = []
sacarEspacioInicio (x:xs) | x == ' ' = xs
                          | otherwise = (x:xs)

limpiarCadena :: [Char] -> [Char]
limpiarCadena xs = sacarEspacioInicio (sacarEspacioFin (sacarEspaciosRepetidos xs))

contarPalabras :: [Char] -> Integer
contarPalabras xs = contarEspacios (limpiarCadena xs) + 1

--- Inciso C) info: que dada una lista arma una nueva lista con las palabras de la lista original
sepiii :: [Char] -> [Char]
sepiii (xs) = separador(limpiarCadena(xs))

separador :: [Char] -> [Char]
separador []=[]
separador (x:y:xs) | x /= ' ' && y == ' ' = [x]
                   | otherwise =x:separador(y:xs)
