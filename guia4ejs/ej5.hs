midfac :: Int -> Int
midfac x | x == 0 = 1
         | x == 1 = 1   
         | x >= 0 = x * midfac (x-2)  