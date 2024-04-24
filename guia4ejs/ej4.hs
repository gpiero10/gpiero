sumaImpares :: Int -> Int
sumaImpares 0 = 0
sumaImpares x = (2*x - 1) + sumaImpares (x - 1) 