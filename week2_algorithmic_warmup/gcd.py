#Uses python2

A = [int(x) for x in raw_input().split()]

def GCD(n1, n2):
    gcd = min(n1, n2)
    first = max(n1, n2)
    rem = first%gcd
    while rem != 0:
        first = gcd
        second = rem 
        rem = first%second
        gcd = second
    return gcd

print GCD(A[0], A[1])    
