with open('input.txt') as inp: 
    inp = inp.read().strip()

directions, connections = inp.split('\n\n')
connections = [x.split(' = ') for x in connections.split('\n')]
connections = {x[0]:x[1][1:-1].split(', ') for x in connections}

starts = [node for node in connections if node[-1] == 'A']

# This code assumes that all --Z nodes are contained in the loop
# e.g no occurences of AAA -> ZZZ -> BBB -> CCC -> AAZ -> BBB -> CCC -> ...
loop_lengths = []
for cur in starts:
    # Find the path until it starts looping
    dir = 0
    seen = {}
    path = []
    while not (cur, dir%len(directions)) in seen:
        path.append(cur)
        seen[(cur, dir%len(directions))] = dir

        if directions[dir%len(directions)] == 'L':
            cur = connections[cur][0]
        else:
            cur = connections[cur][1]
        
        dir += 1
    
    indexes = [i for i in range(len(path)) if path[i][-1] == 'Z']
    loop = path[seen[(cur, dir%len(directions))]:]
    loop_lengths.append((indexes, len(loop)))

# Using the neat face that only 1 --Z node is reached and
# also that it gets reached in a multiple of 'loop_length' steps
# I can just do the lcm of all the loop_lengths
import math
things = [x[1] for x in loop_lengths]
print(math.lcm(*things))
