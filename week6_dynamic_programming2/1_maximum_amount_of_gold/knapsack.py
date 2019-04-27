# Uses python2
import sys

def optimal_weight(W, w):
    values = [[None] * (W + 1) for i in xrange(len(w) + 2)]
    for i in xrange(len(w) + 1):
        values[i][0] = 0
    for i in xrange(1, W + 1):
        values[0][i] = 0

    for i in xrange(1, len(w) + 1):
        for j in xrange(1, W + 1):
            values[i][j] = values[i - 1][j]
            if w[i - 1] <= j:
                val = values[i - 1][j - w[i - 1]] + w[i - 1]
                if values[i][j] < val:
                    values[i][j] = val

    return values[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    W = data[0]
    w = data[2:]
    print(optimal_weight(W, w))
