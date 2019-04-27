# Uses python2

n = int(raw_input())

def FibList(n):
    F = [0] * (n + 1)
    if n == 0:
        F[0] = 0
    else:
        F[0] = 0
        F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 2] + F[i - 1]
    return F[n]

sum = FibList(n + 2) - 1
# print sum
print sum%10
