from collections import deque, defaultdict

rank = defaultdict(lambda : 1000000)

x_s,y_s = (0,0)
x_f,y_f = (1,1)


with open('input12.txt') as f:
    L = f.read().strip()

lattice = [list(l) for l in L.split("\n")]
for i in range(len(lattice)):
    for j in range(len(lattice[0])):
        if lattice[i][j] == "S":
            x_s,y_s = (i,j)
        if lattice[i][j] == "E":
            x_f,y_f = (i,j)

lattice[x_s][y_s] = "a"
lattice[x_f][y_f] = "z"

lattice = [[ord(r) - ord("a") for r in l] for l in lattice]


q_one = deque([(x_s,y_s)])
q_two = deque([(i,j) for i in range(len(lattice))
               for j in range(len(lattice[0])) if lattice[i][j] == 0])
moves = [(0,1),(1,0),(0,-1),(-1,0)]


for x,y in q_one:
    rank[x,y] = 0
while len(q_one) > 0:
    x,y = q_one.popleft()
    if (x,y) == (x_f,y_f):
        print(rank[x_f,y_f])
        break
    for x_m,y_m in moves:
        x_new,y_new = x+x_m,y+y_m
        if x_new in range(len(lattice)) and y_new in range( len(lattice[0])):
            if lattice[x][y] >= lattice[x_new][y_new] - 1:
                if rank[x,y] + 1 < rank[x_new,y_new]:
                    q_one.append((x_new,y_new))
                    rank[x_new,y_new] = rank[x,y] + 1



for x,y in q_two:
    rank[x,y] = 0
while len(q_two) > 0:
    x,y = q_two.popleft()
    if (x,y) == (x_f,y_f):
        print(rank[x_f,y_f])
        break
    for x_m,y_m in moves:
        x_new,y_new = x+x_m,y+y_m
        if x_new in range(len(lattice)) and y_new in range( len(lattice[0])):
            if lattice[x][y] >= lattice[x_new][y_new] - 1:
                if rank[x,y] + 1 < rank[x_new,y_new]:
                    q_two.append((x_new,y_new))
                    rank[x_new,y_new] = rank[x,y] + 1

#%%
