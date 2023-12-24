graph = []
with open('input.txt') as inp: 
    for line in inp:
        graph.append(line.strip())

for col in range(len(graph[0])):
    if graph[0][col] == '.':
        start = (0, col)

    if graph[-1][col] == '.':
        end = (len(graph)-1, col)

def adjacent(pos):
    return [new_pos for new_pos in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
            if 0 <= new_pos[0] < len(graph) and 0 <= new_pos[1] < len(graph[0])]

stack = [(start, 0, {start})]
best = -1
while stack:
    pos, steps, visited = stack.pop()

    if pos == end:
        best = max(steps, best)
        continue

    new_positions = []
    if graph[pos[0]][pos[1]] == '>':
        if pos[1]+1 < len(graph[0]):
            new_positions = [(pos[0], pos[1]+1)]
    elif graph[pos[0]][pos[1]] == '<':
        if pos[1]-1 >= 0:
            new_positions = [(pos[0], pos[1]-1)]
    elif graph[pos[0]][pos[1]] == 'v':
        if pos[0]+1 < len(graph):
            new_positions = [(pos[0]+1, pos[1])]
    elif graph[pos[0]][pos[1]] == '^':
        if pos[0]-1 >= 0:
            new_positions = [(pos[0]-1, pos[1])]
    else:
        new_positions = adjacent(pos)
    
    for new_pos in new_positions:
        if not new_pos in visited and graph[new_pos[0]][new_pos[1]] != '#':
            stack.append((new_pos, steps+1, visited.copy() | {new_pos}))

print(best)