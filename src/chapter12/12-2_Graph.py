n = int(input())
adjacency_list = []
for _ in range(n):
    adjacency_list.append(list(map(int, input().split())))

adjacency_matrices = [[0] * (n) for _ in range(n)]

for i in range(n):
    node_idx = adjacency_list[i][0] - 1  # 辺(u, v)のuのidx: 正直, iと同義
    adj_node_num = adjacency_list[i][1]  # 辺(u, v)のvの数
    for adj_node_idx in range(adj_node_num):
        idx = adjacency_list[node_idx][adj_node_idx + 2] - 1  # 辺(u, v_i)のv_iのidx
        adjacency_matrices[node_idx][idx] = 1

[print(*matric) for matric in adjacency_matrices]
