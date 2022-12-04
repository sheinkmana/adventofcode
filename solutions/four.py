with open('input4.txt') as input:
    L = [l.strip() for l in input]
number = 0
numbertwo =0
overlap = 0
for l in L:
    a, b = l.strip().split(',')
    ast, af = map(int, a.split('-'))
    bs, bf = map(int, b.split('-'))
    if ast <= bs and af >= bf:
        number+= 1
    elif bs <= ast and bf >= af:
        number += 1
    overlap = set(range(ast, af+1)) & set(range(bs, bf + 1))
    if overlap:
        numbertwo +=1
print(number)
print(numbertwo)
#%%
