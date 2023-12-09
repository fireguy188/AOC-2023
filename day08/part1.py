with open('input.txt') as inp: 
    inp = inp.read().strip()

directions, connections = inp.split('\n\n')
connections = [x.split(' = ') for x in connections.split('\n')]
connections = {x[0]:x[1][1:-1].split(', ') for x in connections}

cur = 'AAA'
dir = 0
while cur != 'ZZZ':
    if directions[dir%len(directions)] == 'L':
        cur = connections[cur][0]
    else:
        cur = connections[cur][1]
    
    dir += 1

print(dir)