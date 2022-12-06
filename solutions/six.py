with open('input6.txt') as f:
    L = f.read()
condition_one = False
condition_two= False
for i in range(len(L)):
    if (not condition_one) and i-3>=0 and \
            len(set([L[i-j] for j in range(4)]))==4:
        print(i+1)
        condition_one = True
    if (not condition_two) and i-13>=0 and\
            len(set([L[i-j] for j in range(14)]))==14:
        print(i+1)
        condition_two = True
