# Uses python2
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    maxa = 0
    for i in a:
        if i > maxa:
            maxa = i
    b = [0] * (maxa + 1)
    
    for i in a:
        b[i] = b[i] + 1
    max = 0
    for i in b:
        if i > max:
            max = i
    if max > (len(a) / 2):
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
   
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
