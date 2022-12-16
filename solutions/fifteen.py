with open('input15.txt') as file:
    lines = [l for l in file.read().strip().split('\n')]

S = set()
B = set()

for line in lines:
    line = line.split()
    sensor_x, sensor_y = line[2],line[3]
    beacon_x, beacon_y = line[8],line[9]
    sensor_x = int(sensor_x[2:-1])
    sensor_y = int(sensor_y[2:-1])
    beacon_x = int(beacon_x[2:-1])
    beacon_y = int(beacon_y[2:])
    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    S.add((sensor_x, sensor_y, dist))
    B.add((beacon_x, beacon_y))

def closest(x,y,S):
    for (sensor_x, sensor_y, dist) in S:
        dist_new = abs(x-sensor_x) + abs(y-sensor_y)
        if dist_new <= dist:
            return False
    return True

cant = 0
for x in range(-10000000, 10000000):
    y = 2000000
    if not closest(x,y,S):
        if (x,y) not in B:
            cant += 1
print(cant)


distress = False

for (sensor_x, sensor_y, dist) in S:
    for x in range(dist+2):
        y = (dist+1) - x
        for tune_x,tune_y in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            new_x = sensor_x+(x*tune_x)
            new_y = sensor_y+(y*tune_y)
            if not (0 <= new_x <= 4000000) or not (0 <= new_y <=4000000):
                continue
            assert abs(new_x-sensor_x)+abs(new_y-sensor_y) == dist + 1
            if closest(new_x,new_y,S):
                if (not distress):
                    print(new_x*4000000 + new_y)
                    distress = True


