f1 ::Int -> Int
f1 x | x == 0 = 1
     | x == 1 = 3
     | x > 1 = 2^(x) + f1 (x - 1)   

f2 :: Int -> Float -> Float
f2 n q | q == 0 = 0
       | n == 0 = 0
       | n == 1 = q
       | n == 2 = q + q^2 
       | n > 2 = q^(n) + f2 (n - 1) (q)   

f3 :: Int -> Float -> Float
f3 n q | q == 0 = 0
       | n == 0 = 0
       | n == 1 = q
       | n == 2 = q + q^2 + q^3 + q^4
       | n > 2 = q^(2*n) + f2 (2*n - 1) (q)  

f4 :: Int -> Float -> Float
f4 n q = f4Aux n (2*n) q 

f4Aux :: Int -> Int -> Float -> Float
f4Aux i n q | i == n = q^i 
            | otherwise = q^i + f4Aux (i+1) n q