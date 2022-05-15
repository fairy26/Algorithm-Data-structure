def insection_sort(A, n: int, g: int) -> int:
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


def shell_sort(A, n: int) -> int:
    cnt = 0

    #  数列Gを生成
    #  ver1: log2(n) - 1 -> 1
    # m = int(log2(n))
    # G = [2 ** i - 1 for i in range(m)][::-1]

    #  ver2
    h = 1
    G = []
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    m = len(G)
    G = G[::-1]  # reverse

    print(m)  # l.1
    print(*G)  # l.2

    #  ソート
    for g in G:
        cnt += insection_sort(A, n, g)

    return cnt


def get_input():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    return n, A


def main():
    # n, A = 5, [5, 1, 4, 3, 2]
    n, A = get_input()
    cnt = shell_sort(A, n)
    print(cnt)  # l.3
    print(*A, sep="\n")  # l.4 ~


if __name__ == "__main__":
    main()
