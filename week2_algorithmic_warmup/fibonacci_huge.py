# Uses python2

a = [int(x) for x in raw_input().split()]
m = a[1]
n = a[0]

# Computing Pisano period
def PisanoPeriod(n):
    if n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        c = a + b
        for i in range(0, n ** 2):
            c = (a + b) % n
            a = b
            b = c
            if a == 0 and b == 1:
                break
    return int((i + 1))

p = (PisanoPeriod(m))

# Computing Fibonacci number
def FibList(n):
    F = [0] * (n + 1)
    if n == 0:
        F[0] == 0
    else:
        F[0] = 0
        F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 2] + F[i - 1]
    return F[n]

# Computing/displaying modulo m
print FibList(n%p) % m 
