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

# Pisano period for 10 is 60
# Sum(n) = F(n + 2) - 1
# Sum(n)%10 = F(n + 2)%10 - 1
p = n % 60
fib_part = FibList(p + 2)
if (fib_part % 10) == 0:
    print 9
else:
    print (fib_part % 10) - 1
