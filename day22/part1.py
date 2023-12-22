bricks = []
with open('input.txt') as inp: 
    for line in inp:
        pos1, pos2 = line.strip().split('~')
        bricks.append((tuple([int(x) for x in pos1.split(',')]), tuple([int(x) for x in pos2.split(',')])))
bricks.sort(key = lambda brick: brick[0][2])

def range_overlap(r1, r2):
    return (max(r1[0], r2[0]), min(r1[1], r2[1]))

def is_colliding(brick1, brick2):
    # There has to be an overlap in each axis
    for i in range(3):
        r1 = (brick1[0][i], brick1[1][i])
        r2 = (brick2[0][i], brick2[1][i])
        overlap = range_overlap(r1, r2)
        if overlap[1] < overlap[0]:
            # There is no overlap in this axis
            return False
    return True

def fall_bricks(bricks):
    # Make all bricks fall down
    fallen_bricks = []
    for brick in bricks:
        assert brick[0] <= brick[1]
        while brick[0][2] != 1:
            # See if we can make it fall
            for fallen_brick in fallen_bricks:
                if is_colliding(fallen_brick, ((brick[0][0], brick[0][1], brick[0][2]-1), (brick[1][0], brick[1][1], brick[1][2]-1))):
                    # Then it has fallen as much as it can
                    break
            else:
                # Make it fall
                brick = ((brick[0][0], brick[0][1], brick[0][2]-1), (brick[1][0], brick[1][1], brick[1][2]-1))
                continue

            break

        fallen_bricks.append(brick)
    return fallen_bricks

bricks = fall_bricks(bricks)
total = 0
for i in range(len(bricks)):
    print(f'{i} / {len(bricks)}')
    test_bricks = [bricks[j] for j in range(len(bricks)) if j != i]
    if test_bricks == fall_bricks(test_bricks):
        # Then removing this brick didn't matter
        total += 1
print(total)
