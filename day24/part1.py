hails = []
with open('input.txt') as inp: 
    for line in inp:
        pos, vel = line.strip().split('@')
        pos = [int(x) for x in pos.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        hails.append((pos, vel))

def range_overlap(r1, r2):
    return (max(r1[0], r2[0]), min(r1[1], r2[1]))

MINIMUM = 200000000000000
MAXIMUM = 400000000000000

hails = [(pos[:-1], vel[:-1]) for pos, vel in hails]

total = 0
for h1 in range(len(hails)):
    for h2 in range(h1+1, len(hails)):
        hail1, hail2 = hails[h1], hails[h2]
        M = [[-hail2[1][0], hail1[1][0]],
            [-hail2[1][1], hail1[1][1]]]
        # Invert the matrix
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        row1 = (hail2[0][0] - hail1[0][0])
        row2 = (hail2[0][1] - hail1[0][1])
        if det != 0:
            invertedM = [[M[1][1]/det, -M[0][1]/det],
                        [-M[1][0]/det, M[0][0]/det]]
            mu = invertedM[0][0] * row1 + invertedM[0][1] * row2
            lamda = invertedM[1][0] * row1 + invertedM[1][1] * row2
            
            if mu >= 0 and lamda >= 0:
                x, y = hail1[0][0] + lamda * hail1[1][0], hail1[0][1] + lamda * hail1[1][1]
                if MINIMUM <= x <= MAXIMUM and MINIMUM <= y <= MAXIMUM:
                    total += 1
        else:
            # There may be infinite solutions or no solutions
            # First, check for the no solution case
            if row1 / row2 != M[0][0] / M[1][0]:
                continue

            # Now we know there are infinite solutions
            # Find the range of values mu can take to fit in the box (x)
            # MINIMUM <= hail2[0][0] + mu*hail2[1][0] <= MAXIMUM
            # MINIMUM - hail2[0][0] <= mu*hail2[1][0] <= MAXIMUM - hail2[0][0]
            if hail2[1][0] < 0:
                # (MINIMUM - hail2[0][0])/hail2[1][0] >= mu >= (MAXIMUM - hail2[0][0])/hail2[1][0]
                xrange = ((MAXIMUM - hail2[0][0]) / hail2[1][0], (MINIMUM - hail2[0][0]) / hail2[1][0])
            elif hail2[1][0] > 0:
                # (MINIMUM - hail2[0][0])/hail2[1][0] <= mu <= (MAXIMUM - hail2[0][0])/hail2[1][0]
                xrange = ((MINIMUM - hail2[0][0]) / hail2[1][0], (MAXIMUM - hail2[0][0]) / hail2[1][0])
            else:
                # (MINIMUM - hail2[0][0])/hail2[1][0] <= 0 <= (MAXIMUM - hail2[0][0])/hail2[1][0]
                if (MINIMUM - hail2[0][0]) / hail2[1][0] <= 0 <= (MAXIMUM - hail2[0][0]) / hail2[1][0]:
                    xrange = (0, float('inf'))
                else:
                    continue
            
            # Now check if the xrange is valid (mu can't be < 0)
            if xrange[1] < 0:
                continue
            xrange = (max(xrange[0], 0), xrange[1])

            # Find the range of values mu can take to fit in the box (y)
            # MINIMUM <= hail2[0][1] + mu*hail2[1][1] <= MAXIMUM
            # MINIMUM - hail2[0][1] <= mu*hail2[1][1] <= MAXIMUM - hail2[0][1]
            if hail2[1][1] < 0:
                # (MINIMUM - hail2[0][1])/hail2[1][1] >= mu >= (MAXIMUM - hail2[0][1])/hail2[1][1]
                yrange = ((MAXIMUM - hail2[0][1]) / hail2[1][1], (MINIMUM - hail2[0][1]) / hail2[1][1])
            elif hail2[1][1] > 0:
                # (MINIMUM - hail2[0][1])/hail2[1][1] <= mu <= (MAXIMUM - hail2[0][1])/hail2[1][1]
                yrange = ((MINIMUM - hail2[0][1]) / hail2[1][1], (MAXIMUM - hail2[0][1]) / hail2[1][1])
            else:
                # (MINIMUM - hail2[0][1])/hail2[1][1] <= 0 <= (MAXIMUM - hail2[0][1])/hail2[1][1]
                if (MINIMUM - hail2[0][1]) / hail2[1][1] <= 0 <= (MAXIMUM - hail2[0][1]) / hail2[1][1]:
                    yrange = (0, float('inf'))
                else:
                    continue
            
            # Now check if the yrange is valid (mu can't be < 0)
            if yrange[1] < 0:
                continue
            yrange = (max(yrange[0], 0), yrange[1])

            # Now find the true range that mu can take
            mu_range = range_overlap(xrange, yrange)
            if mu_range[1] < mu_range[0]:
                # invalid range
                continue

            # There is a value for mu that works
            # Find the range of values for lamda
            # -hail2[1][0]mu + hail1[1][0]lamda = row1
            # hail1[1][0]lamda = row1 + hail2[1][0]mu
            # lamda = (row1 + hail2[1][0]mu) / hail1[1][0]
            lamda_range = ((row1 + hail2[1][0]*mu_range[0]) / hail1[1][0], (row1 + hail2[1][0]*mu_range[1]) / hail1[1][0])
            if lamda_range[0] > lamda_range[1]:
                lamda_range = (lamda_range[1], lamda_range[0])
            
            lamda_range = (max(lamda_range[0], 0), lamda_range[1])
            if lamda_range[1] < lamda_range[0]:
                # invalid range
                continue

            # We have found a valid lamda and a valid mu that get us in the box
            total += 1
            

print(total)