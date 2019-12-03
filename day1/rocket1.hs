import AOC

getTotal :: [Integer] -> Integer
getTotal l = sum [ x `div` 3 - 2 | x <- l ]
