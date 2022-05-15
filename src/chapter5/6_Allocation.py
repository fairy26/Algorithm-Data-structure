n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]


def check(P: int):
    """最大積載量Pのk台のトラックで何個の荷物を積めるか？"""
    i = 0
    for _ in range(k):
        s = 0
        while s + w[i] <= P:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i


left = 0
right = (10 ** 5) * (10 ** 5)  # 荷物の最大個数 x １個当たりの最大重量
# 二分探索
while abs(right - left) > 1:
    mid = (left + right) // 2
    v = check(mid)
    if v >= n:
        right = mid
    else:
        left = mid

print(right)
