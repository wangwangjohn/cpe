def dfs(node, color, graph, colors):
    # 檢查節點是否已經染色，若已染色，則確認顏色是否符合
    if colors[node] != 0:
        return colors[node] == color

    # 如果節點未染色過，將節點染色
    colors[node] = color

    # 遍歷所有相鄰節點
    for neighbor in graph[node]:
        # 若相鄰節點無法成功染色，則返回 False
        if not dfs(neighbor, -color, graph, colors):
            return False

    return True


while True:
    # n 節點數 m 邊數
    n = int(input())
    if n == 0:
        break
    m = int(input())

    # 初始化鄰接表，每個節點對應一個空列表
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a].append(b)
        graph[b].append(a)

    # 初始化顏色陣列，0表示未染色
    colors = [0] * n
    if dfs(0, 1, graph, colors):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
