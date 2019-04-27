import sys

def binSearch(a, x):
    def recurse(first, last):
        mid = (first + last) / 2
        if first > last:
            return -1
        elif (a[mid] < x):
            return recurse(mid + 1, last)
        elif (a[mid] > x):
            return recurse(first, mid - 1)
        else:
            return mid
    return recurse(0, len(a) - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print (binSearch(a, x))
