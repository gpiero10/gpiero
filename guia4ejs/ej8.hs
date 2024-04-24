iesimoDigito :: Int ->Int ->Int
iesimoDigito x i | x>= 0 && i >= 1 && i <= cantDigitos(x) = mod (div (x) (10^(cantDigitos(x) - i))) (10)
                 | otherwise = cantDigitos(mod x 10)   

cantDigitos :: Int -> Int
cantDigitos x | x == 0 = 1
              | x > 0 && x < 10 = div (x) (10) + 1
              | x >= 10 = 1 + cantDigitos(div x 10)   