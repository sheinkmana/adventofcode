# I don't really like this one, but at least understand


from json import loads
from functools import cmp_to_key

def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])

    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v

    return len(x) - len(y)

with open('input13.txt') as l:
    L = l.read().replace('\n\n', '\n').splitlines()

right_pairs = 0
all_packets = list(map(loads, L))
packets = [all_packets[i:i + 2] for i in range(0, len(all_packets), 2)]

for i, (a, b) in enumerate(packets):
    if f(a, b) < 0:
        right_pairs += i + 1
print(right_pairs)

all_packets.extend(([[2]], [[6]]))
all_packets.sort(key=cmp_to_key(f))
decoder_key = (all_packets.index([[2]]) + 1)*(all_packets.index([[6]]) + 1)
print(decoder_key)

#%%
