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
    


seen_beams = set()
energised = set()
cycle_light((0, -1), 'R', graph, seen_beams, energised)
print(len(energised)-1)
