with open('input.txt') as inp: 
    inp = inp.read().strip().split('\n\n')

for m in range(len(inp)):
    if m == 0:
        inp[0] = [int(seed) for seed in inp[0].split(': ')[1].split()]
        seeds = []
        for pair in range(0, len(inp[0]), 2):
            seeds.append({'start':inp[0][pair], 'end':inp[0][pair]+inp[0][pair+1]-1})
        inp[0] = seeds
    else:
        map_name, maps = inp[m].split(':\n')
        source_name, dest_name = map_name.split('-to-')
        the_maps = {'source':source_name, 'dest':dest_name[:-4], 'maps':[]}
        for map_ in maps.split('\n'):
            map_ = [int(x) for x in map_.split()]
            the_maps['maps'].append({'dest_start':map_[0], 'source_start':map_[1], 'dest_end':map_[0]+map_[2]-1, 'source_end':map_[1]+map_[2]-1})
        
        the_maps['maps'].sort(key=lambda x: x['source_start'])
        inp[m] = the_maps

def split_range(source_ranges, the_maps):
    # takes in (list of ranges of sources and a list of maps)
    # returns list of new dest ranges
    new_dest_ranges = []
    for s_range in source_ranges:
        # find the maps this s_range relates to
        for the_map in the_maps:
            new_source_range = {'start':max(s_range['start'], the_map['source_start']),
                                'end':min(s_range['end'], the_map['source_end'])}
            # Check if it is valid
            if new_source_range['start'] <= new_source_range['end']:
                # Convert to the corresponding destination range
                new_dest_range = {'start':the_map['dest_start'] + (new_source_range['start'] - the_map['source_start'])}
                new_dest_range['end'] = new_dest_range['start'] + (new_source_range['end'] - new_source_range['start'])
                new_dest_ranges.append(new_dest_range)
        
        # Also add parts completely not in any maps
        fake_maps = []
        fake_maps.append({'source_start':-float('inf'), 'source_end':the_maps[0]['source_start']-1})
        for m in range(len(the_maps)-1):
            fake_maps.append({'source_start':the_maps[m]['source_end']+1, 'source_end':the_maps[m+1]['source_start']-1})
        fake_maps.append({'source_start':the_maps[-1]['source_end']+1, 'source_end':float('inf')})

        for the_map in fake_maps:
            new_dest_range = {'start':max(s_range['start'], the_map['source_start']),
                                'end':min(s_range['end'], the_map['source_end'])}
            
            if new_dest_range['start'] <= new_dest_range['end']:
                new_dest_ranges.append(new_dest_range)
    
    return new_dest_ranges


# Find location number of each seed
lowest = float('inf')
for seed_range in inp[0]:
    cur = [seed_range]
    for m in range(1, len(inp)):
        the_maps = inp[m]
        cur = split_range(cur, the_maps['maps'])

    for r in cur:
        if r['start'] < lowest:
            lowest = r['start']

print(lowest)