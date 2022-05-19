from collections import deque


n = int(input())
us = []
ks = []
vs = []
for i in range(n):
    u, k, *v = list(map(int, input().split()))
    us.append(u)
    ks.append(k)
    vs.append(v)


def BFS(start):
    global distances
    distances[start - 1] = 0
    Q = deque([start])
    while len(Q) > 0:
        u = Q.popleft()
        for v in vs[u - 1]:
            if distances[v - 1] != -1:  # 探索済み
                continue
            distances[v - 1] = distances[u - 1] + 1
            Q.append(v)


distances = [-1] * n
BFS(1)

for i, d in enumerate(distances):
    print(i + 1, d)
