with open('input.txt') as inp: 
    times, distances = inp.read().strip().split('\n')
    times = [int(x) for x in times.split(':')[1].split()]
    distances = [int(x) for x in distances.split(':')[1].split()]

total = 1
for race in range(len(times)):
    ways = 0
    for hold_time in range(0, times[race]+1):
        speed = hold_time
        travelled = speed * (times[race] - hold_time)
        if travelled > distances[race]:
            ways += 1

    total *= ways

print(total)