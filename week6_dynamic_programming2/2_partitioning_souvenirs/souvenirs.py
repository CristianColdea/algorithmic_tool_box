# Uses python2
import sys

def partition3(A):
    third, module = divmod(sum(A), 3)
    if len(A) < 3 or module or max(A) > third:
        return 0

    DP = [[0] * (len(A) + 1) for _ in range(third + 1)]
    taken = [[0] * (len(A) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(A) + 1):
            if DP[i][j-1] == 2:
                DP[i][j] = 2
                continue

            if A[j-1] == i:
                DP[i][j] = 1 if DP[i][j-1] == 0 else 2
                taken[i][j] = j
                continue

            ii = i - A[j-1]

            available = True
            taken_id = taken[ii][j-1]
            if taken_id:
                for jj in range(1, j):
                    if taken[ii][jj] == taken_id:
                        if taken[i][jj]:
                            available = False
                            break

            if ii > 0 and DP[ii][j-1] > 0 and not taken[i][j-1] and available:
                DP[i][j] = 1 if DP[i][j-1] == 0 else 2

                taken[i][j] = j
                taken[i][j-1] = j

                matcher = A[j-1] + A[j-2]
                if taken_id:
                    for jj in range(1, len(A)):
                        if taken[ii][jj] == taken_id:
                            taken[i][jj] = j
                            matcher += A[jj-1]
                if matcher < i:
                    for jj in range(j - 2, 0, -1):
                        if taken[i][jj] or matcher + A[jj - 1] > i:
                            continue
                        matcher += A[jj - 1]
                        taken[i][jj] = j
                        if matcher == i:
                            break
            else:
                DP[i][j] = DP[i][j-1]

    return 1 if DP[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))

print partition3(A[1:])
