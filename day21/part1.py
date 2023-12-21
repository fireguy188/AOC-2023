graph = []
with open('input.txt') as inp: 
    for line in inp:
        graph.append(line.strip())

for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] == 'S':
            start = (row, col)

queue = [(start, 0)]
visited = {(start, 0)}
required_steps = 64
total = 0
for pos, steps in queue:
    if steps == required_steps:
        total += 1
    if steps > required_steps:
        continue

    if not ((pos[0]+1, pos[1]), steps+1) in visited and pos[0]+1 < len(graph) and graph[pos[0]+1][pos[1]] != '#':
        visited.add(((pos[0]+1, pos[1]), steps+1))
        queue.append(((pos[0]+1, pos[1]), steps+1))

    if not ((pos[0], pos[1]+1), steps+1) in visited and pos[1]+1 < len(graph[0]) and graph[pos[0]][pos[1]+1] != '#':
        visited.add(((pos[0], pos[1]+1), steps+1))
        queue.append(((pos[0], pos[1]+1), steps+1))

    if not ((pos[0]-1, pos[1]), steps+1) in visited and pos[0]-1 >= 0 and graph[pos[0]-1][pos[1]] != '#':
        visited.add(((pos[0]-1, pos[1]), steps+1))
        queue.append(((pos[0]-1, pos[1]), steps+1))

    if not ((pos[0], pos[1]-1), steps+1) in visited and pos[1]-1 >= 0 and graph[pos[0]][pos[1]-1] != '#':
        visited.add(((pos[0], pos[1]-1), steps+1))
        queue.append(((pos[0], pos[1]-1), steps+1))

print(total)