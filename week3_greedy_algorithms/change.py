# Uses python 2

n = int(raw_input())

def Coins(n):
    if n == 0:
        return 0
    else:
        output = int(n / 10)
        rest10 = n % 10
        output = output + rest10 / 5 + rest10 % 5
    return output

print(Coins(n))
