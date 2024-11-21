# 深度搜尋法
def dfs(node, color, graph, colors):
    # 檢查染色，如果節點已染色過需檢查是否與當前遞迴要染的顏色一樣
    if colors[node] != 0:
        return colors[node] == color
    # 染色
    colors[node] = color
    # 對當前的節點進行動作
    for i in graph[node]:
        if not dfs(i, -color, graph, colors):
            return False
    return True


while True:
    # n為節點數，m為邊數
    n = int(input())
    if n == 0:
        break
    m = int(input())
    # 初始化鄰接表，每個節點對應一個空列表
    graph = [[] for _ in range(n)]
    # 因為是強連通所以新增進鄰接表
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 顏色陣列，0代表尚未染色
    colors = [0]*n
    if dfs(0, 1, graph, colors) == True:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
