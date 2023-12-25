graph = []
with open('test.txt') as inp: 
    for line in inp:
        graph.append(line.strip())

for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] == 'S':
            start = (row, col)

def get_value(pos):
    return graph[pos[0]%len(graph)][pos[1]%len(graph[0])]

def ans(required_steps):
    queue = [(start, 0)]
    visited = {(start, 0)}
    total = 0
    for pos, steps in queue:
        if steps == required_steps:
            total += 1
        if steps > required_steps:
            continue

        if not ((pos[0]+1, pos[1]), steps+1) in visited and get_value((pos[0]+1, pos[1])) != '#':
            visited.add(((pos[0]+1, pos[1]), steps+1))
            queue.append(((pos[0]+1, pos[1]), steps+1))

        if not ((pos[0], pos[1]+1), steps+1) in visited and get_value((pos[0], pos[1]+1)) != '#':
            visited.add(((pos[0], pos[1]+1), steps+1))
            queue.append(((pos[0], pos[1]+1), steps+1))

        if not ((pos[0]-1, pos[1]), steps+1) in visited and get_value((pos[0]-1, pos[1])) != '#':
            visited.add(((pos[0]-1, pos[1]), steps+1))
            queue.append(((pos[0]-1, pos[1]), steps+1))

        if not ((pos[0], pos[1]-1), steps+1) in visited and get_value((pos[0], pos[1]-1)) != '#':
            visited.add(((pos[0], pos[1]-1), steps+1))
            queue.append(((pos[0], pos[1]-1), steps+1))
    
    return total

def better_ans(required_steps):
    queue = [(start, 0)]
    visited = {start}
    total = 0
    for pos, steps in queue:
        if steps%2 == required_steps%2:
            total += 1
        if steps > required_steps:
            continue

        if not (pos[0]+1, pos[1]) in visited and get_value((pos[0]+1, pos[1])) != '#':
            visited.add((pos[0]+1, pos[1]))
            queue.append(((pos[0]+1, pos[1]), steps+1))

        if not (pos[0], pos[1]+1) in visited and get_value((pos[0], pos[1]+1)) != '#':
            visited.add((pos[0], pos[1]+1))
            queue.append(((pos[0], pos[1]+1), steps+1))

        if not (pos[0]-1, pos[1]) in visited and get_value((pos[0]-1, pos[1])) != '#':
            visited.add((pos[0]-1, pos[1]))
            queue.append(((pos[0]-1, pos[1]), steps+1))

        if not (pos[0], pos[1]-1) in visited and get_value((pos[0], pos[1]-1)) != '#':
            visited.add((pos[0], pos[1]-1))
            queue.append(((pos[0], pos[1]-1), steps+1))
    
    return total

# test = [better_ans(x) for x in range(0, 500+1, 5)]
# test = [ans(x) for x in range(0, 110+1, 11)]
# differences = [test[i+1]-test[i] for i in range(len(test)-1)]
# second_differences = [differences[i+1]-differences[i] for i in range(len(differences)-1)]
# print(test)
# print(differences)
# print(second_differences)

def really_cool_ans(required_steps):
    steps = 0
    answers = []
    differences = []
    second_differences = []
    adding = len(graph)
    while True:
        answers.append(better_ans(steps))
        if len(answers) >= 2:
            differences.append(answers[-1]-answers[-2])
        if len(differences) >= 2:
            second_differences.append(differences[-1]-differences[-2])
        if len(second_differences) > 1 and second_differences[-1] == second_differences[-2]:
            break

        steps += adding
    steps -= adding

    # THE SECOND DIFFERENCE FUCKING SETTLES
    # Let's find the quadratic equation for generating elements
    a = 0.5 * second_differences[-1]
    # ans(51), ans(62), ... ans(700)
    # b and c are a bit different, we don't just want the multiples of len(graph)
    # we want to be able to get answers for 1+multiple of len(graph) or 2+ etc.

    answer = better_ans(steps+required_steps%len(graph))
    difference = better_ans(steps+required_steps%len(graph)+len(graph)) - answer
    b = difference - 3*a
    c = answer - a - b
    # so n = 1 gives the answer when required_steps = steps+required_steps%len(graph)
    # so putting n = (required_steps - steps) // len(graph) + 1
    # gives the answer
    n = (required_steps - steps) // adding + 1
    return int(a*n**2 + b*n + c)

    # for x in range(5):
    #     test = []
    #     for step in range(steps+adding*x, steps+adding*(x+1)):
    #         test.append(better_ans(step))
    #     print(test)

print(really_cool_ans(26501365))
#print(better_ans(66))
# Each difference is of form 4n - something?

# Create a dictionary of all garden plots where values are the (row, col)
# adjacent that are garden plots
# next_steps = {}
# for row in range(len(graph)):
#     for col in range(len(graph[0])):
#         if get_value((row, col)) != '#':
#             next_steps[(row, col)] = []
#             for row_off, col_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 if get_value((row+row_off, col+col_off)) != '#':
#                     next_steps[(row, col)].append(((row+row_off)%len(graph), (col+col_off)%len(graph[0])))

# anything reachable in 2n steps is reachable in 2n + 2x number of steps (x > 0)
# anything reachable in 2n + 1 steps is reachable in 2n + 1 + 2x number of steps (x > 0)
# f(0) = 1
# f(1) = 1, 2, 3 or 4 (based on input)
# f(10) = f(8) + new_stuff
# So how do we find new_stuff?
# 
                    
# Imagine an empty grid:
# 0, 1, 2, 3 steps:
# ........... ........... ........... ...........
# ........... ........... ........... ...........
# ........... ........... ........... .....O.....
# ........... ........... .....O..... ....O.O....
# ........... .....O..... ....O.O.... ...O.O.O...
# .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# ........... .....O..... ....O.O.... ...O.O.O...
# ........... ........... .....O..... ....O.O....
# ........... ........... ........... .....O.....
# ........... ........... ........... ...........
# ........... ........... ........... ...........
# 1, 4, 9, 16

# ........... ........... ........... ........... ...........
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ........... .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# .....O#.... ....O.#.... ...O.O#.... ..O.O.#.... .O.O.O#O...
# ........... .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... ........... ...........

# ........... ........... ........... ........... ...........
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ........... .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# .....O##... ....O.##... ...O.O##... ..O.O.##... .O.O.O##...
# ........... .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... ........... ...........

# What do the #'s actually do?
# Theory: stops any exploration on their gradient (theory WRONG)
# ........... ........... ........... ........... ...........
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ......#.... .....O#.... ....O.#.... ...O.O#.... ..O.O.#....
# .....O#.... ....O.#.... ...O.O#.... ..O.O.#.... .O.O.O#O...
# ........... .....O..... ....O.O.... ...O.O.O... ..O.O.O.O..
# ........... ........... .....O..... ....O.O.... ...O.O.O...
# ........... ........... ........... .....O..... ....O.O....
# ........... ........... ........... ........... .....O.....
# ........... ........... ........... ........... ...........

# ........... ........... ........... ...........
# ........... ........... ........... ...........
# ........... ........... ........... ...........
# ....#...... ....#...... ....#...... ....#......
# .....#..... .....#..... ....O#..... ...O.#.....
# .....O#.... ....O.#.... ...O.O#.... ..O.O.#....
# .......#... .....O.#... ....O.O#... ...O.O.#...
# ........... ........... .....O..... ....O.O....
# ........... ........... ........... .....O.....
# ........... ........... ........... ...........
# ........... ........... ........... ...........

# Theory: multiple #'s part of 1 gradient have only 1 effect on outer diamond
# (n+1)^2 - #'s part of a diamond - gradients encountered (WRONG)
#
# if n is even, then #'s part of diamond is just #'s with even distance
# otherwise #'s with odd distance
blocks = set()
for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] == '#':
            blocks.add((row, col))

# def find_blocks(distance, blocks):
#     found = 0
#     for (row, col) in blocks:
#         v_dist1, h_dist1 = abs(row-len(graph)//2), abs(col-len(graph[0])//2)
#         v_dist2, h_dist2 = len(graph) - v_dist1, len(graph) - h_dist1
#         # Graph is square
#         distances = set([x%len(graph) for x in [h_dist1 + v_dist1, h_dist1 + v_dist2, h_dist2 + v_dist1, h_dist2 + v_dist2]])
#         for dist in distances:
#             if distance%len(graph) == dist


# required_steps = 50
# for step in range(1, required_steps+1):


# For every # , its distance away from centre is the outer diamond it starts affecting
# go from 1 to 26501365 in steps of 2 and add how many on outer diamond
# how many on outer diamond?
# it is 4n - number of #s this distance away (WRONG)
    


# maximum of 14 steps to reach any point on grid (test.txt)
# (n+1)^2 - (n-1)^2 gets just outer diamond (n >= 1 is number of steps)
# (n+1-n+1)(n+1+n-1) = 4n
#
# go from 1 to 26501365 in steps of 2 and add how many on outer diamond
#
# .OOO. OO.OO
# O...O O.O.O
# O...O .O.O.
# O...O O.O.O
# .OOO. OO.OO
#
# ... .O. OOO OOO
# .O. O.O O.O OOO
# ... .O. OOO OOO
            
# 26501365 = 5 * 11 * 481843
            # 26501365 = 65 + 200200 * 131