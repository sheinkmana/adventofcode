def connect(H,T):
    d_x = (H[0]-T[0])
    d_y = (H[1]-T[1])
    if abs(d_x)<=1 and abs(d_y)<=1:
        pass
    elif abs(d_x)==2 and abs(d_y)==2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(d_x)==2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(d_y)==2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T

with open('input9.txt') as f:
    L = f.readlines()

lines =  [line.strip().split() for line in L]

H = (0,0)
T = [(0,0) for _ in range(9)]
moves_x = {'L': 0, 'U': 1, 'R': 0, 'D': -1}
moves_y = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
positions = {T[0]}
positions_two = {T[8]}
for line in lines:
    direction, length = line
    length = int(length)
    for _ in range(length):
        H = (H[0] + moves_x[direction], H[1]+moves_y[direction])
        T[0] = connect(H, T[0])
        positions.add(T[0])
        for i in range(1,9):
            T[i] = connect(T[i-1], T[i])
        positions_two.add(T[8])
print(len(positions))
print(len(positions_two))

#%%
