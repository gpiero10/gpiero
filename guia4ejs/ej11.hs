eaprox :: Int -> Float
eaprox n | n == 0 = 1
         | n > 0 = (1 / factorial n) + eaprox(n-1)

factorial :: Int -> Float
factorial n | n == 0 = 1
            | otherwise = fromIntegral n * (factorial (n-1))

e :: Float
e = eaprox 10
