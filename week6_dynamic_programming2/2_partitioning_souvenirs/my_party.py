# Uses python2
import sys

def partition3(A):
    total = sum(A)
    if len(A) < 3 or total % 3:
        return 0
    A.sort()
    A.reverse()
    print A
    print total
    setA, setB, setC = [], [], []
    
    setA.append(A[0])
    setB.append(A[1])
    setC.append(A[2])
    for i in xrange(3, len(A)):
        to_add = min(setA[i - 3], setB[i - 3], setC[i - 3])
        if to_add == setA[i - 3]:
            setA.append(A[i])
            setB.append(sum(setB))
            setC.append(sum(setC))
        elif to_add == setB[i - 3]:
            setB.append(A[i])
            setA.append(sum(setA))
            setC.append(sum(setC))
        else:
            setC.append(A[i])
            setA.append(sum(setA))
            setB.append(sum(setB))

    print setA[-1], setB[-1], setC[-1]
    if setA[-1] == setB[-1] and setB[-1] == setC[-1]:
        return 1
    else:
        return 0
if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))
    print(partition3(A[1:]))

