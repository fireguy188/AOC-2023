digits = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

total = 0
with open('input.txt') as inp:
    for line in inp:
        first = (float('inf'), '')
        for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] + list(digits.keys()):
            if line.find(x) < first[0] and line.find(x) != -1:
                first = (line.find(x), x)
        
        line = line[::-1]
        last = (float('inf'), '')
        for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] + list(digits.keys()):
            if line.find(x[::-1]) < last[0] and line.find(x[::-1]) != -1:
                last = (line.find(x[::-1]), x)

        if first[1] in digits:
            first = str(digits[first[1]])
        else:
            first = first[1]

        if last[1] in digits:
            last = str(digits[last[1]])
        else:
            last = last[1]
        
        total += int(first+last)

print(total)