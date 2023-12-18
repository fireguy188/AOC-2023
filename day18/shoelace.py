positions = []
with open('input.txt') as inp:
    lines = inp.readlines()

pos = (0, 0)
perimeter = 0
for line in lines:
    dir, amount, color = line.strip().split()
    amount = int(amount)

    # Only color matters now
    amount = int(color[2:7], 16)
    dir = color[-2]
    dir = ['R', 'D', 'L', 'U'][int(dir)]
    perimeter += amount

    if dir == 'R':
        pos = (pos[0]+amount, pos[1])
    elif dir == 'D':
        pos = (pos[0], pos[1]-amount)
    elif dir == 'L':
        pos = (pos[0]-amount, pos[1])
    elif dir == 'U':
        pos = (pos[0], pos[1]+amount)

    positions.append(pos)

area = 0
for i in range(len(positions)-1):
    area += positions[i][0]*positions[i+1][1]

area += positions[-1][0]*positions[0][1]

for i in range(len(positions)-1):
    area -= positions[i][1]*positions[i+1][0]

area -= positions[-1][1]*positions[0][0]

area = 0.5 * abs(area)

print(area - 0.5*perimeter + 1 + perimeter)