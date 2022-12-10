with open('input10.txt') as f:
    L = f.readlines()

lines =  [line.strip() for line in L]

x = 1
cycles = []

for line in lines:
    if line == "noop":
        cycles.append(x)
    else:
        cycles.append(x)
        cycles.append(x)
        v = int(line.split()[1])
        x += v

strengths = sum((number_of_cycle + 1)*x
                for number_of_cycle, x in list(enumerate(cycles))[19:221:40])
print(strengths)

for i in range(0, len(cycles), 40):
    for j in range(40):
        print(end="#" if abs(cycles[i + j] - j)<= 1 else ".")
    print()
#%%
