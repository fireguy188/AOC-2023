import Data.Maybe (fromJust, isJust)

translate :: String -> Int
translate "1" = 1
translate "2" = 2
translate "3" = 3
translate "4" = 4
translate "5" = 5
translate "6" = 6
translate "7" = 7
translate "8" = 8
translate "9" = 9
translate "one" = 1
translate "two" = 2
translate "three" = 3
translate "four" = 4
translate "five" = 5
translate "six" = 6
translate "seven" = 7
translate "eight" = 8
translate "nine" = 9

substr :: String -> String -> Maybe Int
substr s1 s2 = substr' s1 s2 0
  where
    substr' s1 s2 acc
      | length s1 > length s2 = Nothing
      | take (length s1) s2 == s1 = Just acc
      | otherwise = substr' s1 (tail s2) (acc + 1)

firstDigitp1 :: String -> Int
firstDigitp1 xs = translate $ snd $ minimum [(fromJust pos, digit) | digit <- digits, let pos = substr digit xs, isJust pos]
  where
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

lastDigitp1 :: String -> Int
lastDigitp1 xs = firstDigitp1 (reverse xs)

part1 :: String -> Int
part1 input = sum [firstDigitp1 line * 10 + lastDigitp1 line | line <- lines input]

firstDigitp2 :: String -> Int
firstDigitp2 xs = translate $ snd $ minimum [(fromJust pos, digit) | digit <- digits, let pos = substr digit xs, isJust pos]
  where
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

lastDigitp2 :: String -> Int
lastDigitp2 xs = (translate . reverse) $ snd $ minimum [(fromJust pos, digit) | digit <- digits, let pos = substr digit revxs, isJust pos]
  where
    digits = map reverse ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    revxs = reverse xs

part2 :: String -> Int
part2 input = sum [firstDigitp2 line * 10 + lastDigitp2 line | line <- lines input]

main = do
  input <- readFile "input.txt"
  print (part1 input)
  print (part2 input)