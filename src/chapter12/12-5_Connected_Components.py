#  解法1: TLE
# n, m = map(int, input().split())

# friends = [[0] * n for _ in range(n)]
# for _ in range(m):
#     s, t = map(int, input().split())
#     friends[s][t] = 1
#     friends[t][s] = 1


# def BDS(s, visited):
#     visited[s] = True
#     for i in range(n):
#         if friends[s][i] == 1 and not visited[i]:
#             BDS(i, visited)


# q = int(input())
# ans = []
# for _ in range(q):
#     s, t = map(int, input().split())
#     visited = [False] * n
#     BDS(s, visited)
#     ans.append("yes" if visited[t] else "no")

# print(*ans, sep="\n")

from collections import deque


n, m = map(int, input().split())

friends = [set() for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    friends[s].add(t)
    friends[t].add(s)


def assign_color(s, color_id):
    global color
    color[s] = color_id
    Q = deque([s])
    while len(Q) > 0:
        u = Q.popleft()
        for v in friends[u]:
            if color[v] is None:
                color[v] = color_id
                Q.append(v)


color_id = 0
color = [None] * n
for i in range(n):
    if color[i] is None:
        assign_color(i, color_id)
        color_id += 1

q = int(input())
ans = []
for _ in range(q):
    s, t = map(int, input().split())
    ans.append("yes" if color[s] == color[t] else "no")

print(*ans, sep="\n")
