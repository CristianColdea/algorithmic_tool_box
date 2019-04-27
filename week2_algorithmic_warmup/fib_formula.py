n = int(raw_input())

F = [0] * (n + 1)
for i in range(0, n + 1):
    F[i] = int(1 /5 ** 0.5 * (((1 + 5 ** 0.5) / 2) ** i -((1 - 5 ** 0.5)/2) ** i))

print F
