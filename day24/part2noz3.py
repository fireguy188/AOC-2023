hails = []
with open('input.txt') as inp: 
    for line in inp:
        pos, vel = line.strip().split('@')
        pos = [int(x) for x in pos.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        hails.append((pos, vel))

def solve(M, rhs):
    # Takes in a square matrix and the right hand side of the equations
    # and returns an array of the solutions

    # Gaussian elimination
    for col in range(len(M)):
        for row in range(col+1, len(M)):
            factor = M[col][col] / M[row][col]
            for i in range(col, len(M)):
                M[row][i] -= M[col][i] * factor
            rhs[row] -= factor * rhs[col]
    
    # Jordan reduction
    for col in range(len(M)-1, -1, -1):
        rhs[col] /= M[col][col]
        M[col][col] = 1
        for row in range(col-1, -1, -1):
            factor = M[row][col] / M[col][col]
            M[row][col] -= M[col][col] * factor
            rhs[row] -= factor * rhs[col]
    
    return rhs

ans = solve([[1, 2],
            [1, 1]], [1, 1])

# We only need the first 3 rocks to get 9 equations
# with 9 unknowns
# The equations are in this form (each line is really 3 equations):
# (x y z) + t1(a b c) = hail1_pos + t1*hail1_vel
# (x y z) + t2(a b c) = hail2_pos + t2*hail2_vel
# (x y z) + t3(a b c) = hail3_pos + t3*hail3_vel
# So our unknowns are x, y, z, a, b, c, t1, t2 and t3
M = [[0 for _ in range(9)] for _ in range(9)]
for i in range(3):
    hail = hails[i]
    [1, 0, 0, ]