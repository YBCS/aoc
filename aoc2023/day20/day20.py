# day 20

data = open('test.txt', 'r').read().split('\n')
from collections import deque

# from https://github.dev/hyper-neutrino/advent-of-code/blob/main/2023/day20p1.py

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"


def part1(data):
    [print(d) for d in data]
    modules = {}
    broadcasts = []
    
    for line in data:
        left, right = line.strip().split(' -> ')
        inputs = right.split(', ')
        if left == "broadcaster":
            broadcasts = inputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, inputs)
    [print(k, v) for k,v in modules.items()]
    print()
    # populate the memory of the broadcaster
    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"
    [print(k, v) for k,v in modules.items()]

    # nah I am just copy pasting code at this point
    lo = hi = 0

    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        
        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                lo += 1
            else:
                hi += 1
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    print(lo * hi)

part1(data)