hails = []
with open('input.txt') as inp: 
    for line in inp:
        pos, vel = line.strip().split('@')
        pos = [int(x) for x in pos.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        hails.append((pos, vel))

def simulate(hails, t):
    return [(pos[0]+vel[0]*t, pos[1]+vel[1]*t, pos[2]+vel[2]*t) for pos, vel in hails.copy()]

import z3

s = z3.Solver()

x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')

a = z3.Int('a')
b = z3.Int('b')
c = z3.Int('c')

for i, hail in enumerate(hails):
    t = z3.Int(f't{i}')
    s.add(x + (a - hail[1][0])*t == hail[0][0])
    s.add(y + (b - hail[1][1])*t == hail[0][1])
    s.add(z + (c - hail[1][2])*t == hail[0][2])

s.check()
model = s.model()
print(model[x].as_long() + model[y].as_long() + model[z].as_long())