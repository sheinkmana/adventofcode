with open('input25.txt') as file:
    data = file.read().splitlines()

convert = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

def decimal(l):
    place = 5 ** (len(l) - 1)
    dec = 0
    for digit in l:
        dec += convert[digit] * place
        place //= 5
    return dec


def SNAFU(decimal):
    snaf = ''
    while decimal:
        decimal, digit = divmod(decimal, 5)
        if digit > 2:
            decimal += 1
            if digit == 3:
                snaf += '='
            else:
                snaf += '-'
        else:
            snaf += str(digit)
    return snaf[::-1]

decimal_data = 0

for l in data:
    decimal_data += decimal(l)

print(SNAFU(decimal_data))
#%%
