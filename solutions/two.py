with open('input2.txt') as f: # lines =f.readlines()
    L = [l.strip() for l in f]
score1 = 0
score2 = 0
for l in L:
    op = (l.split())[0]
    m = (l.split())[1]
    score1 += {'X': 1, 'Y': 2, 'Z': 3}[m]
    score1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
               ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
               ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
               }[(op, m)]
    score2 += {'X': 0, 'Y': 3, 'Z': 6}[m]
    score2 += {('A', 'X'): 3,('B', 'X'): 1, ('C', 'X'): 2,
               ('A', 'Y'): 1, ('B', 'Y'): 2,  ('C', 'Y'): 3,
               ('A', 'Z'): 2, ('B', 'Z'): 3,   ('C', 'Z'): 1
               }[(op, m)]
print(score1)
print(score2)
#%%
