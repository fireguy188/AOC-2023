import re

with open('input.txt') as inp: 
    words = inp.read().strip().split(',')

def hash(word):
    val = 0
    for char in word:
        val += ord(char)
        val *= 17
        val %= 256
    return val

boxes = [{} for x in range(256)]
for word in words:
    lens = re.search('\w+', word).group(0)
    box = hash(lens)
    if word[-1] == '-':
        if lens in boxes[box]:
            del boxes[box][lens]
    else:
        focal = int(word.split('=')[1])
        boxes[box][lens] = focal

total = 0
for box in range(len(boxes)):
    focals = list(boxes[box].values())
    for slot in range(len(focals)):
        total += (box+1) * (slot+1) * focals[slot]
print(total)