import re

def adjacent(row, start, end):
    ans = []
    ans.append((row, start-1))
    ans.append((row, end))
    for x in range(start, end):
        ans.append((row-1, x))
        ans.append((row+1, x))
    
    ans.append((row+1, start-1))
    ans.append((row+1, end))
    ans.append((row-1, end))
    ans.append((row-1, start-1))
    
    return ans

total = 0
with open('input.txt') as inp:
    numbers = []
    symbols = []

    inp = inp.read().split('\n')
    for row, line in enumerate(inp):
        line = line.strip()

        matches = re.finditer('\d+', line)
        for m in matches:
            numbers.append((row, (m.start(0), m.end(0))))

        matches = re.finditer('[^.\d]', line)
        for m in matches:
            symbols.append((row, m.start(0)))
    
    for number in numbers:
        row, (start, end) = number
        adj = adjacent(row, start, end)
        for i in adj:
            if i in symbols:
                total += int(inp[row][start:end])
                break
    
print(total)