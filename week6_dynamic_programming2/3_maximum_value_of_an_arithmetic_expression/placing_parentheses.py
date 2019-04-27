# Uses python2
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):

    def MinAndMax(i, j, op):
        min = sys.maxint
        max = - sys.maxint
        
        for k in range(i,j - 1):
            a = evalt(max(i, k), max(k + 1, j), op)
            b = evalt(max(i, k), min(k + 1, j), op)
            c = evalt(min(i, k), max(k + 1, j), op)
            d = evalt(min(i, k), min(k + 1, j), op)
            min = min(min, a, b, c, d)
            max = max(max, a, b, c, d)

        return(min, max)
    
    dimension = 1 + len(dataset) / 2
    m = [[0] * (dimension) for _ in range(dimension)]
    M = [[0] * (dimension) for _ in range(dimension)]

    for i in range(dimension):
        m[i][i] = dataset[i * 2]
        M[i][i] = dataset[i * 2]

    for s in range(dimension - 1):
        for i in range(dimension - s):
            j = i + s
            min[i][j], M[i][j] = (MinAndMax(dataset[2 * i], dataset[2 * j],
dataset[2 * i + 1]))
    return M(1, dimension - 1)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(input)
    for x in range(0, len(data), 2):
        data[x] = int(data[x])
    del data[-1]
    print data
#    print(get_maximum_value(data))
