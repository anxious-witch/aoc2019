import AOC

getFuel :: Integer -> Integer
getFuel n
  | n <= 0      = 0
  | otherwise   = n + getFuel(n `div` 3 - 2)

getFuelTotal :: [Integer] -> Integer
getFuelTotal l = sum [ getFuel x - x | x <- l ]
