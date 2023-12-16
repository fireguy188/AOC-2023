import sys
sys.setrecursionlimit(99999999)

graph = []
with open('input.txt') as inp: 
    for line in inp:
        graph.append(line.strip())

def cycle_light(pos, dir, graph, seen_beams, energised):
    # Energise this position and continue its path
    if (pos, dir) in seen_beams:
        return
    energised.add(pos)
    seen_beams.add((pos, dir))
    
    if dir == 'R':
        new_pos = (pos[0], pos[1]+1)
    elif dir == 'L':
        new_pos = (pos[0], pos[1]-1)
    elif dir == 'U':
        new_pos = (pos[0]-1, pos[1])
    elif dir == 'D':
        new_pos = (pos[0]+1, pos[1])

    if not(0 <= new_pos[0] < len(graph) and 0 <= new_pos[1] < len(graph[0])):
        return

    for new_beam in get_new_beams(new_pos, dir, graph):
        cycle_light(new_beam[0], new_beam[1], graph, seen_beams, energised)

def get_new_beams(new_pos, dir, graph):
    if graph[new_pos[0]][new_pos[1]] == '.':
        return [(new_pos, dir)]
    
    if graph[new_pos[0]][new_pos[1]] == '/':
        if dir == 'R':
            return [(new_pos, 'U')]
        if dir == 'L':
            return [(new_pos, 'D')]
        if dir == 'U':
            return [(new_pos, 'R')]
        if dir == 'D':
            return [(new_pos, 'L')]
    
    if graph[new_pos[0]][new_pos[1]] == '\\':
        if dir == 'R':
            return [(new_pos, 'D')]
        if dir == 'L':
            return [(new_pos, 'U')]
        if dir == 'U':
            return [(new_pos, 'L')]
        if dir == 'D':
            return [(new_pos, 'R')]
    
    if graph[new_pos[0]][new_pos[1]] == '|':
        if dir == 'R':
            return [(new_pos, 'U'), (new_pos, 'D')]
        if dir == 'L':
            return [(new_pos, 'U'), (new_pos, 'D')]
        if dir == 'U':
            return [(new_pos, 'U')]
        if dir == 'D':
            return [(new_pos, 'D')]
    
    if graph[new_pos[0]][new_pos[1]] == '-':
        if dir == 'R':
            return [(new_pos, 'R')]
        if dir == 'L':
            return [(new_pos, 'L')]
        if dir == 'U':
            return [(new_pos, 'R'), (new_pos, 'L')]
        if dir == 'D':
            return [(new_pos, 'R'), (new_pos, 'L')]

def get_energised(start_pos, start_dir, graph):
    seen_beams = set()
    energised = set()
    cycle_light((start_pos[0], start_pos[1]), start_dir, graph, seen_beams, energised)

    return len(energised)-1

best = 0
# handle all rows (apart from corners)
for start_row in range(1, len(graph)-1):
    print(f'{start_row} / {len(graph)-2}')
    best = max(best, get_energised((start_row, -1), 'R', graph))
    best = max(best, get_energised((start_row, len(graph[0])), 'L', graph))

# handle all columns (apart from corners)
for start_col in range(1, len(graph[0])-1):
    print(f'{start_col} / {len(graph[0])-2}')
    best = max(best, get_energised((-1, start_col), 'D', graph))
    best = max(best, get_energised((len(graph), start_col), 'U', graph))

# handle corners
best = max(best, get_energised((0, -1), 'R', graph))
best = max(best, get_energised((-1, 0), 'D', graph))

best = max(best, get_energised((len(graph)-1, -1), 'R', graph))
best = max(best, get_energised((len(graph), 0), 'U', graph))

best = max(best, get_energised((0, len(graph[0])), 'L', graph))
best = max(best, get_energised((-1, len(graph[0])-1), 'D', graph))

best = max(best, get_energised((len(graph)-1, len(graph[0])), 'L', graph))
best = max(best, get_energised((len(graph), len(graph[0])-1), 'U', graph))

print(best)