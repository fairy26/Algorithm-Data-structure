from math import log2
from typing import List


def insection_sort(A: List[int], n: int, g: int) -> int:
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

    return cnt


def shell_sort(A: List[int], n: int) -> int:
    cnt = 0
    m = int(log2(n))
    print(m)  # l.1

    #  数列Gを生成
    #  ver1: log2(n) - 1 -> 1
    # G = [2 ** i - 1 for i in range(m)]
    #  ver2
    h = 1
    G = []
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    print(*G)  # l.2

    #  ソート
    for i in reversed(range(m)):
        cnt += insection_sort(A, n, G[i])

    return cnt


def main():
    n = 5
    A = [5, 1, 4, 3, 2]
    cnt = shell_sort(A, n)
    print(cnt)  # l.3
    print(*A, sep="\n")  # l.4 ~


if __name__ == "__main__":
    main()
