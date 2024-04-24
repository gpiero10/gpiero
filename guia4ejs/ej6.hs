sumaDigitos :: Integer ->Integer
sumaDigitos x | x >= 0 && x <= 9 = x
              | x >= 10 && x < 100 = div x 10 + mod x 10
              | x >= 100 = mod x 10 + sumaDigitos (div x 10)
              