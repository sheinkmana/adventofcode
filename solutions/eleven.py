from copy import deepcopy

with open('input11.txt') as f:
    L = [l.splitlines() for l in f.read().strip().split("\n\n")]

monkeys = []

for i in range(len(L)):
    monkey = []
    monkey.append(list(map(int, L[i][1].split(": ")[1].split(", "))))
    monkey.append(( L[i][2].split("=")[1]))
    for line in L[i][3:]:
        monkey.append(int(line.split()[-1]))
    monkeys.append(monkey)

monkeys_two = deepcopy(monkeys)

def round_one(monkeys):
    for number, monkey in enumerate(monkeys):
        for item in monkey[0]:
            operation = eval("lambda old:" + monkey[1])
            item =operation(item)
            item //= 3
            if item % monkey[2] == 0:
                monkeys[monkey[3]][0].append(item)
            else:
                monkeys[monkey[4]][0].append(item)
        inspections[number] += len(monkey[0])
        monkey[0]= []
    return inspections


inspections = [0] * len(monkeys)

for _ in range(20):
    round_one(monkeys)

inspections.sort(reverse=True)
business = inspections[0]*inspections[1]
print(business)

## part two

inspections = [0] * len(monkeys)

div = 1
for monkey in monkeys:
    div *=monkey[2]

def round_two(monkeys):
    for index, monkey in enumerate(monkeys):
        for item in monkey[0]:
            op = eval("lambda old:" + monkey[1] )
            item = op(item)
            item %= div
            if item % monkey[2] == 0:
                monkeys[monkey[3]][0].append(item)
            else:
                monkeys[monkey[4]][0].append(item)
        inspections[index] += len(monkey[0])
        monkey[0] = []
    return inspections

for _ in range(10000):
    round_two(monkeys_two)

inspections.sort(reverse=True)
business = inspections[1] * inspections[0]
print(business)



#%%
