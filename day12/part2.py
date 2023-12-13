from functools import cache

def get_cool_ans(springs, groups):
    @cache
    def worker(springs, groups, group_index, group_length):
        if springs == '':
            if group_index == len(groups)-1 and groups[group_index] == group_length:
                return 1
            if group_index == len(groups) and group_length == 0:
                return 1
            return 0
        
        if springs[0] == '?':
            if group_length > 0:
                if group_length == groups[group_index]:
                    add1 = worker(springs[1:], groups, group_index+1, 0)
                else:
                    add1 = 0
            else:
                add1 = worker(springs[1:], groups, group_index, 0)

            if group_index == len(groups) or group_length+1 > groups[group_index]:
                add2 = 0
            else:
                add2 = worker(springs[1:], groups, group_index, group_length+1)

            return add1 + add2
    
        if springs[0] == '.':
            if group_length > 0:
                if group_length == groups[group_index]:
                    return worker(springs[1:], groups, group_index+1, 0)
                else:
                    return 0
            else:
                return worker(springs[1:], groups, group_index, 0)
        
        if springs[0] == '#':
            if group_index == len(groups) or group_length+1 > groups[group_index]:
                return 0
            else:
                return worker(springs[1:], groups, group_index, group_length+1)

    return worker(springs, groups, 0, 0)

#print(get_cool_ans(['?', '?'], [1]))
with open('input.txt') as inp:
    total = 0
    for i, line in enumerate(inp):
        #print(f'{i} / 1000')
        fake_springs, fake_groups = line.strip().split()
        groups = []
        springs = []
        for _ in range(5):
            groups += [int(x) for x in fake_groups.split(',')]
            springs.append(fake_springs)
        springs = '?'.join(springs)
        groups = tuple(groups)

        #original_s
            
        total += get_cool_ans(springs, groups)

        
print(total)

# .??..??...?##. # .??..??...?##.