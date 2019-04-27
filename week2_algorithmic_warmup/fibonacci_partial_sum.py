# Uses python2
a = [int(x) for x in raw_input().split()]
m = a[0]
n = a[1]

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

# Pisano period for 10 is 60
# Sum(n) = F(n + 2) - 1
# Sum(n)%10 = F(n + 2)%10 - 1

pm = m % 60
pn = n % 60

if m == n:
    print FibList(pm) % 10
else:
    print (FibList(pn + 2) - FibList(pm + 1)) % 10
