# Uses python2
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    b = {}
    for i in a:
        b[i] = b.get(i, 0) + 1
    v = list(b.values())
    if max(v) > (len(a) / 2):
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
