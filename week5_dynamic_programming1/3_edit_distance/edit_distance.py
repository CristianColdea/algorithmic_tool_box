# Uses python2
import sys

def edit_distance(s, t):
    dist = {}
    for i in range(len(s) + 1):
        dist[i, 0] = i
    for j in range(len(t) + 1):
        dist[0, j] = j
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            ins = dist[i, j - 1] + 1
            dels = dist[i - 1, j] + 1
            match = dist[i - 1, j - 1]
            mismatch = dist[i - 1, j - 1] + 1
            if s[i - 1] == t[j - 1]:
                dist[i, j] = min(ins, dels, match)
            else:
                dist[i, j] = min(ins, dels, mismatch)
    print dist[len(s), len(t)]
    return 0

if __name__ == "__main__":
    input = sys.stdin.read()
    lines = input.split()

s = lines[0]
t = lines[1]

edit_distance(s, t)
