from collections import deque

with open('input20.txt') as file:
    L_one = [int(line) for line in file.read().strip().split('\n')]

j = 0

L_one = deque((list(enumerate(L_one))))


L_two = [line*811589153 for line in L_one]
L_two= deque((list(enumerate(L_two))))

def answer(r, l):
    for _ in range(r):
        for i in range(len(l)):
            while l[0][0]!= i:
                l.append(l.popleft())
            move = l.popleft()
            new = move[1] % len(l)
            assert 0 <= new < len(l)
            for _ in range(new):
                l.append(l.popleft())
            l.append(move)
    for j in range(len(l)):
        if l[j][1] == 0:
            break

     return (l[(j+1000)%len(l)][1] +
            l[(j+2000)%len(l)][1] +
            l[(j+3000)%len(l)][1])
# part 1

print(answer(1, L_one))
# part 2 - print(answer(10, L_two))

#%%
