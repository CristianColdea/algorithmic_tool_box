# Uses python2
import sys

def operations(n):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    sequence.append(1)
    
    for amount in range(4, n + 1):
        by_one = sequence[amount - 2] + 1
        by_two = sequence[(amount)/2 - 1] + 1 + amount % 2
        by_three = sequence[(amount)/3 - 1] + 1 + amount % 3
        added = min(by_one, by_two, by_three)
        sequence.append(added)
    
    return sequence    

input = sys.stdin.read()
n = int(input)

ops = operations(n)
def seqvence(n):
    sequence2 = []
    sequence2.append(n)

    while n > 1:
        one = ops[n - 2] + 1
        two = ops[(n)/2 - 1] + 1 + n % 2
        three = ops[(n)/3 - 1] + 1 + n % 3
        if min(one, two, three) == one:
            n = n - 1
            sequence2.append(n)
        elif min(one, two, three) == two:
            if n % 2 != 0:
                sequence2.append(n - (n%2))
            n = n / 2
            sequence2.append(n)
        elif min(one, two, three) == three:
            if n % 3 == 1:
                sequence2.append(n - 1)
            elif n % 3 == 2:
                sequence2.append(n - 1)
                sequence2.append(n - 2)
            n = n / 3
            sequence2.append(n)
    return sequence2

print ops[n - 1]
seq = seqvence(n)
seq.reverse()
for x in seq:
    print x,
