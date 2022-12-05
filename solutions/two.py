with open('input2.txt') as f: # lines =f.readlines()
    L = [l.strip() for l in f]
score1 = 0
score2 = 0
dict_one = {'X': 1, 'Y': 2, 'Z': 3}
dict_two = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3 }
dict_three = {'X': 0, 'Y': 3, 'Z': 6}
dict_four = {('A', 'X'): 3,('B', 'X'): 1, ('C', 'X'): 2,
             ('A', 'Y'): 1, ('B', 'Y'): 2,  ('C', 'Y'): 3,
             ('A', 'Z'): 2, ('B', 'Z'): 3,   ('C', 'Z'): 1
             }
for l in L:
    op = (l.split())[0]
    m = (l.split())[1]
    score1 += dict_one[m]
    score1 += dict_two[(op, m)]
    score2 += dict_three[m]
    score2 += dict_four[(op, m)]
print(score1)
print(score2)
#%%
