# Uses python2
import sys
import random

def partition3(a, l, r):
    j = l
    x = a[l]
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
 
    k = j
    for t in range(j + 1, r + 1):
        if a[t] == a[j]:
            a[t], a[k + 1] = a[k + 1], a[t]
            k += 1 
    return j, k + 1

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    j, s = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, j - 1);
    randomized_quick_sort(a, s, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    #j, k = partition3(a, 0, n - 1)
    #print j, k, a

    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x),
