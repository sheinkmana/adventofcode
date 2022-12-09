
def crate_mover(stacks, command, model):
    number_of_crates, start, end = list(map(int, command.split()[1::2]))
    if model=='9000':
        stacks[end-1] += stacks[start-1][-number_of_crates:][::-1]
    if model=='9001':
        stacks[end-1] += stacks[start-1][-number_of_crates:]
    stacks[start-1] = stacks[start-1][:-number_of_crates]
    return stacks

with open('input5.txt') as f:
    lines = f.read().splitlines()
#part one
commands = lines[lines.index('')+1:]
stacks = lines[:lines.index('')-1]
stacks = [[l[j] for l in stacks if l[j] != ' '][::-1] for j in range(1,len(lines[0]),4)]
for command in commands:
    crate_mover(stacks, command, '9000')
print(''.join([stack[-1] for stack in stacks]))
#part_two
stacks = lines[:lines.index('')-1]
stacks = [[l[j] for l in stacks if l[j] != ' '][::-1] for j in range(1,len(lines[0]),4)]
for command in commands:
    crate_mover(stacks, command, '9001')
print(''.join([stack[-1] for stack in stacks]))
#%%
