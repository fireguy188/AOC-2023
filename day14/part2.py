locations = {}
with open('input.txt') as inp: 
    inp = inp.read().strip().split('\n')

for row in range(len(inp)):
    for col in range(len(inp[0])):
        locations[(row, col)] = inp[row][col]

def cycle(locations):
    # Tilt north
    new_locations = locations.copy()
    for row in range(len(inp)):
        for col in range(len(inp[0])):
            if new_locations[(row, col)] == 'O':
                # Move it up as far as possible
                new_locations[(row, col)] = '.'
                for new_row in range(row, 0, -1):
                    if new_locations[(new_row-1, col)] != '.':
                        new_locations[(new_row, col)] = 'O'
                        break
                else:
                    new_locations[(0, col)] = 'O'

    # Tilt west
    new_locations = new_locations.copy()
    for col in range(len(inp[0])):
        for row in range(len(inp)):
            if new_locations[(row, col)] == 'O':
                # Move it left as far as possible
                new_locations[(row, col)] = '.'
                for new_col in range(col, 0, -1):
                    if new_locations[(row, new_col-1)] != '.':
                        new_locations[(row, new_col)] = 'O'
                        break
                else:
                    new_locations[(row, 0)] = 'O'
        
    # Tilt south
    new_locations = new_locations.copy()
    for row in range(len(inp)-1, -1, -1):
        for col in range(len(inp[0])):
            if new_locations[(row, col)] == 'O':
                # Move it down as far as possible
                new_locations[(row, col)] = '.'
                for new_row in range(row, len(inp)-1):
                    if new_locations[(new_row+1, col)] != '.':
                        new_locations[(new_row, col)] = 'O'
                        break
                else:
                    new_locations[(len(inp)-1, col)] = 'O'
    
    # Tilt east
    new_locations = new_locations.copy()
    for col in range(len(inp[0])-1, -1, -1):
        for row in range(len(inp)):  
            if new_locations[(row, col)] == 'O':
                # Move it right as far as possible
                new_locations[(row, col)] = '.'
                for new_col in range(col, len(inp[0])-1):
                    if new_locations[(row, new_col+1)] != '.':
                        new_locations[(row, new_col)] = 'O'
                        break
                else:
                    new_locations[(row, len(inp[0])-1)] = 'O'
    
    return new_locations

def get_map(locations):
    ans = []
    for row in range(len(inp)):
        new_row = ''
        for col in range(len(inp[0])): 
            new_row += locations[(row, col)]
        ans.append(new_row)
    return '\n'.join(ans)

# Find the loop
seen = {}
while True:
    c_map = get_map(locations)
    if not c_map in seen:
        seen[c_map] = len(seen)
        locations = cycle(locations)
    else:
        break

seen_indexes = {seen[k]:k for k in seen}
loop = [seen_indexes[m] for m in range(seen[c_map], len(seen))]

cycles = 1000000000
cycles -= seen[c_map]
final_map = loop[cycles%len(loop)].split('\n')

total = 0
for row in range(len(final_map)):
    total += final_map[row].count('O') * (len(final_map) - row)

print(total)