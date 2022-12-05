with open('input4.txt') as input:
    L = [l.strip() for l in input]
number = 0
numbertwo = 0
overlap = 0
for l in L:
    interval_one, interval_two = l.strip().split(',')
    interval_one_start, interval_one_finish = map(int, interval_one.split('-'))
    interval_two_start, interval_two_finish = map(int, interval_two.split('-'))
    if interval_one_start <= interval_two_start and interval_one_finish >= interval_two_finish:
        number+= 1
    elif interval_two_start <= interval_one_start and interval_two_finish >= interval_one_finish:
        number += 1
    overlap = set(range(interval_one_start, interval_one_finish+1)) &\
              set(range(interval_two_start, interval_two_finish + 1))
    if overlap:
        numbertwo +=1
print(number)
print(numbertwo)

#%%
