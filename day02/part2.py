total = 0


def get(sets):
    maxes = {"red": 0, "green": 0, "blue": 0}
    for color in ["red", "green", "blue"]:
        for s in sets:
            if s.get(color, 0) > maxes[color]:
                maxes[color] = s.get(color, 0)
    return maxes


with open("input.txt") as inp:
    for line in inp:
        game_num, data = line.split(": ")
        sets = [s.split(", ") for s in data.split("; ")]
        sets = [{x.split()[1]: int(x.split()[0]) for x in s} for s in sets]

        thing = get(sets)
        total += thing["red"] * thing["green"] * thing["blue"]

print(total)
