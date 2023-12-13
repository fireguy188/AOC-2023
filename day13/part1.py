def get_cols(graph):
    cols = []

    for col in range(len(graph[0])):
        new_col = []
        for row in graph:
            new_col.append(row[col])
        cols.append(new_col)

    return cols

with open('input.txt') as inp: 
    total = 0
    inp = [x.split('\n') for x in inp.read().strip().split('\n\n')]
    for graph in inp:
        # Check for rows of reflection
        for row in range(1, len(graph)):
            above, below = graph[:row], graph[row:]
            above = above[::-1]

            for r in range(min(len(above), len(below))):
                if above[r] != below[r]:
                    break
            else:
                total += row * 100
                break
        
        # Check for cols of reflection
        cols = get_cols(graph)
        for col in range(1, len(graph[0])):
            behind, ahead = cols[:col], cols[col:]
            behind = behind[::-1]

            for c in range(min(len(behind), len(ahead))):
                if behind[c] != ahead[c]:
                    break
            else:
                total += col
                break
    
    print(total)