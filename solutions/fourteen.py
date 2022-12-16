#use complex numbers in order to consider both axis in one number
# y coordinate is for the imag part, x coordinate is for the real part

with open('input14.txt') as file:
    L = [[list(map(int, l.split(","))) for l in line.strip().split("->")]
         for line in file.readlines()]

sand = set()
abyss = 0

for l in L: # (x1,y1) is any of the tuples,
    # (x2,y2) is in any except for the very first one
    for (x1, y1), (x2, y2) in zip(l, l[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                sand.add(x + y * 1j)
                abyss = max(abyss, y + 1)
delta = len(sand)

part = 2
#part = 1
if part == 1:
    while True:
        l = 500
        while True:
            if l.imag >= abyss:
                print(len(sand) - delta)
                exit()
            if l + 1j not in sand:
                l += 1j
                continue
            if l + 1j - 1 not in sand:
                l += 1j - 1
                continue
            if l+ 1j + 1 not in sand:
                l += 1j + 1
                continue
            sand.add(l)
            break
else:
    while 500 not in sand:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in sand:
                 s += 1j
                 continue
            if s + 1j + 1 not in sand:
                s += 1j + 1
                continue
            if s + 1j - 1 not in sand:
                s += 1j - 1
                continue
            break
         sand.add(s)
    print(len(sand) - delta)


#part two
















#%%
