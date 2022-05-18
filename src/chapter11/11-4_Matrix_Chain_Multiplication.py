INT_MAX = 99999

n = int(input())
p = [INT_MAX] * (n + 1)
for i in range(n):
    p[i], p[i + 1] = map(int, input().split())

m = [[INT_MAX] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    m[i][i] = 0

for h in range(2, n + 1):
    for i in range(1, n - h + 2):
        j = i + h - 1
        for k in range(i, j):
            m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j])

print(m[1][n])
