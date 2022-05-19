n = int(input())

us = []
ks = []
vs = []
for i in range(n):
    u, k, *v = list(map(int, input().split()))
    us.append(u)
    ks.append(k)
    vs.append(v)


def DFS(u, V):
    global time

    now_idx = u - 1
    if detected[now_idx] == -1:
        detected[now_idx] = time
        time += 1

    for v in V:
        next_idx = v - 1
        if detected[next_idx] == -1:
            DFS(us[next_idx], vs[next_idx])

    if finished[now_idx] == -1:
        finished[now_idx] = time
        time += 1


time = 1
detected = [-1] * n  # そのノードを最初に訪問した発見時刻
finished = [-1] * n  # そのノードの隣接リストを調べ終えた完了時刻
for i in range(n):
    if detected[i] == -1:
        DFS(us[i], vs[i])

for i in range(n):
    print(i + 1, detected[i], finished[i])
