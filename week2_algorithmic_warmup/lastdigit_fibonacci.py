# Uses python2

n = int(raw_input())

def LastDigitFib(n):
    F = [None] * (n + 1)
    if n == 0:
        F[0] = 0
    else:
        F[0] = 0
        F[1] = 1
    for i in range(2, n + 1):
        F[i] = (F[i - 2]%10 + F[i - 1]%10)%10
    return F[n]

print LastDigitFib(n)
