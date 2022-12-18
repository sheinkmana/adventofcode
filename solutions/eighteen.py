#part one
from collections import deque

with open('input18.txt') as file:
    coordinates = [tuple(map(int, line.split(","))) for line in file.readlines()]

deltas = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]
sides = dict()

for coordinate in coordinates:
    x, y, z = coordinate
    for dx, dy, dz in deltas:
        k = (x + dx, y + dy, z + dz)
        if k not in sides:
            sides[k] = 0
        sides[k] += 1

#alternative way: print(sum([1 for i in sides.values() if i == 1])) (I don't know which is better)
print(list(sides.values()).count(1))


#part two

min_x = min_y = min_z = 1e7
max_x = max_y = max_z = -1e7

for coordinate in coordinates:
    x, y, z = coordinate
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    min_z = min(min_z, z)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

min_x -= 1
min_y -= 1
min_z -= 1

max_x += 1
max_y += 1
max_z += 1


q = deque([(min_x, min_y, min_z)])
inside = {(min_x, min_y, min_z)}
coordinates = set(coordinates)

deltas_two = [(0, 0, 1.0), (0, 1.0, 0), (1.0, 0, 0), (0, 0, -1.0), (0, -1.0, 0), (-1.0, 0, 0)]

while q:
    x, y, z = q.popleft()

    for dx, dy, dz in deltas_two:
        new_x, new_y, new_z  = (x + dx, y + dy, z + dz)

        if not (min_x <= new_x <= max_x
                and min_y <= new_y <= max_y
                and min_z <= new_z <= max_z):
            continue

        if (new_x, new_y, new_z)  in coordinates or (new_x, new_y, new_z) in inside:
            continue

        inside.add((new_x, new_y, new_z))
        q.append((new_x, new_y, new_z))

exterior = set()

for x, y, z in inside:
    for dx, dy, dz in deltas:
        if (x + dx, y + dy, z + dz) in set(sides):
            exterior.add((x + dx, y + dy, z + dz))

print(len(exterior))
