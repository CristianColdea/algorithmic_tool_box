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
fib_partm = FibList(pm + 2)
fib_partn = FibList(pn + 2)

fib_partm_mod = fib_partn_mod = 0

if (fib_partm % 10) == 0:
    fib_partm_mod = 10
else:
    fib_partm_mod = fib_partm % 10
if (fib_partn % 10) == 0:
    fib_partn_mod = 10
else:
    fib_partn_mod = fib_partn % 10

if m == n:
    print FibList(pm) % 10
else: 
    print fib_partn_mod - fib_partm_mod
