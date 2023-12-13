with open('input.txt') as inp:
    total = 0
    for line in inp:
        springs, groups = line.strip().split()
        groups = [int(x) for x in groups.split(',')]
        springs = list(springs)

        questions = set()
        for char in range(len(springs)):
            if springs[char] == '?':
                questions.add(char)
        
        for x in range(2**len(questions)):
            new_springs = springs.copy()
            bin_x = str(bin(x))[2:].zfill(len(questions)).replace('0', '.').replace('1', '#')

            # Check new springs works
            # find contiguous groups of #s
            new_groups = []
            c_group = 0
            digit = 0
            for spring in range(len(new_springs)):
                if spring in questions:
                    new_springs[spring] = bin_x[digit]
                    digit += 1

                # Check contigous groups
                if new_springs[spring] == '#':
                    c_group += 1
                elif c_group > 0 and new_springs[spring] == '.':
                    new_groups.append(c_group)
                    c_group = 0
            if c_group > 0:
                new_groups.append(c_group)
            
            if new_groups == groups:
                total += 1

    print(total)
                

