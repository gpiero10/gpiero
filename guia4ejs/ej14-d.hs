sumaPotencias :: Int ->Int ->Int ->Int
sumaPotencias q n m = q^((sumaux 1 n) + (sumaux 1 m))

sumaux :: Int ->Int ->Int
sumaux i k | i == k = k 
           | i < k = i + sumaux (i + 1) k