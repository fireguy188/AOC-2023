def get_cols(graph):
    cols = []

    for col in range(len(graph[0])):
        new_col = []
        for row in graph:
            new_col.append(row[col])
        cols.append(new_col)

    return cols

def get_ans(graph):
    answers = []
    
    # Check for rows of reflection
    for row in range(1, len(graph)):
        above, below = graph[:row], graph[row:]
        above = above[::-1]

        for r in range(min(len(above), len(below))):
            if above[r] != below[r]:
                break
        else:
            answers.append(('row', row))
    
    # Check for cols of reflection
    cols = get_cols(graph)
    for col in range(1, len(graph[0])):
        behind, ahead = cols[:col], cols[col:]
        behind = behind[::-1]

        for c in range(min(len(behind), len(ahead))):
            if behind[c] != ahead[c]:
                break
        else:
            answers.append(('col', col))
    
    return answers

def get_new_score(graph, real_ans):
    for r_smudge in range(len(graph)):
        for c_smudge in range(len(graph[0])):
            new_graph = [list(row) for row in graph]

            if new_graph[r_smudge][c_smudge] == '.':
                new_graph[r_smudge][c_smudge] = '#'
            else:
                new_graph[r_smudge][c_smudge] = '.'

            for new_ans in get_ans(new_graph):
                if new_ans != real_ans:
                    if new_ans[0] == 'row':
                        return new_ans[1] * 100
                    return new_ans[1]

with open('input.txt') as inp: 
    total = 0
    inp = [x.split('\n') for x in inp.read().strip().split('\n\n')]
    
    for graph in inp:
        total += get_new_score(graph, get_ans(graph)[0])
    
    print(total)
