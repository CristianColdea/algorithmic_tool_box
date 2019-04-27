# Uses python 2
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0
    # computing value/weight ratios and have them sorted properly
    ones = [1.0] * len(weights)
    ratios = [(v * o)/w for v, w, o in zip(values, weights, ones)]
    indx = np.argsort(ratios)
    indx = indx[::-1]
    ratios.sort(reverse=True)
    
    #allocating weights
    restw = 0
    for i in range(0, len(weights)):
        if capacity == 0:
            return value
        else:
            crtw = min(capacity, weights[indx[i]])
            value = value + crtw * ratios[i]
            weights[indx[i]] = weights[indx[i]] - crtw
            capacity = capacity - crtw
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value)) 
