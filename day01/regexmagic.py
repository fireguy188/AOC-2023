import re

p1total = 0
p2total = 0
with open('input.txt') as inp:
    for line in inp:
        a = re.search('(1|2|3|4|5|6|7|8|9)', line).group(0)
        b = re.search('(1|2|3|4|5|6|7|8|9)', line[::-1]).group(0)
        p1total += int(a+b)

        a = re.search('(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)', line).group(0)
        b = re.search('(1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1]).group(0)
        conv = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        if a in conv:
            a = str(conv.index(a) + 1)
        if b[::-1] in conv:
            b = str(conv.index(b[::-1]) + 1)
        p2total += int(a+b)

print(p1total)
print(p2total)