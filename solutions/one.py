with open('input.txt') as f:
    lines =f.readlines()
sum_cal = 0
max_cal = 0
for l in lines:
    try:
        sum_cal += int(l)
    except:
        max_cal = max(max_cal, sum_cal)
        sum_cal = 0
max_three = [0,0,0]
sum_caltwo = 0
for l in lines:
    try:
        sum_caltwo += int(l)
    except:
        if min(max_three) < sum_caltwo:
            max_three.remove(min(max_three))
            max_three.append(sum_caltwo)
        sum_caltwo = 0
print(max_cal, max_three, sum(max_three))
