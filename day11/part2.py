graph = []
with open('input.txt') as inp: 
    for row in inp:
        graph.append(list(row.strip()))

expansion = 1000000
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

galaxy_locations = []
for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] == '#':
            galaxy_locations.append((row, col))

total = 0
for g1 in range(len(galaxy_locations)):
    for g2 in range(g1+1, len(galaxy_locations)):
        gal1, gal2 = galaxy_locations[g1], galaxy_locations[g2]

        # find how many cols and rows between them have expanded
        offset = 0
        for row in range(gal1[0]+1, gal2[0]):
            if row in rows_to_expand:
                offset += expansion-1
        
        # Galaxy 1 may have bigger column than Galaxy 2
        for col in range(gal1[1]+1, gal2[1]):
            if col in cols_to_expand:
                offset += expansion-1
        for col in range(gal2[1]+1, gal1[1]):
            if col in cols_to_expand:
                offset += expansion-1

        total += abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]) + offset

print(total)