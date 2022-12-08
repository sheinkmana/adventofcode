with open('input8.txt') as f:
    L = f.read().splitlines()

lattice = [list(map(int, line)) for line in L]

visible_trees = 0
score = 0

for y in range(len(lattice)):
    for x in range(len(lattice[y])):
        tree = lattice[y][x]
        if all(lattice[y][i] < tree for i in range(x)) or \
                all(lattice[y][i] < tree for i in range(x + 1, len(lattice[y]))) or\
                all(lattice[i][x] < tree for i in range(y)) or\
                all(lattice[i][x] < tree for i in range(y + 1, len(lattice))):
            visible_trees += 1
        L = R = U = D = 0
        for i in range(x-1, -1, -1):
            L += 1
            if lattice[y][i] >= tree:
                break
        for i in range(x+1, len(lattice[y])):
            R += 1
            if lattice[y][i] >= tree:
                break
        for i in range(y-1 , -1, -1):
            U += 1
            if lattice[i][x] >= tree:
                break
        for i in range(y+1, len(lattice)):
            D += 1
            if lattice[i][x] >= tree:
                break
        score = max(score, L*R*U*D)

print(visible_trees)
print(score)
#%%
