vertical_lines = set()
horizontal_lines = set()
with open('input.txt') as inp:
    pos = (0, 0)
    for line in inp:
        dir, amount, color = line.strip().split()
        # amount = int(amount)
        # if dir == 'R':
        #     dir = '0'
        # elif dir == 'L':
        #     dir = '2'
        # elif dir == 'U':
        #     dir = '3'
        # elif dir == 'D':
        #     dir = '1'

        # Only color matters now
        amount = int(color[2:7], 16)
        dir = color[-2]
        if dir == '0':
            horizontal_lines.add((pos, (pos[0]+amount, pos[1])))
            pos = (pos[0]+amount, pos[1])
        elif dir == '1':
            vertical_lines.add(((pos[0], pos[1]-amount), pos))
            pos = (pos[0], pos[1]-amount)
        elif dir == '2':
            horizontal_lines.add(((pos[0]-amount, pos[1]), pos))
            pos = (pos[0]-amount, pos[1])
        elif dir == '3':
            vertical_lines.add((pos, (pos[0], pos[1]+amount)))
            pos = (pos[0], pos[1]+amount)

# Find boundary coords
small_y, big_y = float('inf'), -float('inf')
for line in vertical_lines:
    big_y = max(line[0][1], line[1][1], big_y)
    small_y = min(line[0][1], line[1][1], small_y)

total = 0
for y in range(small_y, big_y+1):
    if y % 100000 == 0:
        print(f'{y} / {big_y}')
    counting = False
    passes_through = []
    for line in vertical_lines:
        if line[0][1] <= y <= line[1][1]:
            passes_through.append(line)
    
    passes_through.sort(key = lambda x: x[0][0])
    counting = False
    old_total = total
    lines_included = set()
    for l in range(len(passes_through)-1):
        l1, l2 = passes_through[l], passes_through[l+1]
        continuing = False
        if y == l1[0][1] == l2[0][1] or y == l1[1][1] == l2[1][1]:
            for line in horizontal_lines:
                if line[0][1] == y and line[0][0] == l1[0][0] and line[1][0] == l2[0][0]:
                    counting = not counting
                    total += l2[0][0] - l1[0][0] + 1 - (l1 in lines_included)
                    lines_included.add(l1)
                    lines_included.add(l2)
                    continuing = True
                    break
        elif y == l1[0][1] == l2[1][1] or y == l1[1][1] == l2[0][1]:
            for line in horizontal_lines:
                if line[0][1] == y and line[0][0] == l1[0][0] and line[1][0] == l2[0][0]:
                    total += l2[0][0] - l1[0][0] + 1 - (l1 in lines_included)
                    lines_included.add(l1)
                    lines_included.add(l2)
                    continuing = True
                    break

        if continuing:
            continue

        counting = not counting
        if counting:
            total += l2[0][0] - l1[0][0] + 1 - (l1 in lines_included)
            lines_included.add(l1)
            lines_included.add(l2)

print(total)
