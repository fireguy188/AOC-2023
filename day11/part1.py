graph = []
with open('input.txt') as inp: 
    for row in inp:
        graph.append(list(row.strip()))

# fnd expanded rows and columns
rows_to_expand = []
cols_to_expand = []
for row in range(len(graph)):
    if not '#' in graph[row]:
        rows_to_expand.append(row)

for col in range(len(graph[0])):
    for row in graph:
        if row[col] == '#':
            break
    else:
        cols_to_expand.append(col)

new_graph = []
for row in range(len(graph)):
    if row in rows_to_expand:
        new_graph.append(graph[row].copy())
    new_graph.append(graph[row].copy())

count = 0
for col in range(len(graph[0])):
    if col in cols_to_expand:
        for row in new_graph:
            row.insert(col + count, '.')
        count += 1

galaxy_locations = []
for row in range(len(new_graph)):
    for col in range(len(new_graph[0])):
        if new_graph[row][col] == '#':
            galaxy_locations.append((row, col))

total = 0
for g1 in range(len(galaxy_locations)):
    for g2 in range(g1+1, len(galaxy_locations)):
        gal1, gal2 = galaxy_locations[g1], galaxy_locations[g2]

        total += abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])

print(total)