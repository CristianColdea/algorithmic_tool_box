# Uses python2
m = int(raw_input())

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
    return (i + 1)

p = (PisanoPeriod(m))
print p
