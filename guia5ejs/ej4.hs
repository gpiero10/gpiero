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
primerpalabra :: [Char] -> [Char]
primerpalabra []=[]
primerpalabra [x]=[x]
primerpalabra (x:y:xs) | x /= ' ' && y == ' ' = [x] 
                       | x /= ' ' && y /= ' '  = x:primerpalabra(y:xs)

sacarprimerpalabra :: [Char] -> [Char]
sacarprimerpalabra [x] = []
sacarprimerpalabra (x:y:xs) | x /= ' ' && y == ' ' = (xs)
                            | x /= ' ' && y /= ' '  = sacarprimerpalabra(y:xs)

palabras :: [Char] -> [[Char]] --que dada una lista arma una nueva lista con las palabras de la lista original
palabras (x:[]) = [[x]]
palabras (xs) = primerpalabra(limpiarCadena(xs)):palabras(sacarprimerpalabra(limpiarCadena xs))
