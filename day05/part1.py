with open('input.txt') as inp: 
    inp = inp.read().strip().split('\n\n')

for m in range(len(inp)):
    if m == 0:
        inp[0] = [int(seed) for seed in inp[0].split(': ')[1].split()]
    else:
        map_name, maps = inp[m].split(':\n')
        source_name, dest_name = map_name.split('-to-')
        the_maps = {'source':source_name, 'dest':dest_name[:-4], 'maps':[]}
        for map_ in maps.split('\n'):
            map_ = [int(x) for x in map_.split()]
            the_maps['maps'].append({'dest_start':map_[0], 'source_start':map_[1], 'length':map_[2]})
        
        inp[m] = the_maps

# Find location number of each seed
lowest = float('inf')
for seed in inp[0]:
    cur = seed
    for m in range(1, len(inp)):
        the_maps = inp[m]
        for r in the_maps['maps']:
            if r['source_start'] <= cur <= r['source_start'] + r['length']:
                cur = r['dest_start'] + (cur - r['source_start'])
                break

    if cur < lowest:
        lowest = cur

print(lowest)