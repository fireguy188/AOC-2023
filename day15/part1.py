with open('input.txt') as inp: 
    words = inp.read().strip().split(',')

def hash(word):
    val = 0
    for char in word:
        val += ord(char)
        val *= 17
        val %= 256
    return val

total = 0
for word in words:
    total += hash(word)

print(total)