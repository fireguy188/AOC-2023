import networkx as nx
G = nx.Graph()

connections = {}
with open('input.txt') as inp: 
    for line in inp:
        name, components = line.split(': ')
        components = components.split()

        if not name in connections:
            connections[name] = set()

        for component in components:
            connections[name].add(component)
            if not component in connections:
                connections[component] = set()
            connections[component].add(name)


def explore_component(component, connections, forbidden):
    group = [component]
    seen = {component}
    for c in group:
        for connected in connections[c]:
            if (c, connected) in forbidden or (connected, c) in forbidden:
                continue

            if not connected in seen:
                group.append(connected)
                seen.add(connected)
    
    return group

# Generate list of wires
# wires = set()
# for component in connections:
#     for other_component in connections[component]:
#         if not (other_component, component) in wires:
#             wires.add((component, other_component))
# wires = list(wires)


def get_groups(connections, forbidden):
    components = set(connections.keys())
    groups = []

    while components:
        group = explore_component(components.pop(), connections, forbidden)
        for c in group:
            components.discard(c)
        groups.append(group)
    
    return groups

for component in connections:
    G.add_node(component)
    for other_component in connections[component]:
        G.add_edge(component, other_component)

wires = nx.minimum_edge_cut(G)
groups = get_groups(connections, wires)
print(len(groups[0]) * len(groups[1]))

# import matplotlib.pyplot as plt
# import scipy.sparse
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()
# (vbk, gqr)
# (klj, scr)
# (mxv, sdv)

#groups = get_groups(connections, [('vbk', 'gqr'), ('klj', 'scr'), ('mxv', 'sdv')])
#print(len(groups[0]) * len(groups[1]))
# for w1 in range(len(wires)):
#     wire1 = wires[w1]
#     if len(get_groups(connections, [wire1])) < 2:
#         for w2 in range(w1+1, len(wires)):
#             print(f'{w2}/{len(wires)}')
#             wire2 = wires[w2]
#             if len(get_groups(connections, [wire1, wire2])) < 2:
#                 for w3 in range(w2+1, len(wires)):
#                     wire3 = wires[w3]
                    
#                     #if ('pzl', 'hfx') in [wire1, wire2, wire3] and ('cmg', 'bvb') in [wire1, wire2, wire3] and ('jqt', 'nvd') in [wire1, wire2, wire3]:

#                     if len(get_groups(connections, [wire1, wire2, wire3])) == 2:
#                         print(get_groups(connections, [wire1, wire2, wire3]))
#                         input()
                        
