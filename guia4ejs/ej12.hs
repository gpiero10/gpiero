raizDe2Aprox :: Int -> Float
raizDe2Aprox n = f (n) - 1

f :: Int -> Float
f n | n == 1 = 2
    | n > 1 = 2 + 1/(f(n-1))