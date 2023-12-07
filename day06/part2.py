with open('input.txt') as inp: 
    time, distance = inp.read().strip().split('\n')
    time = int(time.split(':')[1].replace(' ', ''))
    distance = int(distance.split(':')[1].replace(' ', ''))

ways = 0
for hold_time in range(0, time+1):
    if hold_time % 1000000 == 0:
        print(f'{hold_time} / {time}')
    speed = hold_time
    travelled = speed * (time - hold_time)
    if travelled > distance:
        ways += 1

print(ways)

