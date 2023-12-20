# 0 = low pulse
# 1 = high pulse

modules = {}

class Module:
    def __init__(self, destinations):
        self.destinations = destinations

class FlipFlop(Module):
    def __init__(self, destinations):
        super().__init__(destinations)
        self.on = 0
    
class Conjunction(Module):
    def __init__(self, destinations, inputs):
        super().__init__(destinations)
        self.memory = {name:0 for name in inputs}

class Broadcaster(Module):
    def __init__(self, destinations):
        super().__init__(destinations)

def find_inputs(m_name):
    inputs = []
    for line in lines:
        module, destinations = line.strip().split(' -> ')
        destinations = destinations.split(', ')

        if module == 'broadcaster':
            inp_name = 'broadcaster'
        else:
            inp_name = module[1:]

        if m_name in destinations:
            inputs.append(inp_name)
    
    return inputs

with open('input.txt') as inp:
    lines = inp.readlines()

for line in lines:
    module, destinations = line.strip().split(' -> ')
    destinations = destinations.split(', ')

    if module == 'broadcaster':
        modules['broadcaster'] = Broadcaster(destinations)
        continue

    m_type, m_name = module[0], module[1:]
    if m_type == '%':
        modules[m_name] = FlipFlop(destinations)
    elif m_type == '&':
        modules[m_name] = Conjunction(destinations, find_inputs(m_name))

big_boys = ['ps', 'kh', 'mk', 'ml']
for big_boy, big_boy_inputs in zip(big_boys, [find_inputs(big_boy) for big_boy in big_boys]):
    for m_name in big_boy_inputs:
        inputs = find_inputs(m_name)
        if 'broadcaster' in inputs:
            # All these radio hosts also have one other input
            # being their output
            # So broadcast does its thing, then if the whole thing isn't ready to burst,
            # it gets reset
            #
            # There is one of these guys for each of the 4 big boys
            # When pressed, it does a long cycle through all the little boys
            cur = m_name
            cycles = 0
            while True:
                #print(cur, big_boy_inputs)
                #input()
                cycles += 1
                destinations = modules[cur].destinations
                for dest in destinations:
                    if not dest in big_boys:
                        cur = dest
                        break
                else:
                    break
        else:
            pass

# glossary:
# big boy: one of the 4 conjunctions that need to output 0
# radio host: one of the special 4 flip flops that connects to a big boy.
# (it's called a radio host cause the broadcaster connects to it)
# (also fun and important fact, the broadcaster ONLY connects to radio hosts)
# ready to burst: all 4 big boys output 0 at the same time
# little boy: flip flop that connects to a big boy

# Literally everything above is working out
def send_pulse(pulse, m_name, instructions):
    for destination in modules[m_name].destinations:
        instructions.append((destination, pulse))
        if destination in modules and isinstance(modules[destination], Conjunction):
            modules[destination].memory[m_name] = pulse

def reset():
    for m_name in modules:
        if isinstance(modules[m_name], FlipFlop):
            modules[m_name].on = 0
        elif isinstance(modules[m_name], Conjunction):
            modules[m_name].memory = {m:0 for m in modules[m_name].memory}

def push_button():
    # List of modules and what pulse to send
    instructions = [('broadcaster', 0)]
    for m_name, pulse in instructions:
        if not m_name in modules:
            continue

        if isinstance(modules[m_name], Broadcaster):
            send_pulse(pulse, m_name, instructions)
        elif isinstance(modules[m_name], Conjunction):
            for mem_pulse in modules[m_name].memory.values():
                if mem_pulse == 0:
                    send_pulse(1, m_name, instructions)
                    break
            else:
                send_pulse(0, m_name, instructions)
        elif isinstance(modules[m_name], FlipFlop):
            if pulse == 0:
                modules[m_name].on = 1 - modules[m_name].on
                send_pulse(modules[m_name].on, m_name, instructions)

cycle_lengths = []
for big_boy in big_boys:
    # Find the radio host
    for inp_name in find_inputs(big_boy):
        if 'broadcaster' in find_inputs(inp_name):
            radio_host = inp_name
            break

    cycle_length = 0
    reset()
    while True:
        for m_name, state in modules[big_boy].memory.items():
            if state == 1 and m_name == radio_host or state == 0 and m_name != radio_host:
                break
        else:
            break
        push_button()
        cycle_length += 1
    cycle_lengths.append(cycle_length+1)

# higher than 17592186044416 (2^11)^4
# lower than 281200199450625 (2^12-1)^4
import math
print(math.lcm(*cycle_lengths))
#print(math.lcm(2**11+2**10+2**9+2**8+7, 2**11+2**10+2**9+2**8+2**7+33, 2**11+2**10+2**9+2**8+37, 2**11+2**10+2**9+239))