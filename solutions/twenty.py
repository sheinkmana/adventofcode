# this one is not fully mine

from collections import deque

with open("input20.txt") as file:
   lines = file.read().splitlines()


groove_sum = 0

def groove(part):
    L = [int(l) for l in lines]

    if part == 2:
        L = [l*811589153 for l in L]

    L = deque(list(enumerate(L)))


    if part==2:
        for t in range(10):
            for i in range(len(L)):
                for j in range(len(L)):
                    if L[j][0]==i:
                        break
                while L[0][0]!=i:
                    L.append(L.popleft())
                new = L.popleft()
                new_pop = new[1] % len(L)
                assert 0<= new_pop < len(L)

                for _ in range(new_pop):
                    L.append(L.popleft())
                L.append(new)
    else:
        for t in range(1):
            for i in range(len(L)):
                for j in range(len(L)):
                    if L[j][0]==i:
                        break
                while L[0][0]!=i:
                    L.append(L.popleft())
                new = L.popleft()
                new_pop = new[1]% len(L)
                assert 0<=new_pop < len(L)

                for _ in range(new_pop):
                    L.append(L.popleft())
                L.append(new)


    for j in range(len(L)):
        if L[j][1] == 0:
            break

    groove_sum = L[(j+1000)%len(L)][1]+ L[(j+2000)%len(L)][1]\
                 + L[(j+3000)%len(L)][1]

    return groove_sum


print(groove(2))


