graph = []
with open('input.txt') as inp: 
    for line in inp:
        graph.append([int(x) for x in line.strip()])

def move(pos, dir):
    if dir == 'R':
        return (pos[0], pos[1]+1)
    if dir == 'L':
        return (pos[0], pos[1]-1)
    if dir == 'U':
        return (pos[0]-1, pos[1])
    if dir == 'D':
        return (pos[0]+1, pos[1])

def get_left_and_right(dir):
    if dir == 'R':
        return ('U', 'D')
    if dir == 'L':
        return ('D', 'U')
    if dir == 'U':
        return ('L', 'R')
    if dir == 'D':
        return ('R', 'L')

def dijkstra(start, end, graph):
    # each item in queue is:
    # - (row, col)
    # - direction
    # - amount moved in direction
    # - weight
    queue = [(start, 'R', 0, 0), (start, 'D', 0, 0)]
    seen = {(start, 'R', 0):0, (start, 'D', 0):0}
    while True:
        best = -1
        for i in range(len(queue)):
            if best == -1 or queue[i][3] < queue[best][3]:
                best = i
        pos, dir, amount, weight = queue.pop(best)

        if pos == end:
            return weight

        new_states = []
        # See if we can keep moving in current direction
        if amount < 10:
            new_pos = move(pos, dir)
            if 0 <= new_pos[0] < len(graph) and 0 <= new_pos[1] < len(graph[0]):
                new_states.append((new_pos, dir, amount+1, weight+graph[new_pos[0]][new_pos[1]]))
        
        if amount >= 4:
            # Turn left or right
            for new_dir in get_left_and_right(dir):
                new_pos = move(pos, new_dir)
                if 0 <= new_pos[0] < len(graph) and 0 <= new_pos[1] < len(graph[0]):
                    new_states.append((new_pos, new_dir, 1, weight+graph[new_pos[0]][new_pos[1]]))
        
        for new_state in new_states:
            if new_state[-1] < seen.get(new_state[:-1], float('inf')):
                queue.append(new_state)
                seen[new_state[:-1]] = new_state[-1]

print(dijkstra((0, 0), (len(graph)-1, len(graph[0])-1), graph))