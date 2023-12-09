def not_all_zero(lst):
    for x in lst:
        if x != 0:
            return True
    
    return False

with open('input.txt') as inp: 
    total = 0
    for history in inp:
        history = [int(x) for x in history.split()]
        differences = [history]
        while not_all_zero(differences[-1]):
            last_d = differences[-1]
            differences.append([last_d[x+1] - last_d[x] for x in range(len(last_d)-1)])
        
        # now go backwards
        differences[-1].append(0)
        for x in range(len(differences)-2, -1, -1):
            differences[x].append(differences[x][-1] + differences[x+1][-1])
        
        total += differences[0][-1]
    print(total)
