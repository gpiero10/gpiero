sumubi :: Int -> Int -> Int
sumubi n m = auxi1 (1) (1) (n) (m)  

auxi1 :: Int -> Int -> Int -> Int -> Int
auxi1 i j n m | j == m && i == n = n^(m)
              | j < m && i == n = i^(j) + auxi1 n (j+1) n m 
              | j == m && i < n = i^(m) + auxi1 (i+1) (1) (n) (m) 
              | j < m && i < n = i^j + auxi1 i (j+1) n m
              | j == 1 && i == 1 = 1^1 + auxi1 i (j+1) n m
              | n == 0 = 0

