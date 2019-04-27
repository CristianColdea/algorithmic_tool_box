# Uses python2

A = [int(x) for x in raw_input().split()]

def LCM(n1, n2):
    prod = n1 * n2
    first = max(n1, n2)
    second = min(n1, n2)
    rem = first % second
    while rem != 0:
        first = second
        second = rem
        rem = first % second
    return prod / second

print LCM(A[0], A[1])
