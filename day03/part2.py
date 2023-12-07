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

        matches = re.finditer('\*', line)
        for m in matches:
            symbols.append((row, m.start(0)))
    
    numbers_gears = {}
    for number in numbers:
        numbers_gears[number] = set()
        row, (start, end) = number
        adj = adjacent(row, start, end)
        for i in adj:
            if i in symbols:
                numbers_gears[number].add(i)
    
for n1 in numbers_gears:
    for n2 in numbers_gears:
        if n1 != n2 and n1 < n2:
            if len(numbers_gears[n1].intersection(numbers_gears[n2])) >= 1:
                total += int(inp[n1[0]][n1[1][0]:n1[1][1]]) * int(inp[n2[0]][n2[1][0]:n2[1][1]])

print(total)