import math

with open('input.txt') as inp: 
    time, distance = inp.read().strip().split('\n')
    time = int(time.split(':')[1].replace(' ', ''))
    distance = int(distance.split(':')[1].replace(' ', ''))

# Distance travelled = (total time of race - time holding button) * time holding button
lower_root, upper_root = (time - (time**2 - 4*distance)**0.5) / 2, (time + (time**2 - 4*distance)**0.5) / 2
if int(lower_root) != lower_root:
    lower_root = math.ceil(lower_root)
else:
    lower_root += 1

if int(upper_root) != upper_root:
    upper_root = math.floor(upper_root)
else:
    upper_root -= 1

print(int(upper_root - lower_root + 1))
