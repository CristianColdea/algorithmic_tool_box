# Uses python2
import sys

def binary_search(a, x, left = None, right = None):
    if left == None:
        left = 0
    if right == None:
        right = len(a) - 1

    mid = left + (right - left) / 2

    while left <= right:        
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
            return binary_search(a, x, left, right)
        elif x > a[mid]:
            left = mid + 1
            return binary_search(a, x, left, right)

    return -1
 
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print (binary_search(a, x)),
#        print(linear_search(a, x)),
