holes = {(0, 0):None}
with open('input.txt') as inp:
    pos = (0, 0)
    for line in inp:
        dir, amount, color = line.strip().split()
        amount = int(amount)
        if dir == 'U':
            for _ in range(amount):
                pos = (pos[0], pos[1]+1)
                holes[pos] = color
        elif dir == 'D':
            for _ in range(amount):
                pos = (pos[0], pos[1]-1)
                holes[pos] = color
        elif dir == 'L':
            for _ in range(amount):
                pos = (pos[0]-1, pos[1])
                holes[pos] = color
        elif dir == 'R':
            for _ in range(amount):
                pos = (pos[0]+1, pos[1])
                holes[pos] = color

# Find boundary coords
big_y, big_x = -float('inf'), -float('inf')
small_y, small_x = float('inf'), float('inf')
for pos in holes:
    big_y = max(pos[1], big_y)
    big_x = max(pos[0], big_x)

    small_y = min(pos[1], small_y)
    small_x = min(pos[0], small_x)

def print_holes():
    with open('new_visual.txt', 'w') as visual:
        for y in range(big_y, small_y-1, -1):
            row = ''
            for x in range(small_x, big_x+1):
                if not (x, y) in holes and not (x, y) in new_holes:
                    row += '.'
                else:
                    row += '#'
            visual.write(row+'\n')

# RASTERISATION!!!
new_holes = set()
total = 0
for y in range(small_y, big_y+1):
    counting = False
    below = False
    above = False
    dug = False
    for x in range(small_x, big_x+1):
        if (x, y) in holes:
            # This is the start of a new line
            if not dug:
                above, below = False, False
                dug = True
            if (x, y+1) in holes:
                above = True
            if (x, y-1) in holes:
                below = True
        elif not (x, y) in holes:
            if dug and above and below:
                dug = False
                counting = not counting

            if counting:
                new_holes.add((x, y))

print(len(holes) + len(new_holes))
print_holes()