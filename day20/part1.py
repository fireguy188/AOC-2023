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

def find_inputs(m_name, lines):
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
        modules[m_name] = Conjunction(destinations, find_inputs(m_name, lines))

def send_pulse(pulse, m_name, instructions):
    for destination in modules[m_name].destinations:
        instructions.append((destination, pulse))
        if destination in modules and isinstance(modules[destination], Conjunction):
            modules[destination].memory[m_name] = pulse

def push_button():
    low_pulses, high_pulses = 0, 0
    # List of modules and what pulse to send
    instructions = [('broadcaster', 0)]
    for m_name, pulse in instructions:
        if pulse == 0:
            low_pulses += 1
        else:
            high_pulses += 1

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

    return (low_pulses, high_pulses)

total_low_pulses, total_high_pulses = 0, 0
for _ in range(1000):
    low_pulses, high_pulses = push_button()
    total_low_pulses += low_pulses
    total_high_pulses += high_pulses

print(total_low_pulses * total_high_pulses)
