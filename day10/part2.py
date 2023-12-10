import math

graph = []
with open('input.txt') as inp: 
    for row in inp:
        graph.append(list(row.strip()))

def get_start(graph):
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 'S':
                return (row, col)

def get_adjacent(graph, row, col):
    adjacent = {'N':((row-1, col), '.'), 'E':((row, col+1), '.'), 'S':((row+1, col), '.'), 'W':((row, col-1), '.')}

    if row-1 >= 0:
        adjacent['N'] = ((row-1, col), graph[row-1][col])
    if col+1 < len(graph[0]):
        adjacent['E'] = ((row, col+1), graph[row][col+1])
    if row+1 < len(graph):
        adjacent['S'] = ((row+1, col), graph[row+1][col])
    if col-1 >= 0:
        adjacent['W'] = ((row, col-1), graph[row][col-1])
    
    return adjacent

queue = [get_start(graph)]
visited = {queue[0]:0}
for cur in queue:
    adjacent = get_adjacent(graph, cur[0], cur[1])
    if adjacent['N'][1] in '|7F' and graph[cur[0]][cur[1]] in '|JLS':
        if not adjacent['N'][0] in visited:
            queue.append(adjacent['N'][0])
            visited[adjacent['N'][0]] = visited[cur] + 1
    if adjacent['E'][1] in '-J7' and graph[cur[0]][cur[1]] in '-FLS':
        if not adjacent['E'][0] in visited:
            queue.append(adjacent['E'][0])
            visited[adjacent['E'][0]] = visited[cur] + 1
    if adjacent['S'][1] in '|LJ' and graph[cur[0]][cur[1]] in '|F7S':
        if not adjacent['S'][0] in visited:
            queue.append(adjacent['S'][0])
            visited[adjacent['S'][0]] = visited[cur] + 1
    if adjacent['W'][1] in '-LF' and graph[cur[0]][cur[1]] in '-J7S':
        if not adjacent['W'][0] in visited:
            queue.append(adjacent['W'][0])
            visited[adjacent['W'][0]] = visited[cur] + 1

pipes = set([pos for pos in visited])

def isint(num):
    return int(num) == num

# Go through each tile and see if it can reach an outer edge
# TRYING WITH 0.5 MOVEMENTS
inside = 0
for row in range(len(graph)):
    for col in range(len(graph[0])):
        if (row, col) in pipes:
            continue

        # Find path to edge
        queue = [(row, col)]
        visited = {(row, col)}
        for cur in queue:
            # Check if goal reached
            if cur[0] == 0 or cur[0] == len(graph)-1 or cur[1] == 0 or cur[1] == len(graph[0])-1:
                break

            if not (cur[0]-0.5, cur[1]) in visited:
                # See if we can travel north
                if isint(cur[0]-0.5):
                    if isint(cur[1]):
                        if not (int(cur[0]-0.5), int(cur[1])) in pipes:
                            queue.append((cur[0]-0.5, cur[1]))
                            visited.add((cur[0]-0.5, cur[1]))
                    else:
                        squeeze = graph[int(cur[0]-0.5)][int(cur[1]-0.5)] + graph[int(cur[0]-0.5)][int(cur[1]+0.5)]
                        if not squeeze in [x + y for x in '-FLS' for y in '-J7S']:
                            queue.append((cur[0]-0.5, cur[1]))
                            visited.add((cur[0]-0.5, cur[1]))
                else:
                    queue.append((cur[0]-0.5, cur[1]))
                    visited.add((cur[0]-0.5, cur[1]))
            
            if not (cur[0]+0.5, cur[1]) in visited:
                # See if we can travel south
                if isint(cur[0]+0.5):
                    if isint(cur[1]):
                        if not (int(cur[0]+0.5), int(cur[1])) in pipes:
                            queue.append((cur[0]+0.5, cur[1]))
                            visited.add((cur[0]+0.5, cur[1]))
                    else:
                        squeeze = graph[int(cur[0]+0.5)][int(cur[1]-0.5)] + graph[int(cur[0]+0.5)][int(cur[1]+0.5)]
                        if not squeeze in [x + y for x in '-FLS' for y in '-J7S']:
                            queue.append((cur[0]+0.5, cur[1]))
                            visited.add((cur[0]+0.5, cur[1]))
                else:
                    queue.append((cur[0]+0.5, cur[1]))
                    visited.add((cur[0]+0.5, cur[1]))
            
            if not (cur[0], cur[1]+0.5) in visited:
                # See if we can travel east
                if isint(cur[1]+0.5):
                    if isint(cur[0]):
                        if not (int(cur[0]), int(cur[1]+0.5)) in pipes:
                            queue.append((cur[0], cur[1]+0.5))
                            visited.add((cur[0], cur[1]+0.5))
                    else:
                        squeeze = graph[int(cur[0]-0.5)][int(cur[1]+0.5)] + graph[int(cur[0]+0.5)][int(cur[1]+0.5)]
                        if not squeeze in [x + y for x in '|F7S' for y in '|JLS']:
                            queue.append((cur[0], cur[1]+0.5))
                            visited.add((cur[0], cur[1]+0.5))
                else:
                    queue.append((cur[0], cur[1]+0.5))
                    visited.add((cur[0], cur[1]+0.5))
                
            if not (cur[0], cur[1]-0.5) in visited:
                # See if we can travel west
                if isint(cur[1]-0.5):
                    if isint(cur[0]):
                        if not (int(cur[0]), int(cur[1]-0.5)) in pipes:
                            queue.append((cur[0], cur[1]-0.5))
                            visited.add((cur[0], cur[1]-0.5))
                    else:
                        squeeze = graph[int(cur[0]-0.5)][int(cur[1]-0.5)] + graph[int(cur[0]+0.5)][int(cur[1]-0.5)]
                        if not squeeze in [x + y for x in '|F7S' for y in '|JLS']:
                            queue.append((cur[0], cur[1]-0.5))
                            visited.add((cur[0], cur[1]-0.5))
                else:
                    queue.append((cur[0], cur[1]-0.5))
                    visited.add((cur[0], cur[1]-0.5))
        else:
            inside += 1

print(inside)

