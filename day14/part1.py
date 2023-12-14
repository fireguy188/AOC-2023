locations = {}
with open('input.txt') as inp: 
    inp = inp.read().strip().split('\n')

for row in range(len(inp)):
    for col in range(len(inp[0])):
        locations[(row, col)] = inp[row][col]

# Tilt upwards
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
            
total = 0
for row in range(len(inp)):
    for col in range(len(inp[0])):
        if new_locations[(row, col)] == 'O':
            total += len(inp)-row

print(total)