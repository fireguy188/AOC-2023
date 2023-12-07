total = 0


def works(sets):
    for s in sets:
        amount = {"red": 12, "green": 13, "blue": 14}
        for color in s:
            if amount[color] < s[color]:
                return False
    return True


with open("input.txt") as inp:
    for line in inp:
        game_num, data = line.split(": ")
        sets = [s.split(", ") for s in data.split("; ")]
        sets = [{x.split()[1]: int(x.split()[0]) for x in s} for s in sets]

        if works(sets):
            total += int(game_num.split()[-1])

print(total)
