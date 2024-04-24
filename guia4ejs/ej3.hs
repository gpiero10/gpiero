esDivisible :: Int -> Int -> Bool
esDivisible x y | x > 0 && y > x = False
                | x > 0 && y == x = True             
                | x > 0 && y == 1 = True
                | x > 0 && y > 0 = esDivisible (x - y) y

               