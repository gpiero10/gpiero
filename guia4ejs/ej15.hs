sumaRacionales :: Int -> Int -> Float
sumaRacionales n m = aux (1) (1) (n) (m) 

aux :: Int -> Int -> Int -> Int -> Float
aux p q n m | q == m && p == n = (fromIntegral n :: Float) / (fromIntegral m :: Float)
            | q < m && p == n = val + aux (p) (q+1) (n) (m) 
            | q == m && p < n = val + aux (p+1) (1) (n) (m) 
            | q < m && p < n = val + aux (p) (q+1) (n) (m)
            | q == 1 && p == 1 = 1 + aux (p) (q+1) (n) (m)
            | n == 0 = 0
            where val = (fromIntegral p :: Float) / (fromIntegral q :: Float)