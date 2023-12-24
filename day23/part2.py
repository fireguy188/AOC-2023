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
    return [new_pos for new_pos in [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1), (pos[0]+1, pos[1])]
            if 0 <= new_pos[0] < len(graph) and 0 <= new_pos[1] < len(graph[0])]

# stack = [(start, 0, {start})]
# best = -1
# while stack:
#     pos, steps, visited = stack.pop()

#     if pos == end:
#         if steps > best:
#             best = steps
#             print(best)
#         continue

#     new_positions = adjacent(pos)
    
#     for new_pos in new_positions:
#         if not new_pos in visited and graph[new_pos[0]][new_pos[1]] != '#':
#             stack.append((new_pos, steps+1, visited.copy() | {new_pos}))

#print(best)

# Get every intersection
# make a map of each intersection to the intersections they connect to
# then run the funny algorithm
intersections = []
for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] != '#':
            if len([pos for pos in adjacent((row, col)) if graph[pos[0]][pos[1]] != '#']) > 2:
                intersections.append((row, col))
    
def get_paths(start, end, intersections):
    # Only returns a path if it is the only possible path
    paths = []
    queue = [(start, {start})]
    for pos, path in queue:
        if pos == end:
            paths.append(path)
            continue

        if pos != start and pos in intersections:
            # We only want direct paths not through any other intersections
            continue

        available_adjacent = [new_pos for new_pos in adjacent(pos) if graph[new_pos[0]][new_pos[1]] != '#' and not new_pos in path]
        
        for new_pos in available_adjacent:
            queue.append((new_pos, path | {new_pos}))

    return paths

intersections = [start] + intersections + [end]
intersection_paths = {pos:{} for pos in intersections}
for s in range(len(intersections)):
    print(f'{s+1} / {len(intersections)}')
    for e in range(s+1, len(intersections)):
        paths = get_paths(intersections[s], intersections[e], set(intersections))
        
        if paths:
            intersection_paths[intersections[s]][intersections[e]] = paths
            intersection_paths[intersections[e]][intersections[s]] = paths

# Lucky strike!!!
# There is only one path between each intersection if there exists a path
for s in intersections:
    for e in intersection_paths[s]:
        assert len(intersection_paths[s][e]) == 1
        intersection_paths[s][e] = intersection_paths[s][e][0]

def evaluate_path(path, intersection_paths):
    total = set()
    for i in range(len(path)-1):
        total = total | intersection_paths[path[i]][path[i+1]]
    return len(total)

stack = [(start, (start,), {start})]
best = -1
while stack:
    pos, path, visited = stack.pop()

    if pos == end:
        score = evaluate_path(path, intersection_paths)
        if score > best:
            best = score
            print(best-1)
        continue

    for new_pos in intersection_paths[pos]:
        if not new_pos in visited:
            #stack.append((new_pos, path | intersection_paths[pos][new_pos], visited.copy() | {new_pos}))
            stack.append((new_pos, path + (new_pos,), visited.copy() | {new_pos}))
# ans > 6102
# ans > 6298