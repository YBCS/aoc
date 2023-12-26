# day 19

data = open('test.txt', 'r').read().split('\n')

def explore(flows, flow, lookup): # bool: accepted or rejected
    ins = flows[flow]
    for i, val in enumerate(ins):
        if i == len(ins)-1:
            if val == "A" or val == "R":
                return val == "A"
            return explore(flows, val, lookup)
        condition, outcome = val.split(':')
        item = condition[0]
        sign = condition[1]
        amt = int(condition[2:])

        comp = lookup[item]
        if sign == ">":
            if comp > amt:
                if outcome == "A" or outcome == "R":
                    return outcome == "A" 
                return explore(flows, outcome, lookup)
        else: # "<"
            if comp < amt:
                if outcome == "A" or outcome == "R":
                    return outcome == "A"
                return explore(flows, outcome, lookup)
    print("should not reach here")
    return -1

def part1(data):
    # print('data is ', data)
    workflows = {}
    ans = 0
    for instruction in data:
        if instruction and instruction[0] == "{": # second part of input
            instruction = instruction[1:-1]
            x,m,a,s = instruction.split(',')
            x = int(x[2:])
            m = int(m[2:])
            a = int(a[2:])
            s = int(s[2:])
            lookup = {'x':x, 'm': m, 'a': a, 's': s}
            # print(lookup)
            out = explore(workflows, 'in', lookup)
            print(f'{lookup} has out {out}')
            if out:
                ans += sum(lookup.values())
        else:
            if instruction: # first part
                s = instruction.find('{')
                workflow = instruction[:s]
                workflows[workflow] = instruction[s:][1:-1].split(',') # can I use this to generate a sample program
    [print(k,v) for k,v in workflows.items()]
    print('final ans is ', ans)

# NOTE : incomplete
# interesting recursive brute force approach
def part2(data):
    workflows = {}
    ans = 0
    for instruction in data:
        if instruction and instruction[0] == "{": # second part of input
            instruction = instruction[1:-1]
            x,m,a,s = instruction.split(',')
            x = int(x[2:])
            m = int(m[2:])
            a = int(a[2:])
            s = int(s[2:])
            lookup = {'x':x, 'm': m, 'a': a, 's': s}
            # in part2 lookup is no longer relevant; we need to use just the workflow

            # out = explore(workflows, 'in', lookup)
            # print(f'{lookup} has out {out}')
            print(f'{lookup}')
            # if out:
            #   ans += sum(lookup.values())
        else:
            if instruction: # first part
                s = instruction.find('{')
                workflow = instruction[:s]
                workflows[workflow] = instruction[s:][1:-1].split(',') # can I use this to generate a sample program
    [print(k,v) for k,v in workflows.items()]
    # print('final ans is ', ans)

# part1(data)
part2(data)


## note what is taking you time