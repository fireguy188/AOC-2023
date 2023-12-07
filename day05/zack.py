with open('test.txt', "r") as f:
    data = f.read()

info = [
    [newitem for newitem in item.split() if newitem.isdigit()]
    for item in data.split("\n\n")
]
print(info)


seeds = [int(i) for i in info[0]]
better_seeds = []
for i in range(0, len(seeds), 2):
    better_seeds.append((seeds[i], seeds[i + 1]))


def find_range(seed, convertRanges):
    for i in range(0, len(convertRanges), 3):
        if seed in range(
            convertRanges[i + 1], convertRanges[i + 1] + convertRanges[i + 2]
        ):
            return i
    return None


def create_range(seed, range, convertRanges):
    if range == None:
        return seed
    else:
        return seed + convertRanges[range] - convertRanges[range + 1]


def findnext(rangestarts, start):
    for r in rangestarts:
        if r > start:
            return r
    return 999999999999999999999999999999999999


def convert(seeds, converter):
    convertRanges = [int(i) for i in converter]
    rangestarts = sorted(convertRanges[i] for i in range(1, len(convertRanges), 3))
    newseeds = []
    for start, size in seeds:
        while size > 0:
            rangeIndex = find_range(start, convertRanges)
            if rangeIndex is None:
                endrange = findnext(rangestarts, start)
            else:
                endrange = convertRanges[rangeIndex + 1] + convertRanges[rangeIndex + 2]
            step = min(endrange - start, size)
            newseeds.append((create_range(start, rangeIndex, convertRanges), step))
            size -= step
            start += step
    return newseeds


for converter in info[1:]:
    better_seeds = convert(better_seeds, converter)

print(min(better_seeds)[0])