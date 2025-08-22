from collections import defaultdict

def dfs(graph, node, visited, distance):
    visited[node] = True
    max_distance = distance
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            max_distance = max(max_distance, dfs(graph, neighbor, visited, distance + weight))
    return max_distance


N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    
visited = [False] * (N + 1)
max_distance = dfs(graph, 1, visited, 0)
print(max_distance)